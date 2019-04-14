import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Box布局', size=(400, 250))
        self.Center()
        panel = wx.Panel(self)
        self.st = wx.StaticText(panel, label='Hello', pos=(100, 80))
        btn1 = wx.Button(panel, label='Button1', id=1)
        btn2 = wx.Button(panel, label='Button2', id=2)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(btn1, flag=wx.EXPAND)
        hbox.Add(btn2, flag=wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.onclick, id=1, id2=2)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.st, 3,
                 flag=wx.FIXED_MINSIZE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,
                 border=10)
        vbox.Add(hbox, 2,
                 flag=wx.FIXED_MINSIZE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,
                 border=20)
        panel.SetSizer(vbox)

    def onclick(self, event):
        eid = event.GetId()
        if eid == 1:
            self.st.SetLabelText('Button1单击')
        else:
            self.st.SetLabelText('Button2单击')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
