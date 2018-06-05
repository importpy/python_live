# requests

标签： 爬虫

---

- requests库 简单简洁，一行代码获得相关资源

- 安装requests库,测试
```python
import requests

r = requests.get('http://www.baidu.com')
r.status_code
# 响应码200

r.encoding = 'utf-8'
r.text

```

## requests 库的七个主要方法
- requests.request() 构造一个请求，支持以下各个方法的基础方法
- requests.get() 获取HTML网页的主要方法，对应HTTP的GET
- requests.head()  获取网页头信息的方法
- requests.post() 获取HTML网页提交POST请求的方法
- requests.put() 向HTML网页提交PUT请求的方法
- requests.patch() 向HTML网页提交局部修改请求
- requests.delete() 向HTML网页提交删除请求







