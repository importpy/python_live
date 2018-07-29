# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 14:08:59 2018

@author: hq
"""

from flask import Flask
# 导入Flask类，这个实例是我们WSGI应用，  
app = Flask(__name__)
# 我们创建该实例，第一个参数是应用模块或者包的名称
# 如果使用单一的模块，应该使用__name__
# 取决于作为单独因雇佣启动或者模块导入，他的名称将会不同（'__main__'相对实际的导入名称


@app.route('/')
# 使用route装饰器告诉Flask什么样的URL应该触发我们的函数
# 这个函数的名字也作为特定的函数生成URL，并返回我们想要显示在用户浏览器中的信息
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    # 如果发生错误，会调用调试器
    app.run()
    
# 最后我们用run()函数来让应用运行在本地服务器上，其中main确保服务器只会在改脚本被python结束期直接执行的时候才会运行，而不是作为模块导入
# run函数方法使你的服务器宫口可用
    # app.run(host='0.0.0.0')
    