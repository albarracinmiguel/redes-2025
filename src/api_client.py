"""
Cliente de API reutilizable para Cisco Packet Tracer Northbound API
"""
import json
import requests
from typing import Dict, Any, Optional
from config import API_BASE_URL, USERNAME, PASSWORD, HEADERS_JSON, get_auth_headers


class CiscoAPIClient:
    """Cliente para interactuar con la API de Cisco Packet Tracer"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.ticket = None
        
    def get_ticket(self, username: str = USERNAME, password: str = PASSWORD) -> str:
        """
        Obtiene un ticket de autenticacion
        
        Args:
            username: Nombre de usuario
            password: Contrasena
            
        Returns:
            Service ticket string
        """
        url = f"{self.base_url}/ticket"
        body = {
            "username": username,
            "password": password
        }
        
        try:
            resp = requests.post(url, json.dumps(body), headers=HEADERS_JSON)
            resp.raise_for_status()
            
            response_json = resp.json()
            self.ticket = response_json["response"]["serviceTicket"]
            
            print(f"Ticket obtenido exitosamente: {self.ticket}")
            return self.ticket
            
        except requests.exceptions.RequestException as e:
            print(f"Error obteniendo ticket: {e}")
            raise
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Realiza una peticion GET
        
        Args:
            endpoint: Endpoint de la API (ej: '/network-device')
            params: Parametros query opcionales
            
        Returns:
            Respuesta JSON
        """
        if not self.ticket:
            self.get_ticket()
            
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(self.ticket)
        
        try:
            resp = requests.get(url, headers=headers, params=params)
            resp.raise_for_status()
            return resp.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error en GET {endpoint}: {e}")
            if hasattr(e.response, 'text'):
                print(f"Respuesta: {e.response.text}")
            raise
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Realiza una peticion POST
        
        Args:
            endpoint: Endpoint de la API
            data: Datos a enviar en el body
            
        Returns:
            Respuesta JSON
        """
        if not self.ticket:
            self.get_ticket()
            
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(self.ticket)
        
        try:
            resp = requests.post(url, json.dumps(data), headers=headers)
            resp.raise_for_status()
            return resp.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error en POST {endpoint}: {e}")
            if hasattr(e.response, 'text'):
                print(f"Respuesta: {e.response.text}")
            raise
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Realiza una peticion PUT
        
        Args:
            endpoint: Endpoint de la API
            data: Datos a actualizar
            
        Returns:
            Respuesta JSON
        """
        if not self.ticket:
            self.get_ticket()
            
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(self.ticket)
        
        try:
            resp = requests.put(url, json.dumps(data), headers=headers)
            resp.raise_for_status()
            return resp.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error en PUT {endpoint}: {e}")
            if hasattr(e.response, 'text'):
                print(f"Respuesta: {e.response.text}")
            raise
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """
        Realiza una peticion DELETE
        
        Args:
            endpoint: Endpoint de la API
            
        Returns:
            Respuesta JSON
        """
        if not self.ticket:
            self.get_ticket()
            
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(self.ticket)
        
        try:
            resp = requests.delete(url, headers=headers)
            resp.raise_for_status()
            return resp.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error en DELETE {endpoint}: {e}")
            if hasattr(e.response, 'text'):
                print(f"Respuesta: {e.response.text}")
            raise


if __name__ == "__main__":
    # Prueba basica del cliente
    client = CiscoAPIClient()
    ticket = client.get_ticket()
    print(f"Ticket de prueba: {ticket}")
