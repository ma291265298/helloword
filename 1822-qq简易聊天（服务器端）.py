import socket, wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='qq简易聊天，服务器端', size=(500, 300))
        self.Center()
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)

        tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL, size=(500, 220))
        box1.Add(tc, flag=wx.ALL | wx.EXPAND)

        tc2 = wx.TextCtrl(panel, size=(200, -1))
        bt = wx.Button(panel, label='添加', id=1, size=(50, -1))
        box2.Add(tc2, flag=wx.ALL)
        box2.Add(bt, flag=wx.LEFT, border=30)

        vbox.Add(box1, flag=wx.ALL | wx.EXPAND)
        vbox.Add(box2, flag=wx.TOP | wx.ALIGN_CENTER, border=10)

        panel.SetSizer(vbox)


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
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind(('', 8888))
    # print('服务器启动...')
    # # 从客户端接收数据
    # data, client_address = s.recvfrom(1024)
    # print('从客户端接收消息：{0}'.format(data.decode()))
    # # 给客户端发送数据
    # s.sendto('你好！'.encode(), client_address)
    # # 释放资源
    # s.close()
