'''
计时器
作者：青橙-821028463
日期：2017-01-19

'''
def switch(event):
    '''
    开始暂停控制
    '''
    global basetime
    global timeadd


    global run
    if run==1:
        timeadd = time.time() - basetime + timeadd
        #保存当前计时
        #print(timeadd)
        run = 0
    else:

        run = 1

    basetime = time.time()
    
def check(event):
    #定时触发更新显示
    global run
    if run == 1 :
        #s = str(time.time() - basetime + timeadd)[:10]
        a = time.time() - basetime + timeadd

        h = int(a/3600)
        if h<10:
            h = "0" + str(h)
        m = int(a%3600/60)
        if m<10:
            m = "0" + str(m)
        s = int(a%3600%60)
        if s<10:
            s = "0" + str(s)
        ms = a - int(a)
        
        s = str(h) + ":" + str(m) + ":" + str(s) + str(ms)[1:6]
        timebox.SetLabel(s)
    else:
        pass


def offer(event):
    #程序出口
    timer.Stop()
    os.remove("log.txt")#清理临时文件
    exit(0)

def reset(event):
    #复位相应
    timer.Stop()
    global run
    run = 0
    global timeadd
    timeadd = 0
    global basetime
    basetime = 0
    timebox.SetLabel("00:00:00.0000")
    timer.Start()

    
def opening():
    with open("log.txt","r") as f:
        content.SetValue(f.read())

def saveing():
    with open("log.txt","a+") as f:
        f.write(str(time.time() - basetime + timeadd)[:10])
        f.write("\n")

def cont(event):
    #计次处理
    if run ==1 :
        saveing()
        opening()
        
def clearlog(event):
    #清计数处理
    with open("log.txt","w") as f:
        f.write("")
    opening()
    
import wx
import time
import os
#状态初始化
run = 0
off = 0
timeadd = 0
basetime = 0


#创建临时文件
with open("log.txt","w") as f:
    f.write("")

app = wx.App()
#定义窗口标题，大小，初始位置
frame = wx.Frame(None,title = "Python计时器GUI",pos = (200,200),size = (320,200))

#文字
#wx.StaticText(frame,pos = (10,0),label = "计时器")
wx.StaticText(frame,pos = (10,10),label = "计时器（计次单位：秒）")

#按钮
timebox = wx.StaticText(frame,pos = (30,30),size = (100,20),label = "00:00:00.0000")
startbotton = wx.Button(frame,pos = (15,60),size=(80,30),label = "开始/暂停" )
startbotton.Bind(wx.EVT_BUTTON,switch)
resetbotton = wx.Button(frame,pos = (105,60),size=(80,30),label = "复位" )
resetbotton.Bind(wx.EVT_BUTTON,reset)
contbotton = wx.Button(frame,pos = (195,60),size=(80,30),label = "计次")
contbotton.Bind(wx.EVT_BUTTON,cont)

clearbotton = wx.Button(frame,pos = (15,100),size=(125,30),label = "清除计次")
clearbotton.Bind(wx.EVT_BUTTON,clearlog)
offbotton = wx.Button(frame,pos = (150,100),size=(125,30),label = "退出")
offbotton.Bind(wx.EVT_BUTTON,offer)

#定时器
timer = wx.Timer()
timer.Bind(wx.EVT_TIMER,check , timer)
timer.Start(2)


#计次结果窗口
frame2 = wx.Frame(None,title = "计次",pos = (520,200),size = (200,200))
content = wx.TextCtrl(frame2,pos = (0,0),size = (200,200),style = wx.TE_MULTILINE)
#加载
frame.Show()
frame2.Show()
app.MainLoop()



