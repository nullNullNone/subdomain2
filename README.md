# subdomain2
# subdomain scanner
子域名扫描器

### targs.txt 目标
```
{0}.{1}.edu.cn
{0}.{1}.{2}.edu.cn
```

### res 存放结果
### dic 存放字典

### gen.json 自动生成配置
```json
{
  "rd":{
    "1": 20,
    "2": 600,
    "3": 6000
  },
  "rc": {"600000":[1,2,3,4,5,6]}
}
```
rd "位数":"次数"
rc "次数":[位数,位数......]

```bash
pip install dnspython
```
21.5.26
更新修复大量bug
加入dns服务器选择 及性能选项

### perfom.json
```python
{"th": 500,
  "servlist": ["114.114.114.114","114.114.115.115","223.5.5.5","180.76.76.76","119.29.29.29","218.30.118.6"],
  "mode": 1
}
```
ps 建议使用自己的字典以提高效率 虽然字典会自动生成
ps mode 爆破模式 1.dnspuython 2.socket 没有3
th 线程数 默认500

