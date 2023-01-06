import os,queue,time
def readfile(file):
    with open(file,"r") as f:
        return f.read()

def wfile(path,st):
    with open(path,"a") as f:
        f.write(st)
        f.close()

def wfileb(path,st):
    with open(path,"ab") as f:
        f.write(st)
        f.close()

def abspath(path = ""):
    return os.path.abspath(path=path)


