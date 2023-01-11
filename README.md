# subdomain2 

subdomain scanner

### targs.txt 

targetfile

```
{0}.google.com
{0}.{1}.google.com
```

### res 

output result

### dic 

dictionaries for scan subdomain

### perfom.json

settings for scanner

```python
{
  "threadNum": 500,
  "servlist": ["114.114.114.114","114.114.115.115","223.5.5.5","180.76.76.76","119.29.29.29","218.30.118.6"],
  "mode": 1,
  "dict": "./dict/"
}
```
mode  1.dnspuython 2.socket 

servlist dnsserver list

threadNum number of threads 500 default

dict dir for dics

# UPDATE
21.5.26
bug fix
23.1.5
use threadpool to reduce menmory cost
delete function genaration dics 

# install

```bash
pip install dnspython
```

# PICS
![image](https://user-images.githubusercontent.com/97675486/211027317-3e2d7179-6983-4bd8-bcf2-ab7254778016.png)

# plan
addin 
ip138 
ping
ping in multi-place
whois
collection site of the user 

