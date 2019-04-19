import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="列表", size=(400, 200))
        self.Center()
        panel = wx.Panel(parent=self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)

        st = wx.StaticText(panel, label='选择你喜欢的编程语言：')
        language = ['Python', 'C++', "Java"]
        lb1 = wx.ListBox(panel, -1, choices=language, style=wx.LB_SINGLE)

        box.Add(st, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        box.Add(lb1, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)

        st2 = wx.StaticText(panel, label='选择你喜欢吃的水果：')
        fruit = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(panel, -1, choices=fruit, style=wx.LB_EXTENDED | wx.LB_SORT)

        box2.Add(st2, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        box2.Add(lb2, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(box, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(box2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(vbox)


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
