from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED
from lib.Net import Dns_Query_addr,Dns_plain
from lib.cfgtool import loadjson
from lib.sysdict import dictionary
from lib.clicklist import defclock
from lib.stringt import formatfill
from lib.array import limit,listmap
from lib.file import abspath,wfile
from lib.thredtools import runthread
import time
import queue
import json
import os

ip_scaned_queue = queue.Queue()
lid = []
cc = 0
Qstop = False
ed = set()
########################################
# load CFG 
jls = loadjson("perfom.json")
servlist = jls["servlist"]
burpmode = jls["mode"]
dictpath = abspath(jls["dict"])
threadNum = jls["threadNum"]
########################################

#######################################
# dic combine
dicload = list(dictionary().loaddic(dictpath))
size_dicload = len(list(dicload))
#######################################

#######################################
# scan mode
def scanmod(mod,domain):
    global servlist
    if mod == 1:
        return Dns_Query_addr(domain=domain,serverlist=servlist)
    elif mod == 2:
        return Dns_plain(domain=domain)
#######################################

#######################################
# net
def scan(tempdomain,burpmode):
    global cc,lid
    try:
        temp = scanmod(domain=tempdomain,mod=burpmode)
        res = json.dumps({"domain":tempdomain,"iplist":temp})
        print(res)
        ip_scaned_queue.put(res)
    finally:
        lid.append(0)
        cc+=1
#######################################

#######################################
#file
def res_write(ip_scaned_queue = queue.Queue(),path = ""):
    while True:
        if ip_scaned_queue.empty() == False:
            wfile(path, ip_scaned_queue.get()+"\n")
        else:
            if Qstop == True and ip_scaned_queue.empty() == True:
                break
            time.sleep(1)
#######################################

#######################################
#scan
path = ".{}res{}".format(os.sep,os.sep)
path += "_"+str(time.time())+"_.txt"
runthread(target=res_write,args={"path":path+".tmp","ip_scaned_queue":ip_scaned_queue})
f = open("./targs.txt","r",encoding="utf-8")
count = 0
for x in f.readlines():
    x = x.strip()
    bit = x.count("{")
    clock = defclock(bit=bit,le=size_dicload)
    rtt = ThreadPoolExecutor(max_workers=threadNum)
    for xc in range(clock.forl):
        tempdomain = formatfill(x,listmap(clock.tick(),dicload))
        if tempdomain in ed:
            continue
        ed.add(tempdomain)
        rtt.submit(scan,tempdomain=tempdomain,burpmode=burpmode)
        if count >= threadNum:
            while True:
                if len(lid) >= threadNum:
                    lid.clear()
                    count = 0
                    ed.clear()
                    break
                time.sleep(1)
                print("\r[{}]".format(len(lid)),end="")
        count+=1
    while True:
        if cc == clock.forl:
            cc = 0
            rtt.shutdown(True)
            time.sleep(10)
            break
f.close()
Qstop = True
#######################################

# scan("www.baidu.com",burpmode=2)
# print(lid)
# print(cc)