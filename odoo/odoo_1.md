# 开启关闭odoo服务

Odoo使用客户端/服务器架构，其中客户端是通过RPC访问Odoo服务器的web浏览器。

业务逻辑和扩展通常在服务器端执行，尽管支持客户端特性(例如，交互式地图等新的数据表示)可以添加到客户端。

要启动服务器，只需在shell中调用命令odoo-bin，并在必要时向文件添加完整路径:

```
odoo-bin

```
通过在终端上按下两次Ctrl-C或终止相应的操作系统进程，可以停止服务器。

# 建立一个Odoo模块

服务器和客户端扩展都打包为模块，可选地加载到数据库中。

Odoo模块可以将全新的业务逻辑添加到Odoo系统中，或者改变和扩展现有的业务逻辑:可以创建一个模块，将您的国家的会计规则添加到Odoo的通用会计支持中，而下一个模块则为公共汽车机群的实时可视化添加了支持。

Odoo中的一切都以模块开始和结束。

## 模块的组成

一个Odoo模块可以包含很多元素:

- 业务对象：声明为Python类的这些资源由Odoo根据它们的配置自动持久化

- 数据文件：声明元数据(视图或工作流)、配置数据(模块参数化)、演示数据等的XML或CSV文件

- 网络控制器：处理来自web浏览器的请求

- 静态web数据：web界面或网站使用的图像、CSS或javascript文件

## 模块结构
每个模块都是模块目录中的目录。模块目录通过使用—addons-path选项指定。

> 提示：还可以使用配置文件设置大多数命令行选项

Odoo模块由它的manifest声明。请参阅关于它的清单文档。

模块也是带有__init__的Python包。py文件，包含模块中各种Python文件的导入指令。

例如，如果模块只有一个mymodule。__init__ py文件。py可能包含:

```python
from . import mymodule
```

Odoo提供了一种机制来帮助建立一个新的模块，Odoo -bin有一个子命令脚手架来创建一个空模块:
```
odoo-bin scaffold <module name> <where to put it>
```

该命令为模块创建子目录，并自动为模块创建一组标准文件。它们大多只包含注释代码或XML。本教程将解释这些文件的大部分用法。

> 练习
创建模块

使用上面的命令行创建一个空模块Open Academy，并在Odoo中安装它。

1.调用odoo-bin脚手架附加器命令。

2.使清单文件适应您的模块。

3.别为其他文件操心了。

```python

- openacademy/__manifest__.py
# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
```

```
- openacademy/__init__.py

# -*- coding: utf-8 -*-
from . import controllers
from . import models

```

```python
- openacademy/controllers.py


# -*- coding: utf-8 -*-
from odoo import http

# class Openacademy(http.Controller):
#     @http.route('/openacademy/openacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy/openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy.listing', {
#             'root': '/openacademy/openacademy',
#             'objects': http.request.env['openacademy.openacademy'].search([]),
#         })

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })
```

```python
- openacademy/demo.xml

# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
```

```python
- openacademy/security/ir.model.access.csv

id,name,model_id/id,group_id/id,perm_read,perm_write,perm_create,perm_unlink
access_openacademy_openacademy,openacademy.openacademy,model_openacademy_openacademy,,1,0,0,0

```

```html
- openacademy/templates.xml

<odoo>
    <data>
        <!-- <template id="listing"> -->
        <!--   <ul> -->
        <!--     <li t-foreach="objects" t-as="object"> -->
        <!--       <a t-attf-href="{{ root }}/objects/{{ object.id }}"> -->
        <!--         <t t-esc="object.display_name"/> -->
        <!--       </a> -->
        <!--     </li> -->
        <!--   </ul> -->
        <!-- </template> -->
        <!-- <template id="object"> -->
        <!--   <h1><t t-esc="object.display_name"/></h1> -->
        <!--   <dl> -->
        <!--     <t t-foreach="object._fields" t-as="field"> -->
        <!--       <dt><t t-esc="field"/></dt> -->
        <!--       <dd><t t-esc="object[field]"/></dd> -->
        <!--     </t> -->
        <!--   </dl> -->
        <!-- </template> -->
    </data>
</odoo>
```

## 对象关系映射ORM

Odoo的一个关键组成部分是ORM层。该层避免了手工编写大部分SQL，并提供了可扩展性和安全性服务2。

业务对象被声明为Python类，扩展模型将它们集成到自动持久化系统中。

模型可以通过在其定义上设置许多属性来配置。最重要的属性是_name，它是必需的，定义了Odoo系统中模型的名称。以下是对模型的最低完整定义:

```python
from odoo import models
class MinimalModel(models.Model):
    _name = 'test.model'

```

## 模型字段

字段用于定义模型可以存储的内容和位置。字段定义为模型类的属性:

```python
from odoo import models, fields

class LessMinimalModel(models.Model):
    _name = 'test.model2'

    name = fields.Char()

```

### 共同属性

与模型本身很相似，它的字段可以通过将配置属性作为参数传递来进行配置:

```python
name = field.Char(required=True)
```
所有字段都有一些属性，以下是最常见的属性:

- string(unicode，default:field's name)
    - UI中字段的标签(用户可见)。

- required (bool, default: False)
    - 如果为真，则该字段不能为空，它必须具有一个默认值，或者在创建记录时总是被赋予一个值。

- help (unicode, default: '')
    - Long-form，为UI中的用户提供帮助工具提示。

- index (bool, default: False)
    - 请求Odoo在列上创建一个数据库索引

### 简单的字段

There are two broad categories of fields: "simple" fields which are atomic values stored directly in the model's table and "relational" fields linking records (of the same model or of different models).

简单字段的例子是布尔，日期，Char。

### 保留字段

Odoo在所有的model中都创建了一些字段。这些字段由系统管理，不应该被写入。如有用或有需要，可阅读:


- id(id) 记录在其模型中的唯一标识符。

- create_date(Datetime) 记录的创建日期。

- create_uid(Many2one) 创建记录的用户。

- write_date(Datetime) 记录的最后修改日期。

- write_uid(Many2one) 最后修改记录的用户

### 特殊字段

默认情况下，Odoo还需要在所有模型上为各种显示和搜索行为设置一个name字段。用于这些目的的字段可以通过设置_rec_name来覆盖。

> 练习

在openacademy模块中定义一个新的数据模型课程。一个课程有一个标题和一个描述。课程必须有标题。

编辑文件openacademy /models/models.py 包括课程字段。

```python
# openacademy/models.py

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

```

### 数据文件

Odoo是一个高度数据驱动的系统。虽然行为是使用Python代码来定制的，但是模
块的值的一部分是在加载时设置的数据。

> 提示：有些模块的存在仅仅是为了向Odoo添加数据

模块数据通过数据文件、元素的XML文件声明。每个元素都创建或更新一个数据库记录。

```html
<odoo>
    <data>
        <record model="{model name}" id="{record identifier}">
            <field name="{a field name}">{a value}</field>
        </record>
    </data>
</odoo>
```

- model 是记录的Odoo模型的名称。

- id是一个外部标识符，它允许引用记录(不需要知道它在数据库中的标识符)。

- field有一个名称，该名称是模型中字段的名称(例如description)。他们的身体是场的价值。

数据文件必须在要加载的清单文件中声明，它们可以在“Data”列表(总是加载)中声明，也可以在“demo”列表中声明(仅在演示模式下加载)。

> 练习

定义演示数据

创建演示数据填充课程模型和一些示范课程,编辑该文件openacademy /demo/demo.xml,包含一些数据的xml。

```html
# openacademy/demo.xml

<odoo>
    <data>
        <record model="openacademy.course" id="course0">
            <field name="name">Course 0</field>
            <field name="description">Course 0's description

Can have multiple lines
            </field>
        </record>
        <record model="openacademy.course" id="course1">
            <field name="name">Course 1</field>
            <!-- no description for this one -->
        </record>
        <record model="openacademy.course" id="course2">
            <field name="name">Course 2</field>
            <field name="description">Course 2's description</field>
        </record>
    </data>
</odoo>

```

## 演示

操作和菜单是数据库中的常规记录，通常通过数据文件声明。可以通过三种方式触发动作:

- 通过点击菜单项(链接到特定动作)

- 通过单击视图中的按钮(如果这些按钮与操作相连接)

- 作为对对象的上下文操作

因为要声明有一个<menuitem>来声明ir.ui有些复杂。菜单并将其与相应的操作更容易地连接起来。

```html
<record model="ir.actions.act_window" id="action_list_ideas">
    <field name="name">Ideas</field>
    <field name="res_model">idea.idea</field>
    <field name="view_mode">tree,form</field>
</record>
<menuitem id="menu_ideas" parent="menu_root" name="Ideas" sequence="10"
          action="action_list_ideas"/>


```

> 危险

操作必须在XML文件中相应的菜单之前声明。

数据文件按顺序执行，操作的id必须在创建菜单之前显示在数据库中。

> 练习


348/5000

定义新的菜单项

定义新的菜单项来访问OpenAcademy菜单项下的课程。用户应能:

显示所有课程的列表

创建/修改课程

创建/ openacademy openacademy /视图。带有操作的xml和触发操作的菜单

把它添加到openacademy/__manifest .py的数据列表中。

```html
openacademy/__manifest__.py

    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

openacademy/views/openacademy.xml

<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <!-- window action -->
        <!--
            The following tag is an action definition for a "window action",
            that is an action opening a view or a set of views
        -->
        <record model="ir.actions.act_window" id="course_list_action">
            <field name="name">Courses</field>
            <field name="res_model">openacademy.course</field>
            <field name="view_type">form</field>
            <field name="view_mode">tree,form</field>
            <field name="help" type="html">
                <p class="oe_view_nocontent_create">Create the first course
                </p>
            </field>
        </record>

        <!-- top level menu: no parent -->
        <menuitem id="main_openacademy_menu" name="Open Academy"/>
        <!-- A first level in the left side menu is needed
             before using action= attribute -->
        <menuitem id="openacademy_menu" name="Open Academy"
                  parent="main_openacademy_menu"/>
        <!-- the following menuitem should appear *after*
             its parent openacademy_menu and *after* its
             action course_list_action -->
        <menuitem id="courses_menu" name="Courses" parent="openacademy_menu"
                  action="course_list_action"/>
        <!-- Full id location:
             action="openacademy.course_list_action"
             It is not required when it is the same module -->
    </data>
</odoo>

```

## 基本视图

视图定义显示模型记录的方式。每种类型的视图都表示一种可视化模式(记录列表、它们的聚合图…)。视图可以通过它们的类型(例如伙伴列表)或通过它们的id进行通用请求，对于一般请求，将使用具有正确类型和最低优先级的视图(因此每种类型的最低优先级视图是该类型的默认视图)。视图继承允许修改在其他地方声明的视图(添加或删除内容)。


### 通用视图声明