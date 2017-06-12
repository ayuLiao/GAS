#!/usr/bin/python
# coding:utf-8
import wx
import os
import Pdf2Txt as p2t
import Word2Txt as w2t
def OnOpen(event):
    """

    Load a file into the textField.
    """
    # dialog = wx.FileDialog(None, 'Notepad', style=wx.OPEN)
    wilcard = "Python source (*.pdf)|*.pdf|Compiled Python (*.pdf)|*.pdf|All files (*.*)|*.*"
    wilcard = ""
    dialog = wx.FileDialog(None, "选择一个文件", os.getcwd(), "", wilcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        filename.SetValue(dialog.GetPath())
        # file = open(dialog.GetPath())
        # contents.SetValue(file.read())
        # file.close()
        # print dialog.GetPath()
    dialog.Destroy()


def OnSave(event):
    """

    Save text into the orignal file.
    """
    if filename.GetValue() == '':
        contents.SetValue("必须选择一个文件才可进行运算！！！")
        # dialog = wx.FileDialog(None, 'Notepad', style=wx.SAVE)
        # if dialog.ShowModal() == wx.ID_OK:
        #     filename.SetValue(dialog.GetPath())
            # file = open(dialog.GetPath(), 'w')
            # file.write(contents.GetValue())
            # file.close()
        # dialog.Destory()
    else:
        filepath =  filename.GetValue()
        fileExtension = filepath.split(".")[-1]
        if(fileExtension == "pdf"):
            res = p2t.main(filepath)
        if(fileExtension == "docx"):
            res = w2t.WToT(filepath)
        if(fileExtension != "pdf" or fileExtension != "docx"):
            contents.SetValue("只能运算pdf格式和docx格式的文件！！！")
        # contents.SetValue(p2t.main(filename.GetValue()))
        # contents.SetValue(res[0][0]+"\n"+res[0][1])
        # contents.SetValue("haha")

        str = "运算开始\n\n"
        y=0
        for r in res:
            i = 0
            for k in r:
                if(i==0):
                    if(y==0):
                        str += "文章关键词：\n"
                    if(y==1):
                        str += "文章摘要：\n"
                    if(y==2):
                        str += "文章短语：\n"
                str += "-----"+k+"\n"
                i = i+1
            y = y+1
        str +="\n运算结束"
        contents.SetValue(str)



app = wx.App()
win = wx.Frame(None, title="文章摘要运算器  ayuliao", size=(600, 400))

bkg = wx.Panel(win)

# Define a 'load' button and its label, bind to an button event with a function 'load'
loadButton = wx.Button(bkg, label='选择文件')
loadButton.Bind(wx.EVT_BUTTON, OnOpen)

# Define a 'save' button and its label, bind to an button event with a function 'save'
saveButton = wx.Button(bkg, label='运算')
saveButton.Bind(wx.EVT_BUTTON, OnSave)

# Define a textBox for filename.
filename = wx.TextCtrl(bkg)
# Define a textBox for file contents.
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

# Use sizer to set relative position of the components.
# Horizontal layout
hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
# Vertical layout
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()