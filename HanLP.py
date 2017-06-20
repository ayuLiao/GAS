# -*- coding:utf-8 -*-
from jpype import *
import os
import sys

reload(sys)
# 因为解码的时候会默认使用系统的编码，一般是ascii，如果是中文就会出现编码错误，直接将系统编码改成utf8则可
sys.setdefaultencoding('utf8')
path = os.getcwd();
# print(path)
startJVM(getDefaultJVMPath(), "-Djava.class.path="+path+"/hanlp-portable-1.3.4.jar:"+path+"/hanlp", "-Xms1g",
         "-Xmx1g")  # 启动JVM，Window下需替换分号;为冒号:
HanLP = JClass('com.hankcs.hanlp.HanLP')

def GetFenWord(content):
    return HanLP.segment(content)

def GetKeyWord(content,number):
    return HanLP.extractKeyword(content,number)

def GetSummary(content,number):
    return HanLP.extractSummary(content,number)

def GetPhrase(content,number):
    return HanLP.extractPhrase(content, number)
# print HanLP.extractKeyword(document, 2)
# # 自动摘要
# print HanLP.extractSummary(document, 3)
# # 短语提取
# phraseList = HanLP.extractPhrase(text,10);
# print phraseList
# 依存句法分析
# print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))

def ShopJVM():
    shutdownJVM()
