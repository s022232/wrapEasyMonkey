'''
basical import file
'''

import re
import sys
import os
import string
import locale

'''
try:
    ANDROID_WRAPEASYMONKEY_HOME =  os.environ['ANDROID_WRAPEASYMONKEY_HOME']
except KeyError:
    print >>sys.stderr, "%s: ERROR: ANDROID_WRAPEASYMONKEY_HOME not set in environment" % __file__
    sys.exit(1)
sys.path.append(ANDROID_WRAPEASYMONKEY_HOME + '/src')
#print sys.getdefaultencoding()
'''
sys.setdefaultencoding('utf-8')
from com.whoistester.android.viewclient import ViewClient
from com.whoistester.android.wrapEasyMonkey import wrapEasyMonkey
from com.whoistester.android.testRunner import testRunner
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

