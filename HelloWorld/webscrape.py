# test api connection status
import http.client

conn = http.client.HTTPSConnection("api.browse.ai")

headers = {'Authorization': "Bearer 2f306880-5e1c-46f7-815e-308948f581a6:cf22efb7-b237-42f1-9027-9df15a8581f6"}

conn.request("GET", "/v2/status", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
