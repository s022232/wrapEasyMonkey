# wrapEasyMonkey-

代码已经不在更新，建议python编写android 自动化脚本， 可以参考 https://github.com/xiaocong/uiautomator。 
或者通过apium python client。


Api(libraries) based monkeyrunner , easy to build the android automation test script.  Support identifing the ui element by Id or by text.

more contents please visit my blog :  http://lihao.cf/category/my-work/wrapeasydevice/

更多信息请访问我的博客 http://lihao.cf/category/my-work/wrapeasydevice/

[purpose: ]

1. 将monkeyDevice 与 easyMonkeyDevice统一封装到库
2. 进行自动化操作时, 增加对异常处理,防止异常退出 (例如 当某textview未显示出来时, 捕捉对该textview的操作异常,防止测试脚本异常退出. 如果手动在脚本里加入sleep语句， 但sleep的时间难以指定）
3. 增加了一些比较便捷的函数， 降低了使用 monkeyDevice 和 easyMonkeyDevice 的复杂度。


[wrapEasyMonkey ]

new feature 新特性:
1. don’t need set the env vars anymore
不需要再设置wrapeasymonkey的环境变量了
2. just put the lib into the android sdk tools lib directory
只需要将wrapeasymonkey的lib 放到 android sdk 的tools文件夹里的lib目录里，就可以使用，简单。
3. write the test case with python code , and monkeyrunner run it.
写测试用例代码，并用monkeyrunner 执行该case

[Pre-use: 前提：]

1. you have the android sdk installed.
你需要android sdk 安装
2. download the wrapEasyMonkey 2.0 from sourceforge 
下载wrapeasymonkey.zip 后缀名改为wrapeasymonkey.jar  并放到android sdk monkeyrunner里对应的lib目录下

[Install the lib 安装lib:]

1. unzip the downloaded file and extract the wrapeasymonkey.jar.
解压，并拿到wrapeasymonkey.jar
2. mv the jar to the lib directory of the android sdk tools dir.
将jar移动到 android sdk 的tools文件夹里的lib目录里

[How to use: 如何使用]

1. write the python code folow the examples , and monkeyrunner it.
It’s easy to test the android.

[Known isues: 已知问题]

1. couldn’t simultaneously run multi test process on multi devices. 经过试验, 同一个脚本不能同时在多个设备上运行. 该问题经分析应为monkeyrunner及android底层问题. 当同时执行时,既传入的deviceid 不同,但会发现发送的event会串. 既发给a设备的key动作,有时会串到b设备.
2. couldn’t locate the coordinate of the dialog button , you should use the direction press to chose ok or cancel and context menu instead . 系统对话框的坐标不能通过id进行定位, 需要通过发送方向键,来定位并进行触摸touch.



[如何使用呢]

1. 首先你需要有最新的android sdk.
这只是一个sdk manager工具。下载安装后，并打开。 可以看到有tools，Android不同版本的sdk platform等（例如Android 4.0.3 api15 , api 13)， 还有Extras。

注意我们这里至少需要下载tools里的Android SDK tools 和 Android SDK Platform-tools。 如果你已经有下载过， 建议您升级到最新的版本。 因为sdk 经常有更新，有些文件会有变动，包括文件夹的组织结构。

2. 将下载到的wrapEasyMonkey源码zip包。解压后放到某个目录。 您可以解压到sdk里的tools文件夹的lib子文件夹。 当然放到哪里都ok，因为之后我们设定环境变量，以便让monkeyrunner 执行脚本的时候可以加载到这些库。 但未了便于您的管理， 所以建议放到sdk里的某个目录。

3. 设定环境变量。 设定环境并不是必须的， 但如果不设定，那么意味着您的程序和库文件的位置不能够是灵活的。 就是说代码中必须写死您加载库的地址。 当然我们不像这么做。
1) 首先我们要添加的是 Android_HOME 环境变量。
2) 然后是ANDROID_VIEW_CLIENT_HOME 环境变量。 后者是指的您的wrapEasyMonkey源码的解压路径。 例如 C:\Users\hp\Downloads\AndroidViewClient\AndroidViewClient 进入后，我们可以看到如下的目录结构就对了。
3个文件夹(examples, src, tests) ， 2个文件(.project, .pydevproject)
3) 最后我们将android sdk里的tools文件夹和platform-tools文件夹加到系统环境变量path里。这样我们可以方便的调用tools的命令了。例如adb, ddms, hierachyviewer等。

4. 写测试脚本。
如下是一个测试脚本例子(wrapEasyMonkey api 具体说明及介绍)。 当然例子也可以去wrapEasyMonkey里的例子文件夹找例子。
```
#! /usr/bin/env monkeyrunner
'''
Copyright (C) 2012  whoistester.com
@author: whoistester
'''

import re
import sys
import os
import string
import locale

'''
将库的地址添加到系统路径
'''
try:
ANDROID_VIEW_CLIENT_HOME =  os.environ['ANDROID_VIEW_CLIENT_HOME']
except KeyError:
print sys.stderr, "%s: ERROR: ANDROID_VIEW_CLIENT_HOME not set in environment" % __file__
sys.exit(1)
sys.path.append(ANDROID_VIEW_CLIENT_HOME + '/src')
sys.setdefaultencoding('utf-8')

from com.dtmilano.android.viewclient import ViewClient
from com.dtmilano.android.wrapEasyMonkey import wrapEasyMonkey
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

package = 'com.android.contacts'
activity = '.activities.PeopleActivity'
component = package + "/" + activity
device = MonkeyRunner.waitForConnection(10) #连接device

device.startActivity(component=component)# 启动联系人应用

easyDevice = EasyMonkeyDevice(device) #生成easyDevice 对象

wrapdevice = wrapEasyMonkey(easyDevice,device) #由easyDevice,device 生成wrapEasyMonkey对象

create_contact_button = wrapdevice.getView('id/create_contact_button')# 通过wrapEasyMonkey对象获得创建新联系人的view视图对象

wrapdevice.touchView(create_contact_button,wrapdevice.DOWN_AND_UP) #对该view进行点击操作，该函数会调用easyMonkey api，
自动获得该view的坐标值，并进行touch行为。

wrapdevice.sleep(2) # 睡眠2秒
wrapdevice.touchDialogButton(2)  #对弹出的对话框，进行选择 ， 参数为1 时， 选择左边的按钮， 参数2时，选择右边的按钮。 为什么没有用touchView函数，
是因为当前最新的layout分析有问题，#不能获得对话框的alertdialog的正确的坐标值。 所以这里的touchDialogButton是通过上下的方向键进行控制的。
wrapdevice.touchViewById('id/0x3',wrapdevice.DOWN_AND_UP) #touchViewById 可以直接对view的id进行直接touch， 不需要中间先获得该view的对象。


wrapdevice.type('test01') # 输入字符
```

5. 执行测试脚本。 打开dos命令窗口或者linux的shell terminal。 运行
“monkeyrunner 脚本路径和名称”。 执行之前确信您已经正确安装了手机的驱动. 可以通过adb devices 进行查看.

相关文章:
