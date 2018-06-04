# Python高级变量类型列表详解

标签： Python列表

---

## 列表的定义
- list（列表）是Python中使用最频繁的数据类型，在其他语言中通常叫做数组
- 列表是有序的集合
- 定义列表使用[]定义，数据之间使用，分割
```py
name_list = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
```

- 列表的索引从0开始
    - 索引就是数据在列表中的位置编号，索引有可以被称为下标
- 注意：从列表中取值时，如果超出索引范围，程序会产生异常
```
IndexError: list index out of range
```

## 列表的常用操作

### 增加

- 列表名.insert(index, 数据)：在指定位置插入数据（位置前有空元素会补位）
```python
# 往列表name_list 下标为0的地方插入数据
name_list.insert(0,'sasuke')

name_list
Out[3]: ['sasuke', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu']

# 现有的列表下标为0-4，如果我们要在下标是6的地方插入数据，那么会自动被插入到下标为5的地方，也就是插入到最后
name_list.insert(6, 'Tom')

name_list
Out[5]: ['sasuke', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'Tom']
```

- 列表名.append（数据）：在列表的末尾追加数据（最常用的方法）
```python
name_list.append('Python')

name_list
Out[7]: ['sasuke', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'Tom', 'Python']

```

- 列表.extend(Iterable):将可迭代对象中的元素追加到列表
```python
# 有两个列表a 和 b a.extend(b)会将b中的元素追加到列表a中
a = [11, 22, 33]
b = [44, 55, 66]
a.extend(b)

a
Out[11]: [11, 22, 33, 44, 55, 66]

# 有列表c 和字符串d c.extend(d) 会将字符串d中的每一个字符拆开作为元素插入到列表c
c = ['j', 'a', 'v', 'a']
d = 'python'
c.extend(d)

c
Out[15]: ['j', 'a', 'v', 'a', 'p', 'y', 't', 'h', 'o', 'n']
```

- 取值和修改
    - 取值：列表名[index]:根据下标来取值
```python
name_list
Out[16]: ['sasuke', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'Tom', 'Python']

name_list[0]
Out[17]: 'sasuke'

name_list[3]
Out[18]: 'wangwu'
```
- 修改:列表名[index] = 数据：修改指定索引的数据
```python
# 将列表中下标为0的值sasuke修改为num01
name_list[0] = 'num01'

name_list
Out[20]: ['num01', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'Tom', 'Python']
```
- 删除
    - del列表名[index]:删除指定索引的数据
```python
name_list
Out[21]: ['num01', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'Tom', 'Python']
# 删除索引为1的数据
del name_list[1]

name_list
Out[23]: ['num01', 'lisi', 'wangwu', 'zhaoliu', 'Tom', 'Python']
```
- 列表名.pop():删除末尾的数据，返回值：返回被删除的元素
```python
name_list
Out[24]: ['num01', 'lisi', 'wangwu', 'zhaoliu', 'Tom', 'Python']

# 删除最后一个元素Python并将Python返回
name_list.pop()
Out[25]: 'Python'

name_list
Out[26]: ['num01', 'lisi', 'wangwu', 'zhaoliu', 'Tom']
```

- 列表名.pop(index):删除指定索引的数据，并返回被删除的元素
```python
name_list
Out[27]: ['num01', 'lisi', 'wangwu', 'zhaoliu', 'Tom']

# 删除索引为1的数据lisi
name_list.pop(1)
Out[28]: 'lisi'

name_list
Out[29]: ['num01', 'wangwu', 'zhaoliu', 'Tom']
```    
- 列表名.clear():清空整个列表的元素
```python
name_list
Out[30]: ['num01', 'wangwu', 'zhaoliu', 'Tom']

name_list.clear()

name_list
Out[32]: []
```
### 排序
- 列表名.sort():升序排序，从小到大
```python
a = [33, 44, 22, 66, 11]
a.sort()

a
Out[35]: [11, 22, 33, 44, 66]
```
- 列表名.sort(reverse = True):降序排序，从大到小
```python
a = [33, 44, 22, 66, 11]

a.sort(reverse = True)

a
Out[38]: [66, 44, 33, 22, 11]
```

- 列表名.reverse():列表逆序、反转
```python
a = [11, 22, 33, 44, 55]

a.reverse()

a
Out[41]: [55, 44, 33, 22, 11]
```

### 统计相关
- len(列表名)：得到列表的长度
```python
a = [11,22,33,44,55]

len(a)
Out[43]: 5
```
- 列表名.count(数据)：数据在列表中出现的次数
```python
a = [11, 22, 33, 11, 11]

a.count(11)
Out[45]: 3
```
- 列表名.index(数据)：数据在列表中首次出现时的索引，没有查到会报错
```python
a = [11, 22, 33, 44, 22]

a.index(22)
Out[47]: 1
```
- if 数据in列表：判断列表中是否包含某元素
```python
a = [11, 22, 33, 44, 55]

if 33 in a:
    print('ok')
    
```
### 循环遍历
- 使用while循环
```python
a =[11, 22, 33, 44, 55]

i = 0

while i < len(a):
    print(a[i])
    i += 1
    
11
22
33
44
55
```
- 使用for循环：
```python
a = [11, 22, 33, 44, 55]

for i in a:
    print(i)
    
11
22
33
44
55
```