import json

def loadjson(file):
    with open(file,"r") as f:
        jsonld = json.loads(f.read())
        f.close()
        return jsonld