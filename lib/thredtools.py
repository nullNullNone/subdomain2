import threading

def runthread(target = "",args = dict()):
    t = threading.Thread(target=target,kwargs=(args))
    t.start()