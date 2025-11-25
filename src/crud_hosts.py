"""
CRUD para Hosts
Endpoints: GET, DELETE
"""
from api_client import CiscoAPIClient
from tabulate import tabulate
import json


def get_all_hosts(client: CiscoAPIClient):
    """GET - Obtener todos los hosts"""
    print("\n" + "="*60)
    print("GET - Obtener todos los Hosts")
    print("="*60)
    
    try:
        response = client.get("/host")
        
        if "response" in response:
            hosts = response["response"]
            print(f"\nTotal de hosts: {len(hosts)}")
            
            # Formatear en tabla
            table_data = []
            for host in hosts:
                table_data.append([
                    host.get("id", "N/A"),
                    host.get("hostName", "N/A"),
                    host.get("hostIp", "N/A"),
                    host.get("hostMac", "N/A"),
                    host.get("hostType", "N/A"),
                    host.get("vlanId", "N/A")
                ])
            
            print(tabulate(
                table_data,
                headers=["ID", "Hostname", "IP", "MAC", "Type", "VLAN"],
                tablefmt='grid'
            ))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_host_by_ip(client: CiscoAPIClient, ip_address: str):
    """GET - Obtener host por IP"""
    print("\n" + "="*60)
    print(f"GET - Obtener Host por IP: {ip_address}")
    print("="*60)
    
    try:
        response = client.get(f"/host/ip-address/{ip_address}")
        
        if "response" in response:
            host = response["response"]
            
            # Mostrar detalles del host
            details = [
                ["ID", host.get("id", "N/A")],
                ["Hostname", host.get("hostName", "N/A")],
                ["IP Address", host.get("hostIp", "N/A")],
                ["MAC Address", host.get("hostMac", "N/A")],
                ["Host Type", host.get("hostType", "N/A")],
                ["VLAN ID", host.get("vlanId", "N/A")],
                ["Connected Device", host.get("connectedNetworkDeviceId", "N/A")],
                ["Connected Interface", host.get("connectedInterfaceName", "N/A")],
            ]
            
            print("\nDetalles del host:")
            print(tabulate(details, headers=["Campo", "Valor"], tablefmt='grid'))
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_host_count(client: CiscoAPIClient):
    """GET - Obtener cantidad de hosts"""
    print("\n" + "="*60)
    print("GET - Obtener cantidad de Hosts")
    print("="*60)
    
    try:
        response = client.get("/host/count")
        
        if "response" in response:
            count = response["response"]
            print(f"\nTotal de hosts en la red: {count}")
        else:
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


def delete_host_by_ip(client: CiscoAPIClient, ip_address: str):
    """DELETE - Eliminar host por IP"""
    print("\n" + "="*60)
    print(f"DELETE - Eliminar Host por IP: {ip_address}")
    print("="*60)
    
    try:
        response = client.delete(f"/host/ip-address/{ip_address}")
        
        if "response" in response:
            print("\nRespuesta de la API:")
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Crear cliente API
    client = CiscoAPIClient()
    
    # Demostracion de operaciones con Hosts
    print("\n" + "="*60)
    print("DEMOSTRACION - HOSTS")
    print("="*60)
    
    # 1. GET - Contar hosts
    get_host_count(client)
    
    # 2. GET - Listar todos los hosts
    get_all_hosts(client)
    
    # 3. GET - Obtener host especifico por IP
    # get_host_by_ip(client, "172.16.1.30")
    
    # 4. DELETE - Eliminar host por IP
    # delete_host_by_ip(client, "172.16.1.30")
    
    print("\n" + "="*60)
    print("Demostracion completada")
    print("="*60)
