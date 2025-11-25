"""
CRUD para Discovery
Endpoints: POST, GET, PUT, DELETE
"""
from api_client import CiscoAPIClient
from tabulate import tabulate
import json


def create_discovery(client: CiscoAPIClient, name: str, ip_range: str, discovery_type: str = "Range"):
    """POST - Iniciar un nuevo proceso de discovery"""
    print("\n" + "="*60)
    print("POST - Crear nuevo Discovery")
    print("="*60)
    
    data = {
        "name": name,
        "discoveryType": discovery_type,
        "ipAddressList": ip_range,
        "protocolOrder": "ssh,telnet",
        "timeout": 5,
        "retry": 3
    }
    
    print(f"Iniciando discovery: {name} para rango: {ip_range}")
    
    try:
        response = client.post("/discovery", data)
        
        if "response" in response:
            print(json.dumps(response, indent=2))
            
        return response["discoveryId"]
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_all_discoveries(client: CiscoAPIClient):
    """GET - Obtener todos los discoveries"""
    print("\n" + "="*60)
    print("GET - Obtener todos los Discoveries")
    print("="*60)
    
    try:
        response = client.get("/discovery")
        
        if "response" in response:
            discoveries = response["response"]
            print(f"\nTotal de discoveries: {len(discoveries)}")
            
            # Formatear en tabla
            table_data = []
            for disc in discoveries:
                table_data.append([
                    disc.get("id", "N/A"),
                    disc.get("name", "N/A"),
                    disc.get("discoveryType", "N/A"),
                    disc.get("ipAddressList", "N/A"),
                    disc.get("discoveryStatus", "N/A"),
                    disc.get("numDevices", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["ID", "Name", "Type", "IP Range", "Status", "Devices"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_discovery_by_id(client: CiscoAPIClient, discovery_id: str):
    """GET - Obtener discovery por ID"""
    print("\n" + "="*60)
    print(f"GET - Obtener Discovery ID: {discovery_id}")
    print("="*60)
    
    try:
        response = client.get(f"/discovery/{discovery_id}")
        
        if "response" in response:
            disc = response["response"]
            
            # Mostrar detalles del discovery
            details = [
                ["ID", disc.get("id", "N/A")],
                ["Name", disc.get("name", "N/A")],
                ["Discovery Type", disc.get("discoveryType", "N/A")],
                ["IP Address List", disc.get("ipAddressList", "N/A")],
                ["Status", disc.get("discoveryStatus", "N/A")],
                ["Protocol Order", disc.get("protocolOrder", "N/A")],
                ["Timeout", disc.get("timeout", "N/A")],
                ["Retry", disc.get("retry", "N/A")],
                ["Num Devices", disc.get("numDevices", "N/A")],
            ]
            
            print("\nDetalles del discovery:")
            print(tabulate(details, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def getNetworkDeviceByDiscoveryId(client: CiscoAPIClient, discovery_id: str):
    """GET - Obtener Network Device por Discovery ID"""
    print("\n" + "="*60)
    print(f"GET - Obtener Network Device por Discovery ID: {discovery_id}")
    print("="*60)
    
    try:
        response = client.get(f"/discovery/{discovery_id}/networkDevice")
        
        if "response" in response:  
            devices = response["response"]
            print(f"\nTotal de discoveries: {len(devices)}")
            
            # Formatear en tabla
            table_data = []
            for device in devices:
                table_data.append([
                    device.get("id", "N/A"),
                    device.get("name", "N/A"),
                    device.get("ipAddress", "N/A"),
                    device.get("discoveryType", "N/A"),
                    device.get("discoveryStatus", "N/A"),
                    device.get("numDevices", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["ID", "Name", "IP Address", "Discovery Type", "Discovery Status", "Num Devices"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_discovery_count(client: CiscoAPIClient):
    """GET - Obtener cantidad de discoveries"""
    print("\n" + "="*60)
    print("GET - Obtener cantidad de Discoveries")
    print("="*60)
    
    try:
        response = client.get("/discovery/count")
        
        if "response" in response:
            count = response["response"]
            print(f"\nTotal de discoveries: {count}")
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def update_discovery(client: CiscoAPIClient, discovery_id: str, name: str, discovery_type: str, ip_range: str = None):
    """PUT - Actualizar discovery"""
    print("\n" + "="*60)
    print(f"PUT - Actualizar Discovery ID: {discovery_id}")
    print("="*60)
    
    data = {
        "id": discovery_id,
        "name": name,
        "discoveryType": discovery_type
    }

    try:
        response = client.put("/discovery", data)
        
        if "response" in response:

            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_discovery_by_id(client: CiscoAPIClient, discovery_id: str):
    """DELETE - Eliminar discovery por ID"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar Discovery ID: {discovery_id}")
    print("="*60)
    
    try:
        response = client.delete(f"/discovery/{discovery_id}")
        
        if "response" in response:
            result = [[
                "Task ID", response["response"].get("taskId", "N/A")
            ], [
                "URL", response["response"].get("url", "N/A")
            ]]
            print("\nDiscovery eliminado exitosamente:")
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
    
    # Demostracion de CRUD completo
    print("\n" + "="*60)
    print("DEMOSTRACION CRUD - DISCOVERY")
    print("="*60)
    
    # 1. GET - Contar discoveries
    get_discovery_count(client)
    
    # 2. GET - Listar todos los discoveries
    get_all_discoveries(client)
    
    # 3. POST - Crear nuevo discovery
    # create_discovery(client, "Test-Discovery", "192.168.1.1-192.168.1.10")
    
    # 4. GET - Obtener discovery especifico
    # get_discovery_by_id(client, "ID")
    
    # 5. PUT - Actualizar discovery
    # update_discovery(client, "ID", name="Updated-Discovery")
    
    # 6. DELETE - Eliminar discovery
    # delete_discovery_by_id(client, "ID")
    
    print("\n" + "="*60)
    print("Demostracion completada")
    print("="*60)
