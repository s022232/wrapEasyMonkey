
import sys
import os
import inspect
import traceback

class testRunner:
	
	def __init__(self):
		self.casePassed=0
		self.caseFailed=0
		self.result={}

	def run(self,objectName):

		print 'Starting to run the testcase'
		self.__testSetup(objectName)
		for key in dir(objectName):
			if( key == 'testSetup' or key == 'tearDown'):
				continue
			if(self.__isTestCase(key)):
				if(self.__ismethod(objectName,key)):
					self.__executeCase(objectName,key)
					self.__testTearDown(key)
				else:
					print '%s method is not executed.it\'s prefix isnot "test"' % key
		print 'Case passed: %s' % self.casePassed
		print 'Case failed: %s' % self.caseFailed
		print 'Case Result: %s' % self.result



	def __ismethod(self,objectName,methodName):
		try:
			inspect.ismethod(objectName.__class__.__dict__[methodName].__get__(objectName,objectName.__class__))
			return True
		except:
			return False

	def __isTestCase(self,caseName):
		if(caseName[:4] == 'test'):
			return True
		return False

	def __testSetup(self,objectName):
		try:
			objectName.__class__.__dict__['testSetup'].__get__(objectName,objectName.__class__)()
			return True
		except:
			print 'No testSetup method to call , there\'s no need to setup the test envrionments '
			return False

	def __testTearDown(self,objectName):
		try:
			objectName.__class__.__dict__['tearDown'].__get__(objectName,objectName.__class__)()
			return True
		except:
			return False

	def __executeCase(self,objectName,caseName):
		print     '=================case: %s=====================' % caseName
		endInfo = '================================================='
		try:
			objectName.__class__.__dict__[caseName].__get__(objectName,objectName.__class__)()
			self.casePassed+=1
			self.result[caseName]='pass'
			print 'passed'
			print endInfo
			return True
		except:
			sys.exc_info()
			#traceback.print_exc()
			self.caseFailed+=1
			self.result[caseName]=traceback.format_exc()
			print 'failed'
			print endInfo
			return False
