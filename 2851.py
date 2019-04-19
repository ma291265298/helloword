import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='静态图片控件', size=(300, 350))
        self.Center()
        self.panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        bt1 = wx.Button(self.panel, label='Button1', id=1)
        bt2 = wx.Button(self.panel, label='Button2', id=2)


        self.bmps = [
            wx.Image('pic1.jpg', wx.BITMAP_TYPE_JPEG).Rescale(180, 100).ConvertToBitmap(),
            wx.Image('pic2.jpg', wx.BITMAP_TYPE_JPEG).Rescale(180, 100).ConvertToBitmap(),
            wx.Image('pic3.jpg', wx.BITMAP_TYPE_JPEG).Rescale(180, 100).ConvertToBitmap()
        ]
        self.image = wx.StaticBitmap(self.panel, -1, self.bmps[0], size=(180, 100))
        box.Add(bt1, proportion=1, flag=wx.ALL | wx.EXPAND)
        box.Add(bt2, proportion=1, flag=wx.ALL | wx.EXPAND)

        box.Add(self.image, proportion=3, flag=wx.CENTER)
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)
        self.panel.SetSizer(box)


    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])

        else:
            self.image.SetBitmap(self.bmps[2])
        self.panel.Layout()


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
