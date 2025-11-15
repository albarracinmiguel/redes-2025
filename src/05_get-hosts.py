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

# Obtener hosts
api_url = "http://localhost:58000/api/v1/host"
headers = {
    "X-Auth-Token": serviceTicket,
    "content-type": "application/json"
}

resp = requests.get(api_url, headers=headers)
print("Request status:", resp.status_code)
print()

response_json = resp.json()
hosts = response_json["response"]

# Formatear en tabla
host_list = []
for i, host in enumerate(hosts, 1):
    host_list.append([
        i,
        host.get("hostName", "N/A"),
        host.get("hostIp", "N/A"),
        host.get("hostMac", "N/A"),
        host.get("hostType", "N/A"),
        host.get("connectedInterfaceName", "N/A")
    ])

print(tabulate(host_list, headers=["#", "Hostname", "IP", "MAC", "Type", "Interface"], tablefmt='grid'))
