# requests库的主要方法

标签： requests

---

## Requests库的七个主要方法

| 方法       | 说明  |
| ------------- |:-------------:| 
| request.request()    | 构造一个请求，支撑以下个方法的基础方法 | 
| requests.get()      | 获取HTML网页的主要方法，对应于HTML的GET| 
| requests.head()| 获取HTML网页头信息的方法，对应于HTTP的HEAD     | 
|requests.post() | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
|requests.put() | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
|requests.put()| 向HTML网页提交PUT请求的方法，对应于HTTP的PUT |
|requests.patch()|向HTML网页提交局部修改请求，对应于HTTP的PATCH|
|requests.delete()| 向HTML网页提交删除请求，对应于HTTP的Dele|


----------


## HTTP协议
Hypertext Transfer Protocol（超文本传输协议），基于“请求与响应”模式的、无状态的应用层协议。

无状态指的是第一次请求和第二次请求之间并没有相关的关联。

HTTP协议一般采用URL作为网络的标识，URL格式 ```http://host[:post][path]```,host表示合法的Internet主机域名或IP地址，port表示端口号，缺省的端口号为80，path表示请求资源的内部路径。

URL是通过HTTP协议存取资源的Internet路径，URL对应一个数据资源。


----------


## HTTP协议对资源的操作方法

- GET 请求获取URL位置的资源
- HEAD 请求获取URL位置资源的响应消息报告，即获取该资源头部信息
- POST 请求向URL位置的资源后附加新的数据
- PUT 请求向URL位置存储一个资源，覆盖原URL位置资源
- PATCH 请求局部更新URL位置的资源，即改变该处资源的部分内容
- DELETE 请求删除URL位置存储的资源

可以把互联网称为云端，云端上的所有资源使用URL进行描述或者标识，获取资源用GET、HEAD方法，自己的资源放到URL对应位置上使用PUT、POST、PATCH方法，删除URL现有资源用DELETE方法。

在HTTP协议中，网络通道和服务器都是黑盒子，它能看到的就是URL链接，以及对URL链接的相关操作。


----------


## PATCH与PUT区别


*假设URL位置上有一组数据UserInfo,包括UserId，UserName等20个字段。需求：用户只改变UserName，其它不变*

- 采用PATCH，仅向URL提交UserName的局部更新请求
- 采用PUT，必须将所有20个字段一并提交到URL，未提交字段被删除

*PATCH最大好处是节省网络带宽*


----------


## head方法
可以用很少的网络流量获取网络资源的概要信息
```
>>> import requests
>>> r = requests.head('http://www.baidu.com')
>>> r.headers
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 05 Jun 2018 17:38:23 GMT','Last-Modified': 'Mon, 13 Jun 2016 02:50:08 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18'}
>>> r.text
''
>>>
```


----------
## post方法
可以提交表单等资源，提交键值对会默认存放在form字段下，提交字符串会默认存放在data字段下。
```
>>> s = {'name' :'lvxin', 'age' : 26}
>>> requests.post('http://www.baidu.com',data = s)
<Response [302]>
>>> r = requests.post('http://www.baidu.com',data = s)

>>> r.text
```