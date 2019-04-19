import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态文本和按钮', size=(300, 250))
        self.Center()
        panel = wx.Panel(self)
        self.st = wx.StaticText(panel, 0, label='StaticText1', style=wx.ALIGN_CENTER)
        btn1 = wx.Button(panel, label='ok', id=1)
        btn2 = wx.Button(panel, label='ToggleButton', id=2)
        pic = wx.Image('test.jpg', wx.BITMAP_TYPE_JPEG).Rescale(40, 40).ConvertToBitmap()
        btn3 = wx.BitmapButton(panel, 3, pic)

        gs = wx.GridSizer(1, 1, 0, 0)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.st, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER, border=20)
        box.Add(btn1, proportion=1, flag=wx.EXPAND | wx.ALL)
        box.Add(btn2, proportion=1, flag=wx.EXPAND | wx.ALL)
        box.Add(btn3, proportion=2, flag=wx.EXPAND | wx.ALL)

        gs.Add(box, flag=wx.EXPAND | wx.ALL)

        self.Bind(wx.EVT_BUTTON, self.onclick, id=1, id2=3)

        panel.SetSizer(gs)

    def onclick(self, event):
        eid = event.GetId()
        if eid == 1:
            self.st.SetLabelText('Hello World.')
        elif eid == 2:
            self.st.SetLabelText('Hello World.2')
        else:
            self.st.SetLabelText('Hello World.3')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('应用程序退出')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
