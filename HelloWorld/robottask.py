import http.client

conn = http.client.HTTPSConnection("api.browse.ai")

headers = {'Authorization': "Bearer 2f306880-5e1c-46f7-815e-308948f581a6:cf22efb7-b237-42f1-9027-9df15a8581f6"}

conn.request(
    "GET", "/v2/robots/507fff9e-ec76-4c64-a18d-2af03155fbf8/tasks?page=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
