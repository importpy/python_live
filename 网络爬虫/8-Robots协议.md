# Robots协议

标签： requests

---

Robots Exclusion Standard 网络爬虫排除标准

- 作用：网站告知网络爬虫那些页面可以爬取，哪些不行
- 形式：在网站根目录下的robots.txt文件
- 语法：User-agent,Disallow


京东的Robots协议 https://www.jd.com/robots.txt

```
User-agent: * 
Disallow: /?* 
Disallow: /pop/*.html 
Disallow: /pinpai/*.html?* 
User-agent: EtaoSpider 
Disallow: / 
User-agent: HuihuiSpider 
Disallow: / 
User-agent: GwdangSpider 
Disallow: / 
User-agent: WochachaSpider 
Disallow: /
```
*教育部网站没有robots,协议*

## Robots协议使用
网络爬虫自动或人工识别robots.txt文件，再进行内容爬取
约束性：网络爬虫可以不遵守robots.txt协议，但存在法律风险

其实任何爬虫都应遵守协议，比如某些小程序和人类获取相关一致，可以不遵守robots协议，但是要注意获取的资源不能用于商业用途。


