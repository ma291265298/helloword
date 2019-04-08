import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="网格控件", size=(400, 300))
        self.Center()
        panel = wx.Panel(parent=self)
        text = wx.StaticText(panel, wx.ID_ANY, "居中对齐", (-1, -1), (400, -1), style=wx.ALIGN_CENTER)


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
