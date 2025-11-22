"""
CRUD para Global Credentials (CLI)
Endpoints: GET, POST, PUT, DELETE
"""
from api_client import CiscoAPIClient
from tabulate import tabulate
import json


def get_global_credentials(client: CiscoAPIClient):
    """GET - Obtener todas las credenciales globales CLI"""
    print("\n" + "="*60)
    print("GET - Obtener todas las credenciales globales CLI")
    print("="*60)
    
    try:
        response = client.get("/global-credential/cli")
        
        if "response" in response:
            credentials = response["response"]
            print(f"\nTotal de credenciales: {len(credentials)}")
            
            # Formatear en tabla
            table_data = []
            for cred in credentials:
                table_data.append([
                    cred.get("id", "N/A"),
                    cred.get("username", "N/A"),
                    cred.get("description", "N/A"),
                    cred.get("comments", "N/A"),
                    cred.get("credentialType", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["ID", "Username", "Description", "Comments", "Type"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def create_cli_credential(client: CiscoAPIClient, username: str, password: str, 
                          enable_password: str, description: str = "", 
                          comments: str = ""):
    """POST - Crear nueva credencial CLI"""
    print("\n" + "="*60)
    print(f"POST - Crear nueva credencial CLI: {username}")
    print("="*60)
    
    try:
        payload = {
            "username": username,
            "password": password,
            "enablePassword": enable_password,
            "description": description,
            "comments": comments,
            "credentialType": "GLOBAL"
        }
        
        response = client.post("/global-credential/cli", payload)
        
        if "response" in response:
            result = [[
                "Response", response.get("response", "N/A")
            ], [
                "Version", response.get("version", "N/A")
            ]]
            
            if response.get("response") == True:
                print("\n✓ Credencial creada exitosamente:")
            else:
                print("\n✗ Error al crear credencial:")
            
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def update_cli_credential(client: CiscoAPIClient, credential_id: str, 
                          username: str, password: str, enable_password: str,
                          description: str = "", comments: str = ""):
    """PUT - Actualizar credencial CLI"""
    print("\n" + "="*60)
    print(f"PUT - Actualizar credencial CLI: {credential_id}")
    print("="*60)
    
    try:
        payload = {
            "id": credential_id,
            "username": username,
            "password": password,
            "enablePassword": enable_password,
            "description": description,
            "comments": comments,
            "credentialType": "GLOBAL"
        }
        
        response = client.put("/global-credential/cli", payload)
        
        if "response" in response:
            result = [[
                "Response", response.get("response", "N/A")
            ], [
                "Version", response.get("version", "N/A")
            ]]
            
            if response.get("response") == True:
                print("\n✓ Credencial actualizada exitosamente:")
            else:
                print("\n✗ Error al actualizar credencial:")
            
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_global_credential(client: CiscoAPIClient, credential_id: str):
    """DELETE - Eliminar credencial global por ID"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar credencial global: {credential_id}")
    print("="*60)
    
    try:
        response = client.delete(f"/global-credential/{credential_id}")
        
        if "response" in response:
            result = [[
                "Response", response.get("response", "N/A")
            ], [
                "Version", response.get("version", "N/A")
            ]]
            
            if response.get("response") == True:
                print("\n✓ Credencial eliminada exitosamente:")
            else:
                print("\n✗ Error al eliminar credencial:")
            
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
    
    # Demostracion de operaciones con Credentials
    print("\n" + "="*60)
    print("DEMOSTRACION - GLOBAL CREDENTIALS")
    print("="*60)
    
    # 1. GET - Listar todas las credenciales
    get_global_credentials(client)
    
    # 2. POST - Crear nueva credencial
    # create_cli_credential(client, "admin", "admin", "admin", 
    #                       "Postman", "Ingresado desde Postman")
    
    # 3. PUT - Actualizar credencial
    # update_cli_credential(client, "credential-id-here", "admin", "admin", 
    #                       "admin", "Postman Actualizado", 
    #                       "Actualizado desde Postman")
    
    # 4. DELETE - Eliminar credencial
    # delete_global_credential(client, "credential-id-here")
    
    print("\n" + "="*60)
    print("Demostracion completada")
    print("="*60)
