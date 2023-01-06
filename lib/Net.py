import socket
import dns
import dns.resolver
def Dns_plain(domain):
    try:
        res = socket.gethostbyname(domain)
        return tuple([res])
    except Exception as e:
        raise Exception(str(e)+":"+domain)

def Dns_Query_addr(domain,serverlist = ["114.114.114.114"]):
    A = dns.resolver.resolve(domain)
    A.nameservers = serverlist
    A.timeout = 15
    A.lifetime = 15
    res = set()
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                res.add(j.address)
    return tuple(list(res))