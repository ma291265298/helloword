import wx, threading, socket, math


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Server', size=(500, 300))
        self.Center()
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.tc = wx.TextCtrl(self.panel, size=(500, 300), style=wx.HSCROLL|wx.TE_MULTILINE )

        vbox.Add(self.tc)

        self.panel.SetSizer(vbox)

        threadreceive = threading.Thread(target=self.receive)
        threadreceive.start()

    def receive(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', 8888))
        while True:
            data, self.client = self.s.recvfrom(1024)
            try:
                r = float(data.decode())
                self.tc.AppendText('Radius received from client: '+str(r)+'\n')
                area = math.pi * (r ** 2)
                self.tc.AppendText('Area is: {}'.format(area))
                self.tc.AppendText('\n')
                self.s.sendto(str(area).encode(), self.client)
                self.panel.Layout()
            except:
                self.tc.AppendText('客户端关闭发送')
                break


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
