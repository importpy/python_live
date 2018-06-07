# Scrapy 爬虫框架进行解析

## 5 + 2 结构

- ENGINE

控制所有模块的数据流
同时根据各个模块之间的事件进行触发

不需要用户修改

- DOWNLOADER

根据请求下载网页
不需要用户修改

- Scheduler

对用户所有请求进行调度管理的模块
不需要用户修改

- Downloader Middleware

目的：实施Engine\Scheduler和Downloader之间进行用户可配置的控制

功能：修改、丢弃、新增请求或响应

用户可以编写配置代码

- Spider

解析Downloader返回的响应Response
产生爬取项scraped item
产生额外的爬取请求Request

- Item Pipeline

流水线来处理Spider产生的爬取项
有一组操作顺序组成，类似流水线，每个操作是一个Item Pipeline类型

可能包括清理，检验查重爬取项中的HTML数据、将数据存储到数据库中
对于从网页中提取出来的信息，需要封装的信息，用户需要怎么做，数据库内，或者清洗

- Spider Middleware

目的：对请求和爬取项再处理
功能：修改、丢弃、新增请求或爬取项

