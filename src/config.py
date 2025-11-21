"""
Configuracion centralizada para la API de Cisco Packet Tracer
"""

# Configuracion del servidor API
API_BASE_URL = "http://localhost:58000/api/v1"

# Credenciales de autenticacion
USERNAME = "admin"
PASSWORD = "admin"

# IPs de dispositivos de la topologia de red
NETWORK_DEVICES = {
    # Routers
    "R-ISP": "11.1.1.230",
    "R-Central": "10.0.0.17/30",
    "R-Sucursal": "10.0.0.19/30",
    
    # Switches
    "S0-Central": "172.16.1.126/27",
    "S1-Central": "172.16.1.127",
    "S2-Central": "172.16.1.1/27",
    "S0-Sucursal": "172.16.3.126/27",
    "S1-Sucursal": "172.16.3.127/27",
    
    # Servidores
    "Server-PT": "172.16.1.27/27",
    "Server-NTP": "203.0.113.24",
    "Server-FTP": "203.0.113.24",
    "Server-HTTP": "203.0.113.7.24",
    
    # PCs de ejemplo
    "PC-Operaciones": "172.16.1.30",
    "PC-Administracion": "172.16.1.2/22",
    "PC-Backup": "172.16.1.33/27",
    "PC-Mantenimiento": "172.16.1.33/27",
}

# Headers comunes para las peticiones
HEADERS_JSON = {
    "content-type": "application/json"
}

def get_auth_headers(ticket):
    """Retorna headers con el ticket de autenticacion"""
    return {
        "X-Auth-Token": ticket,
        "content-type": "application/json" # ES REQUERIDO SIEMPRE
    }
