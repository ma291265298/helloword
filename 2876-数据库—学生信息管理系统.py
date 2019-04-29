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
        self.panel = wx.Panel(self)
        self.row = 0
        self.sedata = []
        vbox = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box3 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(self.panel, label='请输入姓名：')
        self.tc1 = wx.TextCtrl(self.panel)
        bt1 = wx.Button(self.panel, label='查询', id=1)
        box1.Add(st1, flag=wx.ALIGN_CENTER | wx.ALL, border=20)
        box1.Add(self.tc1, flag=wx.ALIGN_CENTER | wx.ALL, border=15)
        box1.Add(bt1, flag=wx.ALIGN_CENTER | wx.ALL, border=15)

        self.grid = self.CreateGrid(self.panel)
        box2.Add(self.grid, flag=wx.ALIGN_CENTER | wx.ALL)

        add = wx.Button(self.panel, label='添加', id=2)
        edit = wx.Button(self.panel, label='修改', id=3)
        delete = wx.Button(self.panel, label='删除', id=4)
        box3.Add(add, flag=wx.ALIGN_CENTER | wx.ALL, proportion=1, border=10)
        box3.Add(edit, flag=wx.ALIGN_CENTER | wx.ALL, proportion=1, border=10)
        box3.Add(delete, flag=wx.ALIGN_CENTER | wx.ALL, proportion=1, border=10)

        vbox.Add(box1, 0, flag=wx.ALIGN_CENTER)
        vbox.Add(box2, 1, flag=wx.ALIGN_CENTER | wx.BOTTOM)
        vbox.Add(box3, 0, flag=wx.ALIGN_CENTER | wx.ALL, border=15)

        self.panel.SetSizer(vbox)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('准备就绪')
        # panel.Layout()
        self.Bind(wx.grid.EVT_GRID_CMD_SELECT_CELL, self.OnClick, self.grid)
        self.Bind(wx.EVT_BUTTON, self.select, id=1)
        self.Bind(wx.EVT_BUTTON, self.add, id=2)
        # self.Bind(wx.EVT_BUTTON, self.edit, id=3)
        self.Bind(wx.EVT_BUTTON, self.delete1, id=4)

    def select(self, event):
        name = self.tc1.GetValue()
        if name != '':
            try:
                with conn.cursor() as cursor:
                    sql = "select * from student where name='{}'".format(name)
                    print(sql)
                    cursor.execute(sql)
                    conn.commit()
                    # data2=cursor.fetchall()
                    # print(cursor.fetchall())

                    data2 = list(cursor.fetchall())

                    # data = list(data)
                    print(data2)
                    for i in range(self.grid.GetNumberRows()):
                        self.grid.DeleteRows()
                    for i in range(len(data2)):
                        self.grid.InsertRows()
                    for r in range(len(data2)):
                        self.grid.SetRowSize(r, 50)
                        for c in range(len(data2[r])):
                            # self.grid.SetColLabelValue(c, column_names[c])
                            # print(data2[r][c])
                            self.grid.SetCellValue(r, c, str(data2[r][c]))
                            self.grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                            font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                            self.grid.SetCellFont(r, c, font)

                    # self.grid.InsertRows(data)

                    # print(data)
                    print('查询成功')
            except pymysql.DatabaseError:
                print('查询失败')
                conn.rollback()
        else:
            try:
                with conn.cursor() as cursor:
                    sql = 'select * from student '
                    print(sql)
                    cursor.execute(sql)
                    conn.commit()
                    data2 = list(cursor.fetchall())
                    print(data2)
                    for i in range(self.grid.GetNumberRows()):
                        self.grid.DeleteRows()
                    for i in range(len(data2)):
                        self.grid.InsertRows()
                    for r in range(len(data2)):
                        self.grid.SetRowSize(r, 50)
                        for c in range(len(data2[r])):
                            # print(data2[r][c])
                            self.grid.SetCellValue(r, c, str(data2[r][c]))
                            self.grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                            font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                            self.grid.SetCellFont(r, c, font)
                    print('查询成功')
            except pymysql.DatabaseError:
                print('查询失败')
                conn.rollback()

    def add(self, event):
        self.frame2 = MyFrame2(parent=self.panel)
        self.frame2.ShowModal()
        print(self.frame2.Getflag())
        if not self.frame2.Getflag():
            try:
                with conn.cursor() as cursor:
                    sql = 'select * from student '
                    print(sql)
                    cursor.execute(sql)
                    conn.commit()
                    data2 = list(cursor.fetchall())
                    for i in range(self.grid.GetNumberRows()):
                        self.grid.DeleteRows()
                    for i in range(len(data2)):
                        self.grid.InsertRows()
                    for r in range(len(data2)):
                        self.grid.SetRowSize(r, 50)
                        for c in range(len(data2[r])):
                            self.grid.SetCellValue(r, c, str(data2[r][c]))
                            self.grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                            font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                            self.grid.SetCellFont(r, c, font)
                    print('查询成功')
            except pymysql.DatabaseError:
                print('查询失败')
                conn.rollback()


    def delete1(self, event):
        print(self.sedata)
        try:
            with conn.cursor() as cursor:
                sql = 'delete from student where number=%s and name=%s and sex=%s ' \
                      'and math=%s and english=%s and computer=%s'
                print(sql, self.sedata)
                cursor.execute(sql, self.sedata)
                conn.commit()
                print('删除成功')
                # print(self.row)
                self.grid.DeleteRows(self.row)
                self.panel.Layout()
        except pymysql.DatabaseError:
            print('删除失败')
            conn.rollback()

    def OnClick(self, event):
        print("行号:{0}".format(event.GetRow()))
        print("列号:{0}".format(event.GetCol()))
        print(data[event.GetRow()])
        self.row = event.GetRow()
        self.sedata=[]
        for i in range(self.grid.GetNumberCols()):
          self.sedata.append(self.grid.GetTable().GetValue(event.GetRow(), i))
        # self.sedata = data[event.GetRow()]
        print(self.sedata)
        event.Skip()

    def CreateGrid(self, parent):
        # pp = wx.Panel(parent)
        # grid = wx.grid.Grid(pp)
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
                # grid.SetColLabelValue(c, column_names[c])
                grid.SetCellValue(r, c, str(data[r][c]))
                grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                grid.SetCellFont(r, c, font)
        grid.AutoSize()
        # pp.SetSizer(grid)
        return grid


class MyFrame2(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(300, 500))
        self.SetTitle('添加')
        self.Center()
        self.flag = False
        panel2 = wx.Panel(self)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        btbox = wx.BoxSizer(wx.HORIZONTAL)

        stnnumber = wx.StaticText(panel2, label='学号：')
        self.tcnumber = wx.TextCtrl(panel2)

        stname = wx.StaticText(panel2, label='姓名：')
        self.tcname = wx.TextCtrl(panel2)

        stsex = wx.StaticText(panel2, label='性别：')
        self.tcsex = wx.TextCtrl(panel2)

        stmath = wx.StaticText(panel2, label='数学：')
        self.tcmath = wx.TextCtrl(panel2)

        steng = wx.StaticText(panel2, label='英语：')
        self.tceng = wx.TextCtrl(panel2)

        stcom = wx.StaticText(panel2, label='计算机：')
        self.tccom = wx.TextCtrl(panel2)

        add = wx.Button(panel2, label='添加', id=11)
        canel = wx.Button(panel2, label='取消', id=12)
        btbox.Add(add, flag=wx.ALIGN_CENTER | wx.RIGHT, border=20)
        btbox.Add(canel, flag=wx.ALIGN_CENTER | wx.LEFT, border=20)

        fg = wx.FlexGridSizer(6, 2, 40, 30)
        fg.AddMany([
            stnnumber, (self.tcnumber, 3, wx.EXPAND),
            stname, (self.tcname, 1, wx.EXPAND),
            stsex, (self.tcsex, 1, wx.EXPAND),
            stmath, (self.tcmath, 1, wx.EXPAND),
            steng, (self.tceng, 1, wx.EXPAND),
            stcom, (self.tccom, 1, wx.EXPAND),
        ])
        fg.AddGrowableCol(0, 1)
        fg.AddGrowableCol(1, 30)
        vbox2.Add(fg, 1, flag=wx.ALL | wx.ALIGN_CENTER, border=20)

        vbox2.Add(btbox, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        panel2.SetSizer(vbox2)

        self.Bind(wx.EVT_BUTTON, self.confirm, id=11)
        self.Bind(wx.EVT_BUTTON, self.canel, id=12)

    def confirm(self, event):
        addata = []
        addata.append(self.tcnumber.GetValue())
        addata.append(self.tcname.GetValue())
        addata.append(self.tcsex.GetValue())
        addata.append(float(self.tcmath.GetValue()))
        addata.append(float(self.tceng.GetValue()))
        addata.append(float(self.tccom.GetValue()))
        try:
            with conn.cursor() as cursor:
                sql = 'insert into student values (%s,%s,%s,%s,%s,%s)'
                print(sql, addata)
                cursor.execute(sql, addata)
                conn.commit()
                print('添加成功')
                self.Close()

        except pymysql.DatabaseError:
            print('添加失败')
            conn.rollback()
        print(addata)

    def canel(self, event):
        self.flag = True
        self.Close()
    def Getflag(self):
        return self.flag

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
