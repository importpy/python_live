# coding=utf-8
import requests

r = requests.get("https://www.baidu.com/img/bd_logo1.png")

with open("baidu.png","wb") as f:
    f.write(r.content)