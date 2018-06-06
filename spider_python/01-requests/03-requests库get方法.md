# requests库get方法

标签： requests

---
# requests的get方法
r = requests.get(url)

- 构造一个向服务器请求资源的Requests对象
- 返回一个包含服务契资源的Response对象


```
requests.get(url, params = None, **kwargs)
# url:拟获取页面的url链接
# params:在url中的额外参数，字典或字节流格式可选
# **kwargs:控制访问参数
```

查看request.get的源代码，可看到get方法是使用request方法来封装
```
def get(url, params=None, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)
    # 事实上可以认为requests库只有一个方法就是request方法
```
# Response对象 
Response对象包含爬虫返回的全部内容
```
>>> import requests
>>> r = requests.get('http://www.baidu.com')
>>> print(r.status_code)
200
>>> type(r)
<class 'requests.models.Response'>
>>> r.headers
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 05 Jun 2018 15:38:25 GMT',
'Last-Modified': 'Mon, 23 Jan 2017 13:27:36 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
>>>

```
Response对象包含了返回的所有信息，同时也包含我们向服务器请求的Request信息。

## Response常用属性
- ```r.status_code``` HTTP请求的返回状态，200表示连接成功，404表示失败
- ```r.text```  HTTP响应内容的字符串形式，即url对应的页面内容
- ```r.encoding```  从HTTP header中猜测的响应内容编码方式
- ```r.apparent_encoding``` 从内容分析出的响应内容编码方式（备选编码方式）
- ```r.content``` HTTP响应内容的二进制形式

## 使用get方法基本流程

1. ```r.status_code``` 检查Response对象的状态
2. 如果是200，可以用```r.text```,```r.encoding```,```r.apparent_encoding```,```r.content```去解析返回的内容
3. 如果返回是404或其他，说明这次访问由于某些原因出错，产生异常

## 理解Response编码
为了有效地进行网页可读，所以我们需要编码的概念

- ```r.encoding``` 是从HTTP header中的charset字段获得的，但是并不是所有的服务器对它的相关编码都是有相关要求，如果header中不存在charset,则认为编码为ISO-8859-1,但这样的编码并不能解析中文，所以requests库提供了默认的备选编码
- ```r.apparent_encoding``` 编码根据HTTP内容部分，而不是头部分去分析内容出现的可能编码方式，比encoding会更准确
```
>>> import requests
>>> r = requests.get('http://www.baidu.com')
>>> r.status_code
200
>>> r.encoding
'ISO-8859-1'
>>> r.apparent_encoding
'utf-8'
>>> r.text
'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always 

··· 

href=http://home.baidu.com>å\x85³äº\x8eç\x99¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç
\x94¨ç\x99¾åº¦å\x89\x8då¿\x85è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æ\x84\x8fè§\x81å\x8f\x8dé¦\x88</a>&nbsp;äº¬ICPè¯\x81030173å\x8f·&nbsp; <img src=//www.baidu.com/img/gs.gif> </
p> </div> </div> </div> </body> </html>\r\n'
（很多都是乱码）
>>> r.encoding = 'utf-8'
>>> r.text
'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always 

··· 

href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.b
aidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'
>>>
```
