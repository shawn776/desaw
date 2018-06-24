import json,os
data = "config/status.json"
with open(data) as e:
    jso = json.loads(e.read())
print("Version: "+jso['version'])