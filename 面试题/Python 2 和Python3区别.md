# Python 2 和Python3区别

标签（空格分隔）： 面试题

---

python2 和 python3 的区别

- 性能：py3.0 运行pystone benchmark的速度比py2.5慢30%。Guido认为py3.0有极大的优化空间，在字符串和整型操作上可以取得很好的优化效果

- 编码：py3.x源码文件默认使用utf-8编码

- 语法：


    - 去除了<>,全部改用!=
    - 去除'',全部改用repr()
    - 关键词加入as 和 with,还有True,False,None
    - 整形除法返回浮点数，要得到整型结果，请使用//
    - 加入nonlocal语句，使用noclocal x可以直接指派外围（非全局）变量
    - 去除print语句，加入print()函数实现相同的功能，同样的还有exec语句，已经改为exec()函数
    - 改变顺序操作符的行为，例如x<y,当x和y类型不匹配时抛出TypeError而不是返回随即的bool值
    - 输入函数改变了，删除了raw_input,用input代替
    - 去除元组参数解包，不能def(a,(b,c)):pass这样定义函数了
    - 新式的8进制字变量，相应地修改了oct()函数
    - 增加了2进制字面量和bin()函数
    - 扩展的可迭代解包，在py3.0里，啊，吧，*rest= seq 和*rest, a = 都是合法的，只要求两点：rest是list对象和seq是可迭代的
    - 新的super(),可以不再给super()传参数
    - 新的metaclass语法
    - 支持class decorator ，用法与函数decorator一样



- 字符串

    - 现在字符串只有str一种类型，但它跟2.x版本的unicode几乎一样
    - 关于字符串，参阅数据类型


- 数据类型;

    - py3.0 去除long类型，现在只有一种整型int,但它的行为就像py2.0版本的long
    - 新增了bytes类型，对应于2.x版本的八位串，定义一个bytes字面量的方法如下：
    	str对象和bytes对象可以使用.encode()(str -> bytes) or .decode() (bytes -> str)方法相互转化
    - dict的.keys() .items 和.values()方法返回迭代器，而之前的iterkeys()等函数都被废弃。同时去掉的还有dict.has_key(),用in替代它吧



- 面向对象：
    - 引入抽象基类(Abstract Base Classes, ABCs)
    - 容器类和迭代器类被ABCs化
    - 迭代器的next()方法改名为__next__(),并增加内置函数next(),用以调用迭代器的__next__()方法
    - 增加了@abstractmethod 和@abstractproperty两个decorator,编写抽象方法（属性）更加方便



- 异常
    - 所以异常都从BaseException继承，并删除了StrdardError
    - 去除了异常类的序列行为和.message属性
    - 用raise Exception(args)代替 raise Exception，args语法
    - 捕获异常的语法改变，引入了as关键字用来标识异常实例
    - 异常链，因为__context__在3.0a1版本中没有实现



- 模块变动
    - 移除了cPickle模块，可以使用pickle模块代替，最终我们将会有一个透明高效的模块
    - 移除了imageop模块
    - 移除了audiodev,Basetion,bsddb185,exceptions,linuxaudiodev,md5,MimeWriter,mimify,popen2,rexec,sets,sha,stringold,strop,sunaudiodev,timing和xmllib模块
    - 移除了new模块
    - os.tmpnam()和os.tmpfile()函数被移动到tmpfile模块下
    - tokenize模块现在使用bytes工作。主要的入口点不再是generate_tokens,而是tokenize.tokenize()



- 其他

    - xrange() 改名为range(),更像使用range()获得一个list，必须显式调用
    - bytes 对象不能hash,也不支持b.lower()、b.strip()和bsplit()方法，但对于后者可以使用b.strip(b' \n\t\r \f')和b.split(b'')来达到相同的目的
    - zip()、map()和filter()都返回迭代器。而apply()、callable()、coerce()、execfile()、reduce()和reload()函数都被去除了现在可以使用hasattr()来替换callable()、hasattr()的语法如：hasattr(string,'__name__')
    - string.letters 和相关的.lowercase 和.uppercase被去除，清改用string.ascii_letters等
    - 如果x < y 的不能比较，抛出TypeError异常，2.x版本是返回伪随机布尔值的
    - __getslice__系列成员被废弃，a[i:j]根据上下文转换为a.__getitem__(slice(I,j))或__setitem__和__delitem__调用
    - file类被废弃





