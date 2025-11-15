import json
import requests
from tabulate import tabulate

# Obtener ticket de autenticación
ticket_url = "http://localhost:58000/api/v1/ticket"
headers = {
    "content-type": "application/json"
}
body_json = {
    "username": "cisco",
    "password": "cisco123!"
}

resp = requests.post(ticket_url, json.dumps(body_json), headers=headers)
print("Ticket request status:", resp.status_code)
response_json = resp.json()
serviceTicket = response_json["response"]["serviceTicket"]
print("Service ticket:", serviceTicket)
print()

# ID del dispositivo a eliminar (modificar según necesidad)
device_id = "device-uuid-here"

# Eliminar dispositivo de red por ID
api_url = f"http://localhost:58000/api/v1/network-device/{device_id}"
headers = {
    "X-Auth-Token": serviceTicket,
    "content-type": "application/json"
}

resp = requests.delete(api_url, headers=headers)
print("Delete device request status:", resp.status_code)
print()

response_json = resp.json()

# Formatear respuesta en tabla
if "response" in response_json:
    result_data = [[
        "Task ID", response_json["response"].get("taskId", "N/A")
    ], [
        "URL", response_json["response"].get("url", "N/A")
    ]]
    print(tabulate(result_data, headers=["Field", "Value"], tablefmt='grid'))
else:
    print("Response:", json.dumps(response_json, indent=2))
