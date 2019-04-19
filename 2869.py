import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='分隔窗口', size=(400, 200))
        self.Center()

        window = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(window)
        right = wx.Panel(window)
        window.SplitVertically(left, right, 100)

        box = wx.BoxSizer(wx.VERTICAL)
        box2 = wx.BoxSizer(wx.VERTICAL)

        fruit = ['苹果', '橘子', '香蕉']
        lb = wx.ListBox(left, 1, choices=fruit, style=wx.LB_SINGLE)

        left.SetSizer(box)
        box.Add(lb, 1, flag=wx.EXPAND | wx.ALL, border=5)

        right.SetSizer(box2)
        self.st = wx.StaticText(right, 2, label='右侧面板')
        box2.Add(self.st, 1, flag=wx.EXPAND | wx.ALL, border=5)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox, lb)

    def on_listbox(self, event):
        self.st.SetLabelText('选择 {}'.format(event.GetString()))


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('应用程序退出')
        return 0


if __name__ == '__main__':
    App = App()
    App.MainLoop()
