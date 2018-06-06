# 基于bs4库的HTML遍历方法

## HTML基本格式

HTML结构化设置，会发现demo是具有树型结构的文本信息。

- 沿着树的下行遍历，根节点到叶子节点
- 上行遍历
- 平行遍历方式

### 标签树的下行遍历

- ```.contents``` 
子节点的列表，将tag所有儿子节点存入列表

- ```.children```
子节点的迭代类型，与contents类似，用于循环遍历子节点

- ```.descendants```
子孙节点的迭代类型，包括所有子孙节点，用于循环遍历

```
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.dead
>>> soup.head
<head><title>This is a python demo page</title></head>
>>> soup.head.contents
[<title>This is a python demo page</title>]
>>> soup.body.sontents
>>>
>>> soup.body.contents
['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to
professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\
n']
>>> len(soup.body.contents)
5
>>> soup.body.contents[1]
<p class="title"><b>The demo python introduces several python courses.</b></p>
>>>

```

## 标签树的上行遍历

- ```.parent```
节点的父亲标签

- ```.parents```
节点先辈标签的迭代类型，用于循环遍历先辈节点

