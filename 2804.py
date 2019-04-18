import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="复选框和单选按钮", size=(400, 200))
        self.Center()
        panel = wx.Panel(self)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(parent=panel, label='选择你喜欢的编程语言：')
        self.cb1 = wx.CheckBox(panel, 1, 'python')
        self.cb2 = wx.CheckBox(panel, 2, 'java')
        self.cb3 = wx.CheckBox(panel, 3, 'C++')
        self.cb2.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox, id=1, id2=3)
        hbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=10)
        hbox1.Add(self.cb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(self.cb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(self.cb3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        statictext2 = wx.StaticText(panel, label='选择性别：')
        radiol = wx.RadioButton(panel, 4, '男', style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, 5, '女')

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio, id=4, id2=5)
        hbox2.Add(statictext2, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=10)
        hbox2.Add(radiol, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox2.Add(radio2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        statictext3 = wx.StaticText(panel, label='选择你喜欢吃的水果：')
        radio3 = wx.RadioButton(panel, 6, '苹果', style=wx.RB_GROUP)
        radio4 = wx.RadioButton(panel, 7, '橘子')
        radio5 = wx.RadioButton(panel, 8, '香蕉')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio2, id=6, id2=8)

        hbox3.Add(statictext3, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=10)
        hbox3.Add(radio3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3.Add(radio4, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox3.Add(radio5, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox3, 1, flag=wx.ALL | wx.EXPAND, border=5)

        panel.SetSizer(vbox)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('准备就绪')

    def on_checkbox(self, event):
        cb = event.GetEventObject()
        str = '选择了'
        if self.cb1.IsChecked():
            str += ' Python'
        if self.cb2.IsChecked():
            str += ' Java'
        if self.cb3.IsChecked():
            str += ' C++'
        if str == '选择了':
            str = '无选择'
        self.statusbar.SetStatusText(str)

    def on_radio(self, event):
        rb = event.GetEventObject()

        self.statusbar.SetStatusText('第一组 {0} 被选中'.format(rb.GetLabel()))

    def on_radio2(self, event):
        rb2 = event.GetEventObject()

        self.statusbar.SetStatusText('第二组 {0} 被选中'.format(rb2.GetLabel()))


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
