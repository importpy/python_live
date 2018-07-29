# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:40:27 2018

@author: hq
"""

# 静态文件
# 只要在你的包中或模块傍边创建一个名为static的文件夹，在应用中使用/static即可访问
# 给静态文件生成url，使用特殊的static端点名
# url_for('static', filename = 'style.css')


# 模板渲染
# 在python里生成html十分无趣，而且相当繁琐，需要自行对html做转义来保证应用安全
# flask自动配置了Jinja2模板引擎
# 可以使用render_template()方法来渲染模板
# 将模板名和你想作为关键字的参数传入模板的变量
from flask import Flask
from flask import render_template

app = flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Flask会在templates文件夹里寻找模板
# 如果你的应用是个模块，这个文件夹在模块的旁边，如果他是个包，那么这个文件夹在你的包里面
# 对于模板，可以使用Jinja2模板的全部能力
'''
<!doctype html>
<title>hello from Flask</title>
{% if name %}
    <h1>hello {{ name }}</h1>
{% else %}
    <h1>hello world</h1>
{% endif %}

'''
# 在模板里，也可以访问request\session和g对象，以及get_flasked_messages()函数
# 使用继承模板会相当有用
# 自定义转义默认是开启的，所以如果name包含html，它将会被自动转义
# 如果你能新人一个变量，并且知道他是安全的，可以用Markup类或|safe过滤器在末班中标记他是安全地。
'''
Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Out[10]: Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

Markup.escape('<blink>hacker</blink>')
Out[11]: Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

Markup('<em>Marked up</em> &raquo;HTML').striptags()
Out[12]: 'Marked up »HTML'
'''

# 访问请求数据
# 局部上下文
# 做单元测试，你会发现依赖于一个请求对象的代码会突然中断，因为不会有请求对象。
# 解决方案是自己创建一个请求对象，并且把它绑定到上下文
# 使用 test_request_context()上下文管理器，结合with声明，绑定一个测试请求来进行交互

'''
with app.test_request_content('/hello',method='POST'):
    # now you can do something with request until 
    # the end of the with block, suck as basic assertions
    assert request.path == '/hello'
    assert request.method == 'POST'
''' 

# 另一种可能是传递整个WSGI环境给request_context()方法
'''
with app.request_context(environ):
    assert request.method == 'POST'
'''   

# 请求对象
# 当请求方式通过method属性访问，通过form属性来访问表单数据
# post或put请求提交的数据
@app.route('/login', methods = ['POST', 'GRT'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
        # the code below is executed id the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)

# 文件上传
# 不要忘记html表单中设置enctype = 'mutipart/form-data'属性，否则你的浏览器将根本不提交文件
@app.route('/upload', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        # f.save('/var/www/uploads/' + secure_filename(f.filename))
        # 如果你想要使用客户端的文件名来在服务器上存文件，把它传递给werkzeug提供的secure_filename()函数

# cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookie[key] to not get a 
    # keyerror if the cookir is missing
    
# 存储cookie
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username','the username')
    return resp

# 重定向和错误
    

if __name__ == '__main__':
    app.debug = True
    app.run()


    