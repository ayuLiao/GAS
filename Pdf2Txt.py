# -*- coding:utf-8 -*-
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import HanLP as ayu
import string

# converts pdf, returns its text content as a string
# from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


# 转换目录,将pdfDir中的所有pdf转成txt文件，保存到txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "//"
    for pdf in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename)  # get string of text content of pdf\
            res = ayu.GetKeyWord(text,5)
            res2 = ayu.GetSummary(text,5)
            res3 = ayu.GetPhrase(text,5)
            p2tlist = list();
            p2tlist.append(res)
            p2tlist.append(res2)
            p2tlist.append(res3)
            # print p2tlist
            # print res2
            # print type(res2)
            # print res3
            # textFilename = txtDir + pdf + ".txt"
            # textFile = open(textFilename, "w")  # make text file
            # textFile.write(text)  # write text to text file
            return p2tlist


# i : info
# p : pdfDir
# t = txtDir
def main(argv,pdfDir = "",txtDir = ""):
    try:
        opts, args = getopt.getopt(argv, "ip:t:")
    except getopt.GetoptError:
        print("pdfToT.py -p <pdfdirectory> -t <textdirectory>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-i":
            print("pdfToT.py -p <pdfdirectory> -t <textdirectory>")
            sys.exit()
        elif opt == "-p":
            pdfDir = arg
        elif opt == "-t":
            txtDir = arg
    return convertMultiple(pdfDir, txtDir)


if __name__ == "__main__":
    main("/home/ayuliao/HanLP/AyuZRYY/word2vec.pdf")