"""
CRUD para Users
Endpoints: POST, GET, PUT, DELETE
"""
from api_client import CiscoAPIClient
from tabulate import tabulate
import json


def create_user(client: CiscoAPIClient, username: str, password: str, role: str = "ROLE-OBSERVER"):
    """POST - Crear un nuevo usuario"""
    print("\n" + "="*60)
    print("POST - Crear nuevo Usuario")
    print("="*60)
    
    data = {
        "username": username,
        "password": password,
        "role": role
    }
    
    print(f"Creando usuario: {username} con rol: {role}")
    
    try:
        response = client.post("/user", data)
        
        if "response" in response:
            user = response["response"]
            result = [
                ["Username", user.get("username", "N/A")],
                ["Role", user.get("role", "N/A")],
                ["Authorization", user.get("authorization", "N/A")]
            ]
            print("\nUsuario creado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_all_users(client: CiscoAPIClient):
    """GET - Obtener todos los usuarios"""
    print("\n" + "="*60)
    print("GET - Obtener todos los Usuarios")
    print("="*60)
    
    try:
        response = client.get("/user")
        
        if "response" in response:
            users = response["response"]
            print(f"\nTotal de usuarios: {len(users)}")
            
            # Formatear en tabla
            table_data = []
            for user in users:
                table_data.append([
                    user.get("username", "N/A"),
                    user.get("role", "N/A"),
                    user.get("authorization", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["Username", "Role", "Authorization"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_user(client: CiscoAPIClient, username: str):
    """GET - Obtener usuario especifico"""
    print("\n" + "="*60)
    print(f"GET - Obtener Usuario: {username}")
    print("="*60)
    
    try:
        response = client.get(f"/user/{username}")
        
        if "response" in response:
            user = response["response"]
            
            # Mostrar detalles del usuario
            details = [
                ["Username", user.get("username", "N/A")],
                ["Role", user.get("role", "N/A")],
                ["Authorization", user.get("authorization", "N/A")]
            ]
            
            print("\nDetalles del usuario:")
            print(tabulate(details, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def update_user(client: CiscoAPIClient, username: str, new_password: str = None, new_role: str = None):
    """PUT - Actualizar usuario"""
    print("\n" + "="*60)
    print(f"PUT - Actualizar Usuario: {username}")
    print("="*60)
    
    data = {
        "username": username
    }
    
    if new_password:
        data["password"] = new_password
    if new_role:
        data["role"] = new_role
    
    try:
        response = client.put("/user", data)
        
        if "response" in response:
            user = response["response"]
            result = [
                ["Username", user.get("username", "N/A")],
                ["Role", user.get("role", "N/A")],
                ["Authorization", user.get("authorization", "N/A")]
            ]
            print("\nUsuario actualizado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_user(client: CiscoAPIClient, username: str):
    """DELETE - Eliminar usuario"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar Usuario: {username}")
    print("="*60)
    
    try:
        response = client.delete(f"/user/{username}")
        
        print("\nUsuario eliminado exitosamente")
        print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Crear cliente API
    client = CiscoAPIClient()
    
    # Demostracion de CRUD completo
    print("\n" + "="*60)
    print("DEMOSTRACION CRUD - USERS")
    print("="*60)
    
    # 1. GET - Listar todos los usuarios
    get_all_users(client)
    
    # 2. POST - Crear nuevo usuario
    # create_user(client, "testuser", "TestPass123!", "ROLE-OBSERVER")
    
    # 3. GET - Obtener usuario especifico
    # get_user(client, "testuser")
    
    # 4. PUT - Actualizar usuario
    # update_user(client, "testuser", new_password="NewPass456!", new_role="ROLE-ADMIN")
    
    # 5. DELETE - Eliminar usuario
    # delete_user(client, "testuser")
    
    print("\n" + "="*60)
    print("Demostracion completada")
    print("="*60)
