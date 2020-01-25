# A extensão do arquivo é .pyw
# pra poder ser executada sem o console ou seja, em background 

import wx
import wx.adv
import time
from datetime import datetime
from threading import Thread
import signal
import os
import webbrowser

ICON = 'time.ico'
ICONS = ['time.ico', 'time.ico']
X=[1,0]

HORA = "18:00"

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.thread = Thread(target=self.checkTime)
        self.thread.start()
        self.stop = False
                
        self.frame = frame
        self.toggle = 0
        wx.adv.TaskBarIcon.__init__(self)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnToggle)
        self.OnSetIcon(ICON) 
        #self.ShowBalloon('Olá Bruno', 'Seu timer foi iniciado :)')

    def CreatePopupMenu(self):
        menu = wx.Menu()
        #togglem = wx.MenuItem(menu, wx.NewId(), "self.t")
        #menu.Bind(wx.EVT_MENU, self.OnToggle, id=togglem.GetId())
        #menu.Append(togglem)
        #menu.AppendSeparator()
               
        quitm = wx.MenuItem(menu, wx.NewId(), 'Fechar')
        menu.Bind(wx.EVT_MENU, self.OnQuit, id=quitm.GetId())
        menu.Append(quitm)
        
        return menu

    #Add icon e inicia o thread do checkTimer
    def OnSetIcon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, 'Timer do Bruno')
        
    #OnClick
    def OnToggle(self, event):
        pass
        # self.toggle=X[self.toggle]
        # use_icon = ICONS[self.toggle]
        # self.OnSetIcon(use_icon)        

    def OnQuit(self, event):
        self.RemoveIcon()
        wx.CallAfter(self.Destroy)
        self.frame.Close()

        #Mata o thread
        self.stop = True
        self.thread.join()

    def checkTime(self):
        while True:
            time.sleep(1)

            now = datetime.now()
            nowTime = now.strftime("%H:%M:%S")
            self.t = nowTime
           
            # os.system('cls' if os.name=='nt' else 'clear')
            # print(nowTime)

            if HORA in nowTime:
                webbrowser.open('https://www.google.com/')
                self.stop = True
            
            if self.stop:
                return
  
if __name__ == '__main__':
    app = wx.App()
    frame=wx.Frame(None)
    TaskBarIcon(frame)
    app.MainLoop()
    
