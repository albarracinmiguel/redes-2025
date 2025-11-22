"""
CRUD Completo para Network Devices
Endpoints: POST, GET, PUT, DELETE
"""
from api_client import CiscoAPIClient
from tabulate import tabulate
import json


def create_network_device(client: CiscoAPIClient, ip_address: str):
    """POST - Agregar un nuevo dispositivo de red"""
    print("\n" + "="*60)
    print("POST - Agregar Network Device")
    print("="*60)
    
    data = {
        "ipAddress": [ip_address]
    }
    
    print(f"Agregando dispositivo con IP: {ip_address}")
    
    try:
        response = client.post("/network-device", data)
        
        if "response" in response:
            result = [[
                "Task ID", response["response"].get("taskId", "N/A")
            ], [
                "URL", response["response"].get("url", "N/A")
            ]]
            print("\nDispositivo agregado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_all_network_devices(client: CiscoAPIClient):
    """GET - Obtener todos los dispositivos de red"""
    print("\n" + "="*60)
    print("GET - Obtener todos los Network Devices")
    print("="*60)
    
    try:
        response = client.get("/network-device")
        
        if "response" in response:
            devices = response["response"]
            print(f"\nTotal de dispositivos: {len(devices)}")
            
            # Formatear en tabla
            table_data = []
            for device in devices:
                table_data.append([
                    device.get("id", "N/A"),
                    device.get("hostname", "N/A"),
                    device.get("managementIpAddress", "N/A"),
                    device.get("platformId", "N/A"),
                    device.get("type", "N/A"),
                    device.get("reachabilityStatus", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["ID", "Hostname", "IP", "Platform", "Type", "Status"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_network_device_by_ip(client: CiscoAPIClient, ip_address: str):
    """GET - Obtener dispositivo por IP"""
    print("\n" + "="*60)
    print(f"GET - Obtener Network Device por IP: {ip_address}")
    print("="*60)
    
    try:
        response = client.get(f"/network-device/ip-address/{ip_address}")
        
        if "response" in response:
            device = response["response"]
            
            # Mostrar detalles del dispositivo
            details = [
                ["ID", device.get("id", "N/A")],
                ["Hostname", device.get("hostname", "N/A")],
                ["IP Address", device.get("managementIpAddress", "N/A")],
                ["Platform", device.get("platformId", "N/A")],
                ["Type", device.get("type", "N/A")],
                ["Serial Number", device.get("serialNumber", "N/A")],
                ["Software Version", device.get("softwareVersion", "N/A")],
                ["Reachability", device.get("reachabilityStatus", "N/A")],
                ["Role", device.get("role", "N/A")],
            ]
            
            print("\nDetalles del dispositivo:")
            print(tabulate(details, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def update_network_device(client: CiscoAPIClient, ip_address: str, global_credential_id: str):
    """PUT - Actualizar dispositivo de red"""
    print("\n" + "="*60)
    print(f"PUT - Network Device IP: {ip_address}")
    print("="*60)
    
    data = {
        "ipAddress": ip_address,
        "globalCredentialId": global_credential_id
    }
    
    try:
        response = client.put("/network-device", data)
        
        if "response" in response or "discoveryId" in response:
            result = [[
                "Discovery ID", response.get("discoveryId", "N/A")
            ], [
                "Version", response.get("version", "N/A")
            ]]
            
            print("\n✓ Dispositivo actualizado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_network_device_by_id(client: CiscoAPIClient, device_id: str):
    """DELETE - Eliminar dispositivo por ID"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar Network Device ID: {device_id}")
    print("="*60)
    
    try:
        response = client.delete(f"/network-device/{device_id}")
        
        if "response" in response:
            result = [[
                "Task ID", response["response"].get("taskId", "N/A")
            ], [
                "URL", response["response"].get("url", "N/A")
            ]]
            print("\nDispositivo eliminado exitosamente:")
            print(tabulate(result, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_network_device_by_ip(client: CiscoAPIClient, ip_address: str):
    """DELETE - Eliminar dispositivo por IP"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar Network Device por IP: {ip_address}")
    print("="*60)
    
    try:
        response = client.delete(f"/network-device/ip-address/{ip_address}")
        
        if "response" in response:
            result = [[
                "Task ID", response["response"].get("taskId", "N/A")
            ], [
                "URL", response["response"].get("url", "N/A")
            ]]
            print("\nDispositivo eliminado exitosamente:")
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
    print("DEMOSTRACION CRUD - NETWORK DEVICES")
    print("="*60)
    
    # 1. GET - Listar todos los dispositivos
    get_all_network_devices(client)
    
    # 2. POST - Agregar nuevo dispositivo (usar IP de tu topologia)
    # create_network_device(client, "192.168.1.1")
    
    # 3. GET - Obtener dispositivo especifico por IP
    # get_network_device_by_ip(client, "192.168.1.1")
    
    # 4. PUT - Actualizar dispositivo (necesitas el ID del dispositivo)
    # update_network_device(client, "device-id-here")
    
    # 5. DELETE - Eliminar dispositivo por ID
    # delete_network_device_by_id(client, "device-id-here")
    
    # 6. DELETE - Eliminar dispositivo por IP
    # delete_network_device_by_ip(client, "192.168.1.1")
    
    print("\n" + "="*60)
    print("Demostracion completada")
    print("="*60)
