import wx
import wx.adv

ICON = 'time.ico'
ICONS = ["close.ico", "time.ico"]
X=[1,0]

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        self.toggle = 0
        wx.adv.TaskBarIcon.__init__(self)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnToggle)
        self.OnSetIcon(ICON)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        togglem = wx.MenuItem(menu, wx.NewId(), 'Toggle Icon')
        menu.Bind(wx.EVT_MENU, self.OnToggle, id=togglem.GetId())
        menu.Append(togglem)
        menu.AppendSeparator()

        flashm = wx.MenuItem(menu, wx.NewId(), 'Flash Icon')
        menu.Bind(wx.EVT_MENU, self.OnTimer, id=flashm.GetId())
        menu.Append(flashm)
        menu.AppendSeparator()

        quitm = wx.MenuItem(menu, wx.NewId(), 'Quit')
    
        menu.Bind(wx.EVT_MENU, self.OnQuit, id=quitm.GetId())
        menu.Append(quitm)
        return menu

    def OnSetIcon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, path)

    def OnToggle(self, event):
        self.toggle=X[self.toggle]
        use_icon = ICONS[self.toggle]
        self.OnSetIcon(use_icon)

    def OnTimer(self,event):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnInUseTimer)
        self.timer.Start(1000)

    def OnInUseTimer(self,event):
        self.OnToggle(None)

    def OnQuit(self, event):
        self.RemoveIcon()
        wx.CallAfter(self.Destroy)
        self.frame.Close()

if __name__ == '__main__':
    app = wx.App()
    frame=wx.Frame(None)
    TaskBarIcon(frame)
    app.MainLoop()