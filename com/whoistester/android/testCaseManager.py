'''
Copyright (C) 2012 whoistester
Created on Sep ,2012
@auther: admin@whoistester.com
'''

import sys
import os
import subprocess
from datetime import datetime
#from subprocess import call

DEBUG=True

class testCaseManager:

	def __init__(self,wrapEasyDevice):
		self.resultPath = ''
		self.wrapEasyDevice = wrapEasyDevice
		self.caseSequence = 1
		self.caseStep = 1
		self.caseGroup = 1
		self.caseFailedNum = 0
		self.casePassedNum = 0
		self.testTitle = 'testResult'
		self.caseTitle = ''
		self.caseHtml = ''
		self.caseRet = True
		self.stamp = '-'+str(datetime.now())

	def setResultPath(self,path):
		'''
		create the result file
		'''
		if os.path.exists(path):
			self.resultPath = path
		else:
			os.mkdir(path)
			self.resultPath = path
		
		return True

	def getResultPath(self):

		return self.resultPath


	def __setTestTitle(self,title):
		self.testTitle = title
		if not os.path.exists(self.resultPath+'/'+title+self.stamp):
			os.mkdir(self.resultPath+'/'+title+self.stamp)
			os.mkdir(self.resultPath+'/'+title+self.stamp+'/img')		
		return True


	def testSetup(self):
		self.__setTestTitle("TestResult-"+self.wrapEasyDevice.deviceId)
		self.writeResultHeader()
		return False


	def testStop(self):
		self.writeResultFooter()
		self.wrapEasyDevice.debug('case: %d failed' % self.caseFailedNum)
		self.wrapEasyDevice.debug('case: %d passed' % self.casePassedNum)
		#call('C:\Program Files\Internet Explorer\iexplore.exe '+self.resultPath+'/'+self.testTitle+'/'+self.testTitle+'.html')
		return False


	def caseStart(self,title):
		if len(title) == 0:
			self.caseTitle = str(self.caseSequence)
		else:
			self.caseTitle = title
		self.caseHtml = ''
		self.caseRet = True
		#casestart = '<div style="border:2px ridge green; margin:5px 0"><h3>'+str(self.caseSequence)+'. '+title+'</h3>'
		#self.writeContent(casestart)
		return False

	def getCaseTitle(self):
		if len(self.caseTitle) == 0:
			self.caseTitle = str(self.caseSequence)
		return self.caseTitle

	def caseEnd(self):

		if(self.caseRet):
			self.casePassedNum +=1
			casestart = '<div style="border:2px ridge green; margin:5px 0"><h3 class="green">'+str(self.caseSequence)+'. '+self.caseTitle+'</h3>'
		else:
			self.caseFailedNum +=1
			casestart = '<div style="border:2px ridge red; margin:5px 0"><h3 class="red">'+str(self.caseSequence)+'. '+self.caseTitle+'</h3>'
		caseend = '</div>'
		self.caseHtml = casestart+self.caseHtml+caseend
		self.writeContent(self.caseHtml)
		self.caseSequence +=1
		self.caseStep = 1
		return False

	def saveCaseStatus(self,stepTitle):
		if len(stepTitle) == 0:
			title = self.getCaseTitle()+'_'+str(self.caseStep)
		else:
			title =  self.getCaseTitle()+'_'+stepTitle
		self.caseStep +=1
		self.wrapEasyDevice.takeSnapshot().writeToFile(self.getResultPath()+'/'+self.testTitle+self.stamp+'/img/'+title+ '.png','png')		
		self.caseHtml += '<span class="imgDiv"><img src="img/'+title+ '.png" width="150px"/> </span>'
		#self.writeContent(caseend)		
		return False		


	def writeContent(self,content):
		
		f = open(self.resultPath+'/'+self.testTitle+self.stamp+'/'+self.testTitle+'.html','a')
		f.write(content+'\r\n')
		f.flush()
		f.close		


	def writeResultHeader(self):
		header = '<html><head><title>'+self.testTitle+'</title>'
		header += '''<style type="text/css">
body
{
width:1024px; 
margin:0 auto;
}
div#main{
width:1024px;
margin:0 auto;
}
div
{
   padding:5px 5px;
}
span.imgDiv{
   display:none;
   cursor:pointer;
}
div#report
{
  margin-top:5px;
  background-color:green;
}

h3.red{
   background-color:red;
   margin:0 0 5px 0;
   cursor:pointer;
}
h3.green{
   background-color:#aaffaa;
   margin:0 0 5px 0;
   cursor:pointer;
}
div#report p
{
  font-weight:900;
  color:#FFFFFF;
  text-align:center;
  font-size:30px;
  margin:0;
  padding:0;
}

div#popupImg
{
display:none;
background-color:#aaffaa;
padding:10px;
z-index:10;

}


div#close
{
  background-color:green;
  color:#FFFFFF;
}
</style>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.14/jquery-ui.min.js" type="text/javascript"></script>
<script type="text/javascript">
$(document).ready(function(){
	var foldflag = 0;

	$("#popupImg").draggable();

	$("h3").click(function(){
		
                if($(this).parent().children('span.imgDiv').css('display') == 'none')
                 {
		   $(this).parent().children('span.imgDiv').css('display','inline');
		
                 }
                else {
		     $(this).parent().children('span.imgDiv').hide();
                 }
        });

	$("span#unfold").click(function(){

                	$("span.imgDiv").show();

	});

	$("span#fold").click(function(){
                	
			$("span.imgDiv").css('display','none');

	});		

        $(".imgDiv img").click(function(){
                var position = $(this).position();
		$("#popupImg").css({position:'absolute',left:position.left+50,top:position.top-200,display:'block',cursor:'move'});
		$("#popupImg img").attr('src',$(this).attr('src'));
		$("#popupImg img").css('width','350px');
		$("#close").css('cursor','pointer');

	});

	$("#close").click(function(){
		$(this).parent().css('display','none');

	});
});
</script>
'''
		header +='</head>\r\n<body><div id="main"><div id="popupImg"><div id="close">CLOSE this Window</div><img /></div><div id="report" style="border:2px ridge green;"><p>Test Report</p>'
		header +='<span id="unfold" style="color:#FFFFFF;border:1px solid #ffffff;padding:2px;margin-right:5px;">Unfold all</span><span id="fold" style="color:#FFFFFF;border:1px solid #ffffff;padding:2px;">Fold all</span></div>'
		header +='<div style="border:2px ridge green; margin:5px 0"><b>Phone Details:</b><br>'+self.getVersion()+'</div>'
		self.writeContent(header)
		
	def writeResultFooter(self):
		footer = '</div></body></html>'
		self.writeContent(footer)

	def getVersion(self):
		
		return os.popen( 'adb shell cat /etc/version.conf').read().replace('\r\n','<br>')

	def assertText(self,id,text):
		if(self.wrapEasyDevice.checkIdExist(id)):
			if(self.wrapEasyDevice.getTextById(id) == text):
				self.wrapEasyDevice.debug('case: %s passed' % self.caseTitle)
				return True
		self.wrapEasyDevice.debug('case: "%s" failed' % self.caseTitle)
		self.caseRet=False
		return False

	def assertId(self,id):
		if(self.wrapEasyDevice.checkIdExist(id)):
			self.wrapEasyDevice.debug('case: "%s" passed' % self.caseTitle)
			return True
		self.wrapEasyDevice.debug('case: "%s" failed' % self.caseTitle)
		self.caseRet=False
		return False
		
