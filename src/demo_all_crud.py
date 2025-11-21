"""
Script maestro para ejecutar todas las operaciones CRUD
"""
from api_client import CiscoAPIClient
from crud_network_devices import *
from crud_hosts import *
from crud_users import *
from crud_discovery import *
from crud_policy_tags import *
import time


def print_section_header(title):
    """Imprime un encabezado de seccion"""
    print("\n\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def demo_all_endpoints():
    """Ejecuta una demostracion completa de todos los endpoints CRUD"""
    
    client = CiscoAPIClient()
    
    # NETWORK DEVICES
    print_section_header("1. NETWORK DEVICES - CRUD Completo")
    
    print("\nGET - Listar todos los dispositivos de red")
    get_all_network_devices(client)
    time.sleep(1)
    
    # POST
    print("\nPOST - Agregar nuevo dispositivo")
    create_network_device(client, "192.168.1.100")
    time.sleep(1)
    
    # GET por IP
    print("\nGET - Obtener dispositivo por IP")
    get_network_device_by_ip(client, "192.168.1.100")
    time.sleep(1)
    
    # PUT
    print("\nPUT - Actualizar dispositivo")
    update_network_device(client, "device-id-here")
    time.sleep(1)
    
    # DELETE
    print("\nDELETE - Eliminar dispositivo por IP")
    delete_network_device_by_ip(client, "192.168.1.100")
    time.sleep(1)
    
    # HOSTS
    print_section_header("2. HOSTS - Operaciones GET y DELETE")
    
    print("\nGET - Contar hosts")
    get_host_count(client)
    time.sleep(1)
    
    print("\nGET - Listar todos los hosts")
    get_all_hosts(client)
    time.sleep(1)
    
    # GET por IP
    print("\nGET - Obtener host por IP")
    get_host_by_ip(client, "172.16.1.30")
    time.sleep(1)
    
    # DELETE
    # print("\nDELETE - Eliminar host")
    # delete_host_by_ip(client, "172.16.1.30")
    # time.sleep(1)
    
    # USERS
    print_section_header("3. USERS - CRUD Completo")
    
    print("\nGET - Listar todos los usuarios")
    get_all_users(client)
    time.sleep(1)
    
    # POST
    # print("\nPOST - Crear nuevo usuario")
    # create_user(client, "testuser", "TestPass123!", "ROLE-OBSERVER")
    # time.sleep(1)
    
    # GET
    # print("\nGET - Obtener usuario especifico")
    # get_user(client, "testuser")
    # time.sleep(1)
    
    # PUT
    # print("\nPUT - Actualizar usuario")
    # update_user(client, "testuser", new_password="NewPass456!")
    # time.sleep(1)
    
    # DELETE
    # print("\nDELETE - Eliminar usuario")
    # delete_user(client, "testuser")
    # time.sleep(1)
    
    # DISCOVERY
    print_section_header("4. DISCOVERY - CRUD Completo")
    
    print("\nGET - Contar discoveries")
    get_discovery_count(client)
    time.sleep(1)
    
    print("\nGET - Listar todos los discoveries")
    get_all_discoveries(client)
    time.sleep(1)
    
    # POST
    # print("\nPOST - Crear nuevo discovery")
    # create_discovery(client, "Test-Discovery", "192.168.1.1-192.168.1.50")
    # time.sleep(1)
    
    # GET por ID
    # print("\nGET - Obtener discovery por ID")
    # get_discovery_by_id(client, "discovery-id-here")
    # time.sleep(1)
    
    # PUT
    # print("\nPUT - Actualizar discovery")
    # update_discovery(client, "discovery-id-here", name="Updated-Discovery")
    # time.sleep(1)
    
    # DELETE
    # print("\nDELETE - Eliminar discovery")
    # delete_discovery_by_id(client, "discovery-id-here")
    # time.sleep(1)
    
    # POLICY TAGS
    print_section_header("5. POLICY TAGS - POST, GET, DELETE")
    
    print("\nGET - Contar policy tags")
    get_policy_tags_count(client)
    time.sleep(1)
    
    print("\nGET - Listar todos los policy tags")
    get_all_policy_tags(client)
    time.sleep(1)
    
    # POST
    # print("\nPOST - Crear nuevo policy tag")
    # create_policy_tag(client, "Test-Tag", "Tag de prueba")
    # time.sleep(1)
    
    # DELETE
    # print("\nDELETE - Eliminar policy tag")
    # delete_policy_tag(client, "tag-id-here")
    # time.sleep(1)
    
    print("\n" + "="*70)
    print("Demostracion completada exitosamente")
    print("="*70)
    print("\n")


if __name__ == "__main__":
    demo_all_endpoints()
