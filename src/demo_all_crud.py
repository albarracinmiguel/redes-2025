"""
Script maestro para ejecutar todas las operaciones CRUD

"""
from api_client import CiscoAPIClient
from crud_network_devices import *
from crud_hosts import *
from crud_users import *
from crud_discovery import *
from crud_credentials import *
import time


def print_section_header(title):
    """Imprime un encabezado de seccion"""
    print("\n\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def demo_all_endpoints():
    """Ejecuta una demostracion"""
    
    client = CiscoAPIClient()

    # ========================================================================
    # 1. NETWORK DEVICES
    # ========================================================================
    print_section_header("1. NETWORK DEVICES")
    
    print("\nGET - Listar todos los dispositivos de red")
    get_all_network_devices(client)
    time.sleep(1)
    
    print("\nGET - Obtener dispositivo por IP: 172.16.0.190")
    get_network_device_by_ip(client, "172.16.0.190")
    time.sleep(1)
    
    # POST - Agregar nuevo dispositivo
    print("\nPOST - Agregar nuevo dispositivo: 172.16.0.199")
    create_network_device(client, "172.16.0.199")
    time.sleep(1)
    
    # PUT - Actualizar dispositivo (requiere IP y globalCredentialId)
    # El globalCredentialId se puede obtener de GET /global-credential/cli
    # Usando el ID del ejemplo de Postman
    print("\nPUT - Actualizar dispositivo con IP y credencial global")
    update_network_device(client, "172.16.0.199", "3eb4d174-af61-41d0-82a0-00b05bc44147")
    time.sleep(1)
    
    # DELETE - Eliminar dispositivo por IP
    print("\nDELETE - Eliminar dispositivo por IP: 172.16.0.199")
    delete_network_device_by_ip(client, "172.16.0.199")
    time.sleep(1)
    
    # ========================================================================
    # 2. HOSTS 
    # ========================================================================
    print_section_header("2. HOSTS ")
    
    print("\nGET - Contar hosts")
    get_host_count(client)
    time.sleep(1)
    
    print("\nGET - Listar todos los hosts")
    get_all_hosts(client)
    time.sleep(1)
    
    print("\nGET - Obtener host por IP: 172.16.1.33")
    get_host_by_ip(client, "172.16.1.33")
    time.sleep(1)
    
    # DELETE - Eliminar host por IP - DESCOMENTAR EN CASO DE QUERER ELIMINAR, PERO NO SE PUEDE AGREGAR HOSTS POR API
    # print("\nDELETE - Eliminar host por IP: 172.16.1.33")
    # delete_host_by_ip(client, "172.16.1.33")
    # time.sleep(1)
    
    # ========================================================================
    # 3. USERS
    # ========================================================================
    print_section_header("3. USERS - CRUD")
    
    print("\nGET - Listar todos los usuarios")
    get_all_users(client)
    time.sleep(1)
    
    print("\nGET - Obtener usuario especifico: admin")
    get_user(client, "admin")
    time.sleep(1)
    
    # POST - Crear nuevo usuario
    print("\nPOST - Crear nuevo usuario: testusername")
    create_user(client, "testusername", "testpassword", "ROLE_ADMIN")
    time.sleep(1)
    
    # PUT - Actualizar usuario
    print("\nPUT - Actualizar usuario: testusername")
    update_user(client, "testusername", new_password="testuser123", new_role="ROLE_ADMIN")
    time.sleep(1)
    
    # DELETE - Eliminar usuario
    print("\nDELETE - Eliminar usuario: testusername")
    delete_user(client, "testusername")
    time.sleep(1)
    
    # ========================================================================
    # 4. DISCOVERY
    # ========================================================================
    print_section_header("4. DISCOVERY")
    
    print("\nGET - Contar discoveries")
    get_discovery_count(client)
    time.sleep(1)
    
    print("\nGET - Listar todos los discoveries")
    get_all_discoveries(client)
    time.sleep(1)
    
    print("\nGET - Obtener discovery por ID: 0")
    get_discovery_by_id(client, "0")
    time.sleep(1)
    
    # POST - Crear nuevo discovery
    print("\nPOST - Crear nuevo discovery")
    discovery_id = create_discovery(client, "discovery ejemplo", discovery_type="Range", ip_address_list="192.168.100.106")
    time.sleep(1)
    
    # PUT - Actualizar discovery
    print("\nPUT - Actualizar discovery ID: ", discovery_id)
    update_discovery(client, discovery_id, discovery_type = "CDP", name="CDP - Modificado")
    time.sleep(1)
    
    # DELETE - Eliminar discovery
    print("\nDELETE - Eliminar discovery ID:", discovery_id)
    delete_discovery_by_id(client, discovery_id)
    time.sleep(1)
    
    # # ========================================================================
    # # 5. CREDENTIALS - CRUD
    # # ========================================================================
    print_section_header("5. CREDENTIALS - CRUD Completo")
    
    print("\nGET - Listar todas las credenciales globales CLI")
    get_global_credentials(client)
    time.sleep(1)
    
    # POST - Crear nueva credencial
    print("\nPOST - Crear nueva credencial CLI")
    credential_id = create_cli_credential(client, "admin2", "admin2", "admin2", 
                          "Postman", "Ingresado desde API")
    time.sleep(1)
    
    # PUT - Actualizar credencial (requiere ID de la credencial)
    print("\nPUT - Actualizar credencial CLI")
    update_cli_credential(client, credential_id, 
                          "admin3", "admin3", "admin3",
                          "Actualizado", "Actualizado desde API")
    time.sleep(1)
    
    # DELETE - Eliminar credencial (requiere ID de la credencial)
    print("\nDELETE - Eliminar credencial global ID:", credential_id)
    delete_global_credential(client, credential_id)
    time.sleep(1)


if __name__ == "__main__":
    demo_all_endpoints()
