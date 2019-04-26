import wx
import wx.grid
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    db='python_student'
)

column_names = ['学号', '姓名', '性别', '数学', '英语', '计算机']


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="学生信息管理系统", size=(700, 550))
        self.Center()
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box3 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='请输入姓名：')
        self.tc1 = wx.TextCtrl(panel)
        bt1 = wx.Button(panel, label='查询', id=1)
        box1.Add(st1, flag=wx.ALIGN_CENTER | wx.ALL, border=20)
        box1.Add(self.tc1, flag=wx.ALIGN_CENTER | wx.ALL, border=15)
        box1.Add(bt1, flag=wx.ALIGN_CENTER | wx.ALL, border=15)

        self.grid = self.CreateGrid(panel)
        box2.Add(self.grid, flag=wx.ALIGN_CENTER | wx.ALL)

        add = wx.Button(panel, label='添加')
        edit = wx.Button(panel, label='修改')
        delete = wx.Button(panel, label='删除')
        box3.Add(add, flag=wx.ALIGN_CENTER | wx.ALL, proportion=1)
        box3.Add(edit, flag=wx.ALIGN_CENTER | wx.ALL, proportion=1)
        box3.Add(delete, flag=wx.ALIGN_CENTER | wx.ALL, proportion=1)

        hbox.Add(box1, flag=wx.ALIGN_CENTER, proportion=1)
        hbox.Add(box2, flag=wx.ALIGN_CENTER | wx.BOTTOM, proportion=1)
        hbox.Add(box3, flag=wx.ALIGN_CENTER | wx.BOTTOM, proportion=10)

        panel.SetSizer(hbox)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('准备就绪')
        # panel.Layout()
        # self.Bind(wx.grid.EVT_GRID_CMD_SELECT_CELL, self.OnClick, self.grid)
        self.Bind(wx.EVT_BUTTON, self.select, id=1)

    def select(self, event):
        name = self.tc1.GetValue()
        try:
            with conn.cursor() as cursor:
                sql = "select * from student where name='{}'".format(name)
                print(sql)
                cursor.execute(sql)
                conn.commit()
                print(cursor.fetchall())
                data = cursor.fetchall()
                data = list(data)
                self.grid.Refresh()
                print(data)
                print('查询成功')
        except pymysql.DatabaseError:
            print('查询失败')
            conn.rollback()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.CreateGrid(len(data), len(data[0]))
        grid.SetColSize(0, 70)
        grid.SetColSize(1, 110)
        grid.SetColSize(2, 70)
        grid.SetColSize(3, 110)
        grid.SetColSize(4, 110)
        grid.SetColSize(5, 110)
        grid.SetColMinimalAcceptableWidth(80)
        grid.SetRowMinimalAcceptableHeight(50)
        for r in range(len(data)):
            grid.SetRowSize(r, 50)
            for c in range(len(data[r])):
                grid.SetColLabelValue(c, column_names[c])
                grid.SetCellValue(r, c, str(data[r][c]))
                grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                grid.SetCellFont(r, c, font)
        grid.AutoSize()
        return grid




class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    try:
        with conn.cursor() as cursor:
            sql = 'select * from student'

            cursor.execute(sql)
            conn.commit()

            data = cursor.fetchall()
            data = list(data)
            print(data)
            print('查询成功')
            app = App()
            app.MainLoop()
    except pymysql.DatabaseError:
        print('查询失败')
        conn.rollback()
    finally:
        conn.close()

