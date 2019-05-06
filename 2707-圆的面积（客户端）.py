import wx, threading, socket


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Client', size=(500, 300))
        self.Center()
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)

        st = wx.StaticText(self.panel, label='Enter a radius:')
        self.tc = wx.TextCtrl(self.panel, size=(320, 25))
        bt = wx.Button(self.panel, label='发送', size=(80, 25), id=1)
        box1.Add(st)
        box1.Add(self.tc, flag=wx.LEFT, border=10)
        box1.Add(bt)

        self.tc2 = wx.TextCtrl(self.panel, size=(500, 220), style=wx.TE_MULTILINE | wx.HSCROLL)
        box2.Add(self.tc2, flag=wx.TOP, border=10)

        vbox.Add(box1, flag=wx.TOP, border=10)
        vbox.Add(box2)

        self.panel.SetSizer(vbox)
        bt.Bind(wx.EVT_BUTTON, self.commit)

        self.flag = False
        threadreceive = threading.Thread(target=self.receive)
        threadreceive.start()

    def receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            if self.flag:
                data, _ = self.s.recvfrom(1024)
                self.tc2.AppendText('Area received from the server is' + data.decode() + '\n')
                self.panel.Layout()

    def commit(self, event):
        address = ('127.0.0.1', 8888)
        test = self.tc.GetValue()
        try:
            ts = float(test)
            self.tc2.AppendText('Radius is ' + str(ts) + '\n')
            self.s.sendto(test.encode(), address)
        except:
            self.tc2.AppendText('输入无效' + '\n')

        self.tc.Clear()
        self.flag = True


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
