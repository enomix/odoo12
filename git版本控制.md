### 上传文件

在本地目录中创建一个git的目录

进入目录之后鼠标右击点击git bush here

然后进入命令行

```shell
git init #初始化仓库，仓库里面不能有东西

#往这个文件夹里面添加文件

git status #查看状态会出现no commits yet(还没提交) untracked files(没有被装载的文件) 文件名被标红了

git add .  #装载全部文件

git status #这时查看状态会发现：no commits yet(还没提交) Changes to be committed（需被提交的更改），文件名被标绿了

git commit -m "提交了第一个文件" #提交被装载的文件，双引号内写这次的提交名

git status #这时查看状态查看状态：nothing to commit, working tree clean

git remote add origin https://github.com/enomix/odoo12.git #链接github仓库，具体配置可以在 .git 文件夹下的config文件里面查看和配置

git remote -v #查看fentch push的地址, orgin为远程地址的别名

git push origin master #推送到github里面，第一次连接到github需要登录授权

git remote add orgin "https://gitee.com/enomix/odoo12.git"#链接到码云，同样码云第一次链接也需要登录授权

```

 









### 版本控制系统

##### 本地版本控制系统

将项目的各个版本放到本地磁盘里面备份，坏处就是不同系统之间协同开发非常麻烦

##### 集中化版本控制系统CVCS

（Centralized Version Control Systems）

比如说CVS、Subversion以及Perforce，都有一个集中的管理服务器，但是又有了新的问题：单点故障。只要整个项目的历史记录被保存在单一位置，就有丢失所有历史最新记录的风险

##### 分布式版本控制系统DVCS

Distributed Version Control System

比如说Git, Mercurial, Bazaar以及Darcs等，客户端不只是提取出最新版的文件快照，而是把最原始的代码仓库镜像到本地，任何一处协同工作的服务器发生故障，时候都可以用任何一个镜像出来的本地仓库恢复。因为每一次的提取操作，实际上都是一次对代码仓库的完整备份













### 安装配置

1. 安装Git

```
https://git-scm.com/downloads
或者
https://gitforwindows.org/
```

2. 检查是否安装好

```shell
git --version
```

出现了版本号就是安装好了

3. 打开终端

鼠标右键Git Bash Here



5. 创建一个自己的目录，然后进去操作

6. 初始配置

   配置用户名称和email（global代表全局，不加这个参数的话就表示当前项目用这个名字和邮箱，如果你建立了很多的项目的话就加 --global）

```shell
git config --global user.email "670849551@qq.com"
git config --global user.name "sp"
```

7. 这项操作需要提前安装好sublime，并且配置环境变量path里面sublime的安装地址

```shell
subl .git/config
```

8. .git目录下的东西

```shell
Administrator@sp MINGW64 ~/git/.git (GIT_DIR!)
$ ll
total 7
-rw-r--r-- 1 Administrator 197121  23 Apr  7 15:35 HEAD
-rw-r--r-- 1 Administrator 197121 130 Apr  7 15:35 config
-rw-r--r-- 1 Administrator 197121  73 Apr  7 15:35 description
drwxr-xr-x 1 Administrator 197121   0 Apr  7 15:35 hooks/
drwxr-xr-x 1 Administrator 197121   0 Apr  7 15:35 info/
drwxr-xr-x 1 Administrator 197121   0 Apr  7 15:35 objects/
drwxr-xr-x 1 Administrator 197121   0 Apr  7 15:35 refs/

```

前缀d表示这是个目录

9. 刚刚修改的name 和 email 就是 .git 目录下的东西

10. 下载某个人的github上面的项目

    ```shell
    git clone https://github.com/houdunwang/cart.git
    ```

    

11.创建了工作代码之后就将代码添加add到暂存区里面（小推车），之后会提交到Git从仓库里面

```shell
Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.php

nothing added to commit but untracked files present (use "git add" to track)

Administrator@sp MINGW64 ~/git/hd (master)
$ git add a.php

Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.php


Administrator@sp MINGW64 ~/git/hd (master)

```

提交到仓库里面

```shell
Administrator@sp MINGW64 ~/git/hd (master)
$ git commit -m '测试学习'
[master (root-commit) e482c63] 测试学习
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.php
 create mode 100644 b.php

Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master
nothing to commit, working tree clean
```

修改了a.php内容之后，状态将变为modified， 需要再次添加到推车里面add，然后再提交到仓库里面commit

```shell
Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.php

no changes added to commit (use "git add" and/or "git commit -a")

Administrator@sp MINGW64 ~/git/hd (master)
$ git add a.php

Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   a.php


Administrator@sp MINGW64 ~/git/hd (master)
$ git commit -m '第二次入库'
[master 9112d0c] 第二次入库
 1 file changed, 1 insertion(+)


```



改了很多文件，需要加入到推车里面git add .

```shell
Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.php
        d.php
        f.php

nothing added to commit but untracked files present (use "git add" to track)

Administrator@sp MINGW64 ~/git/hd (master)
$ git add .

Administrator@sp MINGW64 ~/git/hd (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   c.php
        new file:   d.php
        new file:   f.php

```

修改了很多文件，提交时不想提交其中的某几个文件，需要写忽略文件配置.gitignore

```shell
subl .gitignore
```

这个文件里面写需要忽略的文件信息

```gitignore
*.txt		//忽略后缀为txt的文件
!a.txt		//除了a.txt
/vendor		//忽略在vendor文件夹里面的文件
```

最后添加到推车里面

```shell
git add .
```





移除东西rm（本地和仓库里面都移除）

```shell
$ git rm a.txt
```

移除仓库里面的不移除本地的

```shell
$ git rm a.txt
```

仓库里的文件重命名，并重新提交

```shell
Administrator@sp MINGW64 ~/git/bbs (master)
$ git mv c.php houdunren.php

Administrator@sp MINGW64 ~/git/bbs (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    c.php -> houdunren.php


Administrator@sp MINGW64 ~/git/bbs (master)
$ git commit -m 'c.php rename houdunren.php'
[master 5505599] c.php rename houdunren.php
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename c.php => houdunren.php (100%)

```







### 查看日志

查看所有的变动日志

```shell
git log -p
```

查看最近的一条日志

```shell
git log -p -1
```

查看最近的两条日志

```shell
git log -p -2
```

```shell
git log --oneline
```

```shell
git log --name-only

```

```shell
git log --name-status
```

### alias命令

修改之后按a执行添加（将add变为了a，少敲了点字符）

```shell
git config --global alias.a add
```

也可以在主目录修改配置文件

```shell
subl .gitconfig
```

