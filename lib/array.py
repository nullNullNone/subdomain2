
def limit(obj,inp):
    return inp%len(obj)

def file2li(f,en = "utf8"):
    sett = set()
    print(f)
    ff = open(f.strip(),"r",encoding=en)
    for x in ff.readlines():
        if x.strip() == "":
            continue
        sett.add(x.strip())
    ff.close()
    return sett    

def li2str(s = [],sep = ",",pos = True):
    res = ""
    for x in s:
        if not pos:
            res += x + sep
        if pos:
            res += sep + x
    res+="\n"
    return res

def tu2set(s = tuple(),sets = set()):
    for x in s:
        sets.add(x)
    return sets

def listmap(lis1 = [],lis2 = []):
    res = []
    for x in range(len(lis1)):
        res.append(lis2[lis1[x]])
    return res

# print(listmap([1,2,3,4],[333,4,3,4,5,6,7]))
    