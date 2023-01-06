
def Md5(Str = ""):
    import hashlib
    return hashlib.md5(Str.encode('utf8')).hexdigest()

def base64en(Str):
    import base64
    return base64.b64encode(Str.encode())