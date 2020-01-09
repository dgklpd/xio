# xio 
# ![](https://github.com/CAIMEOX/FbFiles/images/master/b1.png)
此程序对武汉外国语学校美加分校五班的同学提供技术支持，和开源版本

## 使用教程

###windows

在windows上，将本仓库的代码，下载解压，找到xio_SCE=>msi版本=>build文件夹中的一个安装包，安装下载程序

###在Android上

首先先网页搜索下载termux这是安卓端的一款linux终端模拟器，相信熟悉linux,shell脚本的同学会用的得心应手，当然没有的我这里也给出教程：
1. 下载终端软件(如Termux),并给予其存储权限.
2. 执行apt update && apt upgrade 如弹出(y/n)确认信息,输入y后回车,如果报错则重新输入.
3. 执行apt install python,如弹出(y/n)确认信息,输入y后回车
4. 执行apt install git,如弹出(y/n)确认信息,输入y后回车  
5. 执行git clone https://github.com/dgklpd/xio_latest.git
6. cd xio_latest
7. python xio.py
8. 后续如需运行只需执行6、7步.
   注意:如果哪一步报错了,必须重新执行,不然后续步骤会一错再错…
   
###在linux上

相信敢用linux的人都是大佬，和termux的命令一样，只是主要要加sudo
   
## 版本区分
xio现在有两个版本:SCE和FSE
在手机上运行的是SCE控制台版
可以在电脑上运行的是FSE版本，有前端，用到依赖库easygui

## 开发相关

* [python](http://python.org) - 程序语言

###开发者
* [**dgklpd**](https://github.com/dgklpd)
喜欢这个项目别忘记给我们个Star!

## License
此项目纯粹开源，不收取任何费用

## 鸣谢
* 盖主席
* python37
