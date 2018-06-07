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

```
soup.title.parent
Out[24]: <head><title>This is a python demo page</title></head>

soup.html.parent
Out[25]: 
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>

soup.parent
```

## 标签树平行遍历

- .next_sibling 返回按照HTML文本顺序的下一个平行节点标签
- .previous_sibling 返回按照html文本顺序的上一个平行节点标签
- .next_siblings 迭代类型，范湖i按照HTML文本顺序的后续所有平行节点标签
- .previous_siblings 迭代类型，返回按照html文本孙旭的谦虚所有平行节点标签

所有的平行遍历必须发生在同一树型节点下。

```
soup.a.next_sibling
Out[27]: ' and '

soup.a.next_sibling.next_sibling
Out[28]: <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>

soup.a.previous_sibling
Out[29]: 'Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n'

soup.a.previous_sibling.previous_sibling

soup.a.parent
Out[31]: 
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
```

## 总结

下行遍历 .content, .children, .descendants
上行遍历 .parent, .parents
平行遍历 .next_sibling,.previous_sibling,.next_siblings,.previous-siblings


