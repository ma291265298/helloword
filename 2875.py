import wx
import wx.grid

data = [['0036', '高等数学', '李放', '人民邮电出版社', '20000812', '1'],
        ['0004', 'FLASH精选', '刘杨', '中国纺织出版社', '19990312', '2'],
        ['0026', '软件工程', '牛田', '经济科学出版社', '20000328', '4'],
        ['0015', '人工智能', '周末', '机械工业出版社', '19991223', '3']]

column_names = ['书籍编号', '书籍名称', '作者', '出版社', '出版日期', '库存数量']


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="网格控件", size=(550, 200))
        self.Center()
        self.grid = self.CreateGrid(self)
        self.Bind(wx.grid.EVT_GRID_CMD_SELECT_CELL, self.OnClick, self.grid)

    def OnClick(self, event):
        print("行号:{0}".format(event.GetRow()))
        print("列号:{0}".format(event.GetCol()))
        print(data[event.GetRow()])
        event.Skip()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.CreateGrid(len(data), len(data[0]))
        for r in range(len(data)):
            for c in range(len(data[r])):
                grid.SetColLabelValue(c, column_names[c])
                grid.SetCellValue(r, c, data[r][c])
                grid.SetCellAlignment(r, c, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
                font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False)
                grid.SetCellFont(r, c, font)
                if r % 2 == 0:
                    grid.SetCellBackgroundColour(r, c, "SEA green")
                else:
                    grid.SetCellBackgroundColour(r, c, "SLATE blue")
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
    app = App()
    app.MainLoop()
