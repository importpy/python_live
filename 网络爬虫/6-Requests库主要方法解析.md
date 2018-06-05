# Requests库主要方法解析

标签： requests

---

requests库的request方法是所有方法的基础方法
```
requests.request(method,url,**kwargs)
```
- method 请求方式，对应GET、PUT、PATCH对- 应的7种方法
- URL 拟获取页面的url链接
- **kwargs 控制访问参数，共13个


----------
## method请求方式
```
r = requests.request('GET',url,**kwargs)
r = requests.request('HEAD',url,**kwargs)
r = requests.request('POST',url,**kwargs)
r = requests.request('GET',url,**kwargs)
r = requests.request('PUT',url,**kwargs)
r = requests.request('PATCH',url,**kwargs)
r = requests.request('delete',url,**kwargs)
r = requests.request('OPTIONS',url,**kwargs) # 向服务器获取一些服务器和客户端能够打交道的参数
```


----------
## **kwargs控制访问参数
- params 字典或字节序列，能够增加到URL中的参数
```
>>> import requests
>>> kv = {'name':'lvxin', 'age':26}
>>> r.url
'http://www.baidu.com/?name=lvxin&age=26'

```



- data:字典、字节序列或文件对象，作为Request的内容
- json json格式的数据，作为内容部分向服务器提交
- headers 字典，定制头，用来模拟浏览器
- cookie 字典或CookieJar，Request中的cookie
- auth 元组，支持HTTP认证功能
- files 字典类型，传输文件
- timeout 设定超时时间
- proxies 字典类型，设定访问代理服务器，可以增加登录认证（有效隐藏原地址信息，有效防止对爬虫的逆追踪）
- allow_redicts True/False，默认为True，重定向开关
- stream 默认为True，获取内容立即下载开关
- verify 认证SSL证书开关
- cert 保存本地SSL证书路径的字段


----------


requests的其他方法例如POST、PUT等6种方法都是request方法的一项，由于常用到某一参数，就会把常用参数作为显示参数放到函数设计里面。所以弄清楚requests的控制参数，就明白其他方法的控制参数。
```
def post(url, data=None, json=None, **kwargs)

def put(url, data=None, **kwargs)
```