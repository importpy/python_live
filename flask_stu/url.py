# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:25:52 2018

@author: hq
"""

# 路由

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'hello world'


# 添加变量字段
# 这些字段标记为<variable_name>,这个部分将作为命名参数传递到函数
# 可以用<converter:variable_name制定一个可选的转换器>
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the fiven id, the id is an integer
    return 'Post %d' % post_id


# 重定向行为
# Flask的url规则基于werkzeug的路由模块，基于apache以及更早的http服务器规定的先例
# 保证优雅且唯一的url
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
"""
虽然看着很相似，但他们几位斜线的使用在URL定义中不同，第一种情况中，规范的url指向projects
尾端有一个斜线。这种感觉很像在文件系统中的文件夹，访问一个结尾不带斜线的url会被flask重定
向到带斜线的规范url中去。

第二种情况的url结尾不带斜线，类似unix-like系统下的文件路径名。访问结尾带斜线的url会产生一个
404错误。

当用户访问页面时忘记结尾斜线，这个行为允许关联的url继续工作，并且与apache和其他的服务器的行
为一致，另外，url会保持唯一，有助于避免搜索引擎索引用一个页面两次
"""

# 构建url
# 使用url_for()来给一个特定函数构造url,接收一个函数名和一些关键字参数，每个对应url
# 规则变量的部分，未知变量部分会添加打url末尾作为查询参数

# 为什么想要构建url
# 1.更具描述性，允许一次性修改url，而不是到处找url
# 2.url构建会显示的处理特殊字段和unicode数据的转义，所以不需要亲自处理
# 3.如果你的应用部位与url的跟路径，url_for会为你妥善的处理


# HTTP方法
# 默认情况下，路由只回应GET请求，但是通过给route()装饰器提供methods参数可以更改这个行为
@app.route('login',methods=['GRT', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
        
def do_the_login():
    pass

def show_the_login_form():
    pass

# Http常用方法
    # GET获取页面上的信息发给我
    # HEAD 获取页面信息，支队消息头感兴趣，不传递实际内容
    # POST 想在url上发布新信息，并且服务器必须确保数据已存储且只存储一次。
    # PUT 类似POST但是服务器可能触发了存储多次过程，多次覆盖掉旧值。
    # 考虑到传输可能丢失，在这种情况下浏览器和服务器之间的系统可能安全地第二次接收请求而不破坏其他东西
    # delete删除给定位置的信息
    # options 给客户端提供一个快速途径来弄清这个url支持哪些http方法
     

if __name__ == '__main__':
    app.debug = True
    app.run()
    
    
    
