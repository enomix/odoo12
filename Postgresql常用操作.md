以默认用户登录：

```shell
#切换至postgres
sp@sp-virtual-machine:/usr/local/pycharm/pycharm-2021.1/bin$ sudo su postgres 
#登入默认数据库
postgres@sp-virtual-machine:/usr/local/pycharm/pycharm-2021.1/bin$ psql postgres
psql (10.16 (Ubuntu 10.16-0ubuntu0.18.04.1))
Type "help" for help.


#设置密码
postgres=# postgres= # \password postgres  
Enter new password: 
Enter it again: 
postgres-# 

```

卸载postgresql

```shell
sudo apt-get purge 'postgresql-*'
sudo apt-get autoremove 'postgresql-*'
```

安装PostgreSQL数据库

```shell
sudo apt update #查看需要更新哪些软件，可以先不执行，因为在运行时会占用某些资源
#参考https://blog.csdn.net/dream_follower/article/details/90311799

sudo apt install postgresql -y # 安装PostgreSQL
sudo -u postgres psql#打开postgre数据库
ALTER USER postgres WITH PASSWORD '123456'; #修改数据库用户密码

```

