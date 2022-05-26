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
更新修复大量bug
