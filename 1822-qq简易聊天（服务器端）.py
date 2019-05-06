import socket, wx, threading


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='qq简易聊天，服务器端', size=(500, 300))
        self.Center()
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)

        self.tc = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.HSCROLL, size=(500, 220))
        box1.Add(self.tc, flag=wx.ALL | wx.EXPAND)

        self.tc2 = wx.TextCtrl(self.panel, size=(200, -1))
        bt = wx.Button(self.panel, label='发送', id=1, size=(50, -1))
        box2.Add(self.tc2, flag=wx.ALL)
        box2.Add(bt, flag=wx.LEFT, border=30)

        vbox.Add(box1, flag=wx.ALL | wx.EXPAND)
        vbox.Add(box2, flag=wx.TOP | wx.ALIGN_CENTER, border=10)

        self.panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.commit, id=1)

        threadreceive = threading.Thread(target=self.receive)
        threadreceive.start()

    def receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', 8888))
        while True:
            data, self.client = self.s.recvfrom(1024)
            if data.decode() == '退出':
                self.tc.AppendText('客户端关闭发送')
                break
            self.tc.AppendText('客户端 对 服务端 说：' + data.decode() + '\n')
            self.panel.Layout()

    def commit(self, event):
        test = self.tc2.GetValue()
        self.s.sendto(test.encode(), self.client)
        self.tc2.Clear()


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
