> https://docs.docker.com/samples/library/odoo/#start-a-postgresql-server
> docker run -p 8069:8069 --name odoo --link db:db -t odoo

```
/opt/odoo/--src(源码)
			--odoo(各种文件配置)
		  --runtime(程序)
		  	--test(app)
		  --addons(模块类)
```


- 操作环境：（用docker进行镜像文件的拉取具体操作看[https://docs.docker.com/samples/library/odoo/#start-a-postgresql-server]）
	- docker
	- odoo镜像文件
    - postgresql镜像文件




## 创建db容器

```
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=admin --name db postgres:9.6
```

## 给/opt/odoo 的odoo添加权限

```
chown -R 1000:1000 odoo
```

## 创建odoo容器

```
docker run -v /opt/odoo/runtime/test:/var/lib/odoo -v /opt/odoo/addons:/mnt/extra-addons -v /opt/odoo/src/odoo:/usr/local/lib/python2.7/site-packages/odoo -p 8069:8069  --name test --link db:db -t a33faea4222d 
保证路径没问题，最后的docker镜像文件id正确
```

## 更改容器内数据库配置文件(将)

将odoo.cof文件复制到docker中的test文件夹里：
```
docker cp /home/liubaojia/桌面/odoo.conf test:/etc/odoo/
```

## 重启数据库和odoo容器

然后重新启动数据库db和odoo容器一遍加载上一步的odoo.conf

```
docker restart db test
```


- 开启docker容器服务（ps：一定要先开启数据库db，再开启odoo）
```
docker start NAME

```
- 关闭docker容器服务
```
docker stop NAME
```
- 删除docker容器内的服务
```
docker rm NAME
```
- 强制删除docker容器服务
```
docker rm -f NAME
```
- 查看docker内的镜像
```
docker image ls
```
- 查看docker内开启的镜像
```
docker ps
```
- 查看docker内开启的历史镜像
```
docker ps -a
```
- 搜索docker镜像
```
docker search NAME
```

