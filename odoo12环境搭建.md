### 安装配置

安装Ubuntu18桌面版

安装PostgreSQL数据库

```shell
sudo apt update #查看需要更新哪些软件，可以先不执行，因为在运行时会占用某些资源
#参考https://blog.csdn.net/dream_follower/article/details/90311799

sudo apt install postgresql -y # 安装PostgreSQL
sudo su -c "createuser -s $USER" postgres # 创建数据库超级用户
```

安装odoo12所需的系统依赖

```shell
sudo apt update #查看哪些软件需要更新
sudo apt upgrade #执行更新到最新软件版本，与刚才查看的哪些软件需要更新进行对比
sudo apt install git -y #安装Git
sudo apt install python3-dev python3-pip -y # 安装Python3 for dev和pip3
sudo apt install build-essential libxslt-dev libzip-dev libldap2-dev libsasl2-dev libssl-dev -y # 安装依赖包
```

创建安装目录，下载odoo12的源码

```shell
mkdir ~/odoo-dev # 创建工作目录
cd ~/odoo-dev # 进入工作目录

# 如果这里克隆比较慢可以从国内镜像网站克隆
git clone https://github.com/odoo/odoo.git -b 12.0 --depth=1 # 获取 Odoo12 源码
#国内码云的odoo12源码
git clone https://gitee.com/mirrors/odoo.git -b 12.0 --depth=1 # 获取 Odoo12 源码
```

安装python依赖

```shell
pip3 install -r ~/odoo-dev/odoo/requirements.txt # odoo指定包
pip3 install --user num2words phonenumbers psycopg2-binary watchdog xlwt # 其他依赖包
```

### 虚拟环境安装

```shell
#安装：
pip3 install virtualenv

#创建：
virtualenv venv

#执行这个目录下的active，进入虚拟环境
source ./venv/bin/active

#进入了虚拟环境之后，用户名前面就会出现(venv)这个标签，如下：
(venv) sp@sp-virtual-machine:~/odoo-dev/odoo$

#这个时候进入odoo源码的目录，可以看到有requirements.txt这个文件，这个文件包含了odoo所需要的全部依赖
cd odoo/
#执行下载（在虚拟环境venv下时）
pip3 install -r requirements.txt
#然后所需的依赖就下载到了venv的目录里面了，venv目录大小到了120多MB
```



启动odoo12的实例

```shell
~/odoo-dev/odoo/odoo-bin
```

浏览器里进入

```
http://[用户名]:8069
```



参考：https://www.toutiao.com/i6771961036133106184/?in_ogs=1&traffic_source=CS1114&utm_source=HW&source=search_tab&utm_medium=wap_search&prevent_activate=1&original_source=1&in_tfs=HW&channel=



### 远程开发odoo

在Windows安装pycharm远程连接Linux里面的odoo进行开发

#### 1.设置python解释器

打开Settings>Project:pycharm>Pychon Interpreter>添加一个SSH Interpreter，

设置Host地址，就是Linux的IP地址，然后填上用户名和密码，测试连接。

设置Python interpreter path:Linux下面的venv里面的python解释器的地址

设置PyCharm helpers path:home/用户名/.pycharm_helpers

#### 2.设置地址

Tools>Development>configration

这里面也可以设置远程连接的地址

#### 3.设置启动项

点击run这里的edit然后进入

设置Script path: Linux里面odoo目录下的odoo-bin

设置Parameters:-c Linux里面odoo目录/debian/odoo.conf，没有则新建一个

设置Working directory开发路径

### 常见问题

Linux的IP能与windows 互相 ping 通，但是xhell连接不上Linux，pycharm也连接不上Linux

可能的原因就是ssh相关的服务没有安装

```shell
ps -e | grep ssh #检查ssh是否安装了

sudo apt-get install openssh-server#安装ssh服务

/etc/init.d/ssh start #启动ssh服务

#出现问题时可以重启ssh服务
sudo service ssh restart
```

### 连接pycharm开发

可以在windows下安装pycharm专业版

或者在Linux下安装社区版（免费）

