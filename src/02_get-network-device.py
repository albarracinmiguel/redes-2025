import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": "NC-146-f6b5ae32242c40ada0a5-nbi"}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
## print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    ## print(networkDevice)
    hostname = networkDevice.get("hostname", "N/A")
    platformId = networkDevice.get("platformId", "N/A")
    managementIpAddress = networkDevice.get("managementIpAddress", "N/A")
    print(hostname, "\t", platformId, "\t", managementIpAddress)
