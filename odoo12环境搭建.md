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

启动odoo12的实例

```shell
~/odoo-dev/odoo/odoo-bin
```

浏览器里进入

```
http://[用户名]:8069
```



参考：https://www.toutiao.com/i6771961036133106184/?in_ogs=1&traffic_source=CS1114&utm_source=HW&source=search_tab&utm_medium=wap_search&prevent_activate=1&original_source=1&in_tfs=HW&channel=



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

