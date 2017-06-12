# -*- coding:utf-8 -*-

import docx2txt
import os
import HanLP as ayu
# path = os.getcwd()
# filePath = path+'/中科院.docx'
# text = docx2txt.process(filePath)
# res = ayu.GetKeyWord(text,4)
# res2 = ayu.GetSummary(text,4)
# res3 = ayu.GetPhrase(text,4)
# print res
# print res2
# print res3

# ayu.ShopJVM()

def WToT(filePath):
    text = docx2txt.process(filePath)
    res = ayu.GetKeyWord(text, 4)
    res2 = ayu.GetSummary(text, 4)
    res3 = ayu.GetPhrase(text, 4)
    w2tlist = list();
    w2tlist.append(res)
    w2tlist.append(res2)
    w2tlist.append(res3)
    return w2tlist