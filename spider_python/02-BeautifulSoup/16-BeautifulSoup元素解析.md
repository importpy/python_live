# BeautifulSoup元素解析

## BeautifulSoup理解

解析、遍历、维护HTML标签树的功能库，只要提供标签类型，都可以做很好的解析

- 标签Tag <p>
    - 名称 Name
    - 属性 Attributes

BeautifulSoup类可以理解为HTML标签树的类，形成变量，对变量的处理相当于对HTML处理

## BeautifulSoup库解析器

- bs4的HTML解析器
不需安装就能使用
- lxml的HTML解析器 
安装lxml库
- lxml的XML解析器
安装lxml库
- html5lib的解析器
安装html5lib库

无论哪种解析器都是可以有效解析HTML和XML文档，我们主要使用HTML解析器，如果处理XML文档，或者获得更快的性能，或者更多的信息，可以使用其他的解释器。

## BeautifulSoup类基本元素

- Tag 

标签，最基本的信息组织单元，分别用```<></>```标明开头和结尾

- Name
标签的名字，p标签，```<tag>.name```

- Attributes
标签的属性，字典形式组织 ```<tag>.attrs```

- Navigablestring 
标签内字符串 ```<tag>.string```

- Comment
标签内字符串的注释部分，一种特殊的注释类型

```
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.title
<title>This is a python demo page</title>
>>> soup.a
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
>>> soup.a.parent.name
'p'
>>> soup.p.parent.name
'body'
>>> soup.a.name
'a'
>>> soup.a.parent.name
'p'
>>> soup.p.parent.name
'body'
>>> tag = soup.a
>>> tag.attrs
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
>>> tag.attrs['class']
['py1']
>>> tag.attrs['href']
'http://www.icourse163.org/course/BIT-268001'
>>> type(tag.attrs)
<class 'dict'>
>>> type(tag)
<class 'bs4.element.Tag'>
>>> soup.a.string
'Basic Python'

>>> type(soup.p)
<class 'bs4.element.Tag'>
>>> type(soup.p.string)
<class 'bs4.element.NavigableString'>
>>> soup
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>
>>>

```