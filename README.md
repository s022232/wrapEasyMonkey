# wrapEasyMonkey-
Api(libraries) based monkeyrunner , easy to build the android automation test script.  Support identifing the ui element by Id or by text.

purpose: 
1. 将monkeyDevice 与 easyMonkeyDevice统一封装到库
2. 进行自动化操作时, 增加对异常处理,防止异常退出 (例如 当某textview未显示出来时, 捕捉对该textview的操作异常,防止测试脚本异常退出. 如果手动在脚本里加入sleep语句， 但sleep的时间难以指定）
3. 增加了一些比较便捷的函数， 降低了使用 monkeyDevice 和 easyMonkeyDevice 的复杂度。



wrapEasyMonkey 2.0 released

new feature 新特性:
1. don’t need set the env vars anymore
不需要再设置wrapeasymonkey的环境变量了
2. just put the lib into the android sdk tools lib directory
只需要将wrapeasymonkey的lib 放到 android sdk 的tools文件夹里的lib目录里，就可以使用，简单。
3. write the test case with python code , and monkeyrunner run it.
写测试用例代码，并用monkeyrunner 执行该case

Pre-use: 前提：
1. you have the android sdk installed.
你需要android sdk 安装
2. download the wrapEasyMonkey 2.0 from sourceforge 
下载wrapeasymonkey 2.0 并放到正确的lib目录下

Install the lib 安装lib:
1. unzip the downloaded file and extract the wrapeasymonkey.jar.
解压，并拿到wrapeasymonkey.jar
2. mv the jar to the lib directory of the android sdk tools dir.
将jar移动到 android sdk 的tools文件夹里的lib目录里
How to use: 如何使用

1. write the python code folow the examples , and monkeyrunner it.

It’s easy to test the android.

Known isues: 已知问题
1. couldn’t simultaneously run multi test process on multi devices. 经过试验, 同一个脚本不能同时在多个设备上运行. 该问题经分析应为monkeyrunner及android底层问题. 当同时执行时,既传入的deviceid 不同,但会发现发送的event会串. 既发给a设备的key动作,有时会串到b设备.
2. couldn’t locate the coordinate of the dialog button , you should use the direction press to chose ok or cancel and context menu instead . 系统对话框的坐标不能通过id进行定位, 需要通过发送方向键,来定位并进行触摸touch.
