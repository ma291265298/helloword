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
        super().__init__(parent=None, title="学生信息管理系统", size=(700, 500))
        self.Center()
        panel = wx.Panel(self)
        box1 = wx.BoxSizer(wx.VERTICAL)
        box2 = wx.BoxSizer(wx.VERTICAL)
        box3 = wx.BoxSizer(wx.HORIZONTAL)
        self.grid = self.CreateGrid(self)
        tb1=wx.TextCtrl()
        box2.Add(self.grid, flag=wx.ALIGN_CENTER | wx.ALL | wx.EXPAND)
        panel.SetSizer(box2)

        # panel.Layout()
        self.Bind(wx.grid.EVT_GRID_CMD_SELECT_CELL, self.OnClick, self.grid)

    def OnClick(self, event):
        print("行号:{0}".format(event.GetRow()))
        print("列号:{0}".format(event.GetCol()))
        print(data[event.GetRow()])
        event.Skip()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.CreateGrid(len(data), len(data[0]))
        grid.SetColSize(0, 60)
        grid.SetColSize(1, 100)
        grid.SetColSize(2, 60)
        grid.SetColSize(3, 100)
        grid.SetColSize(4, 100)
        grid.SetColSize(5, 100)
        grid.SetColMinimalAcceptableWidth(60)
        for r in range(len(data)):
            for c in range(len(data[r])):
                # grid.SetRowAttr()
                # grid.SetColMinimalAcceptableWidth(50)
                grid.SetColLabelValue(c, column_names[c])
                grid.SetCellValue(r, c, str(data[r][c]))
                grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                # font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                # grid.SetCellFont(r, c, font)
        # grid.SetDefaultColSize(50)
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
    except pymysql.DatabaseError:
        print('查询失败')
        conn.rollback()
    finally:
        conn.close()
    app = App()
    app.MainLoop()
