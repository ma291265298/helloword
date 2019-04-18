import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title='下拉列表', size=(400, 200))
        self.Center()
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)

        cblbl = wx.StaticText(panel, label="选择你喜欢的编程语言：", style=wx.ALL)

        languages = ['C', 'C++', 'Python', 'Java']
        self.combo = wx.ComboBox(panel, choices=languages)
        self.combo.SetLabelText('C++')
        box1.Add(cblbl, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        box1.Add(self.combo, proportion=1, flag=wx.ALL, border=5)

        box2 = wx.BoxSizer(wx.HORIZONTAL)
        chlbl = wx.StaticText(panel, label="选择性别：", style=wx.ALL)
        sexs = ['男', '女']
        self.choice = wx.Choice(panel, -1, choices=sexs)
        self.choice.SetSelection(0)
        box2.Add(chlbl, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        box2.Add(self.choice, proportion=1, flag=wx.ALL, border=5)

        box.Add(box1, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        box.Add(box2, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)

        box.AddStretchSpacer()
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)

        panel.SetSizer(box)

        self.Show()
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('准备就绪')

    def OnCombo(self, event):
        self.statusbar.SetStatusText('选择 {}'.format(self.combo.GetValue()))

    def OnChoice(self, event):
        if self.choice.GetSelection() == 0:
            self.statusbar.SetStatusText('选择 男')
        else:
            self.statusbar.SetStatusText('选择 女')


app = wx.App()
Mywin(None, 'ComboBox and Choice demo')
app.MainLoop()
