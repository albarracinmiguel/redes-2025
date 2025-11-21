"""
CRUD para Policy Tags
Endpoints: POST, GET, DELETE
"""
from api_client import CiscoAPIClient
from tabulate import tabulate
import json


def create_policy_tag(client: CiscoAPIClient, tag_name: str, description: str = ""):
    """POST - Crear un nuevo policy tag"""
    print("\n" + "="*60)
    print("POST - Crear nuevo Policy Tag")
    print("="*60)
    
    data = {
        "policyTag": tag_name,
        "description": description
    }
    
    print(f"Creando policy tag: {tag_name}")
    
    try:
        response = client.post("/policy/tag", data)
        
        if "response" in response:
            tag = response["response"]
            result = [
                ["Policy Tag", tag.get("policyTag", "N/A")],
                ["Description", tag.get("description", "N/A")],
                ["ID", tag.get("id", "N/A")]
            ]
            print("\nPolicy tag creado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_all_policy_tags(client: CiscoAPIClient):
    """GET - Obtener todos los policy tags"""
    print("\n" + "="*60)
    print("GET - Obtener todos los Policy Tags")
    print("="*60)
    
    try:
        response = client.get("/policy/tag")
        
        if "response" in response:
            tags = response["response"]
            print(f"\nTotal de policy tags: {len(tags)}")
            
            # Formatear en tabla
            table_data = []
            for tag in tags:
                table_data.append([
                    tag.get("id", "N/A"),
                    tag.get("policyTag", "N/A"),
                    tag.get("description", "N/A"),
                    tag.get("dynamicRules", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["ID", "Policy Tag", "Description", "Dynamic Rules"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_policy_tags_count(client: CiscoAPIClient):
    """GET - Obtener cantidad de policy tags"""
    print("\n" + "="*60)
    print("GET - Obtener cantidad de Policy Tags")
    print("="*60)
    
    try:
        response = client.get("/policy/tag/count")
        
        if "response" in response:
            count = response["response"]
            print(f"\nTotal de policy tags: {count}")
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_policy_tag(client: CiscoAPIClient, tag_id: str):
    """DELETE - Eliminar policy tag"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar Policy Tag ID: {tag_id}")
    print("="*60)
    
    try:
        response = client.delete(f"/policy/tag/{tag_id}")
        
        if "response" in response:
            result = [[
                "Task ID", response["response"].get("taskId", "N/A")
            ], [
                "URL", response["response"].get("url", "N/A")
            ]]
            print("\nPolicy tag eliminado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Crear cliente API
    client = CiscoAPIClient()
    
    # Demostracion de operaciones con Policy Tags
    print("\n" + "="*60)
    print("DEMOSTRACION - POLICY TAGS")
    print("="*60)
    
    # 1. GET - Contar policy tags
    get_policy_tags_count(client)
    
    # 2. GET - Listar todos los policy tags
    get_all_policy_tags(client)
    
    # 3. POST - Crear nuevo policy tag
    # create_policy_tag(client, "Test-Tag", "Tag de prueba para demostracion")
    
    # 4. DELETE - Eliminar policy tag
    # delete_policy_tag(client, "tag-id-here")
    
    print("\n" + "="*60)
    print("Demostracion completada")
    print("="*60)
