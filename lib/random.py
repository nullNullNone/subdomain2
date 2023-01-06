import random,time

class ramdd:

    All = []
    Cm = []
    num = [0,1,2,3,4,5,6,7,8,9]
    def __init__(self):
        self.Alllist()
        self.Mklist()

    def Mklist(self):
        A = 65
        Z = A + 26
        a = 97
        z = a + 26
        Li = []
        for x in range(A, Z):
            Li.append(chr(x))
        for xx in range(a, z):
            Li.append(chr(xx))
        for xxx in range(1,10):
            Li.append(str(xxx))
        self.Cm = Li
        return Li

    def Alllist(self):
        Ali = []
        for x in range(128):
            Ali.append(chr(x))
        self.All = Ali
        return Ali

    def ramdschar(self,bit):
        res = ""
        limi = len(self.Cm)-1
        for x in range(bit):
            step = int(random.random()*(time.time())%600*100)
            res += self.Cm[step%limi]
        return res

    def randnum(self,bit,seet):
        res = ""
        limi = len(seet)
        for x in range(bit):
            step = int(random.randint(0,65535))
            res += str(seet[step % limi])
        return res

    def randnumlist(self,bit,rund):
        res = set()
        st = int("1"+"0"*(bit-1))
        ed = int("9"*bit)
        for x in range(rund):
            res.add(random.randint(st,ed))
        return res