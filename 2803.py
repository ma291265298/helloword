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

        gs = wx.GridSizer(4, 1, 0, 0)

        gs.Add(self.st, flag=wx.ALIGN_CENTER)
        gs.Add(btn1,  flag=wx.EXPAND)
        gs.Add(btn2, flag=wx.EXPAND)
        gs.Add(btn3, flag=wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self.onclick, id=1, id2=3)

        panel.SetSizer(gs)

    def onclick(self, event):
        eid = event.GetId()
        if eid == 1:
            self.st.SetLabelText('Hello World.')
        elif eid == 2:
            self.st.SetLabelText('Hello World.2')
        else:
            self.st.SetLabelText('3')


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
