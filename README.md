sendMyIP
===============

Raspberry Pi: Automatically send it's IP address to your samrtphone whenever it get started.

树莓派：系统启动时自动推送IP地址到智能手机

# 在Instapush上建立推送服务，并安装移动app

要处理推送通知，我使用了一个名为Instapush的免费推送服务。Instapush在iOS和Android上有免费的app，而且这个平台上也有一个易于使用的REST API供软件开发者使用。

1. 首先，在[https://instapush.im/](https://instapush.im/)注册并登陆；
2. 下载移动app；
3. 登陆到app上，使用你在网站上注册的账户即可；
4. 在app上登陆后，你会发现控制面板中已经显示你的设备已连接到Instapush的账户上了。去这里查看[https://instapush.im/dashboard](https://instapush.im/dashboard)
5. 然后点击设备标签；
6. 接下来，点击*app*标签。然后选择添加应用；
7. 为你的应用选择一个名称，然后点击*Add*；
8. 添加了你的应用之后，你会进入事件界面；
9. 为你的事件选择一个标题。建议在事件名中不要加入任何空格；
10. 你需要添加至少一个*tracker*。这基本上就是一个用在推送通知中的变量。例如命名为“message”；
11. 最后，输入你想要推送的消息内容。我的Python代码将变量{message}传给Instapush服务，因此建议只把{message}添加到Message字段即可；
12. 点击*Basic Info*标签，记*下Application ID*和*Application Secret fields*这两个字段的内容。在编写Python代码时需要用到这些。

# 安装pycurl库

我们的Python程序需要使用一个称为pycurl的库来发送API请求给InstaPush服务。在树莓派上运行下面的命令来安装这个Python库

```
sudo apt-get install python-pycurl
```

# 编辑代码

1. 开机启动检测网络可用性
2. 获取树莓派本地网卡eth0的IP地址
3. 通过Python脚本推送消息到手机上

# 设置代码开机启动

向/etc/rc.local文件中添加启动命令，注意文件要以exit 0结束

```
python /home/pi/python/sendIP/sendIP.py &
```

