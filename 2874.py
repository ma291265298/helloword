import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='FlexGrid布局', size=(300, 200))
        self.Center()
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        flex = wx.FlexGridSizer(3, 2, 10, 10)

        title = wx.StaticText(panel, label='标题：')
        author = wx.StaticText(panel, label='作者：')
        review = wx.StaticText(panel, label='内容：')

        text1 = wx.TextCtrl(panel)
        text2 = wx.TextCtrl(panel)
        text3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        flex.AddMany([(title), (text1, 1, wx.EXPAND), (author),
                      (text2, 1, wx.EXPAND), (review, 1, wx.EXPAND), (text3, 1, wx.EXPAND)])
        flex.AddGrowableRow(2, 1)
        flex.AddGrowableCol(1, 1)
        hbox.Add(flex, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)


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
