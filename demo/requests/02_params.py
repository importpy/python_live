# coding=utf-8
import requests
headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
# url = "https://www.baidu.com/s?wd={}".format()
# params = {"wd":"python"}
params= dict(wd="python")
url_temp = "https://www.baidu.com/s?"

r = requests.get(url_temp,params=params,headers=headers)
print(r.status_code)
print(r.request.url)