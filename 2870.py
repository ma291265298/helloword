import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="树控件", size=(500, 400))
        self.Center()
        window = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(parent=window)
        right = wx.Panel(parent=window)
        window.SplitVertically(left, right, 200)
        window.SetMinimumPaneSize(80)

        self.tree = self.CreateTreeCtrl(left)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_click, self.tree)

        box = wx.BoxSizer(wx.VERTICAL)
        left.SetSizer(box)
        box.Add(self.tree, 1, flag=wx.EXPAND | wx.ALL, border=5)

        box2 = wx.BoxSizer(wx.VERTICAL)
        right.SetSizer(box2)
        self.st = wx.StaticText(right, 2, label='右侧面板')
        box2.Add(self.st, 1, flag=wx.EXPAND | wx.ALL, border=5)

    def on_click(self, event):
        item = event.GetItem()
        self.st.SetLabel(self.tree.GetItemText(item))

    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot('TreeRoot', image=0)
        item1 = tree.AppendItem(root, 'Item1', 0)
        item2 = tree.AppendItem(root, 'Item2', 0)
        item3 = tree.AppendItem(root, 'Item3', 0)
        item4 = tree.AppendItem(root, 'Item4', 0)
        item5 = tree.AppendItem(root, 'Item5', 0)
        tree.Expand(root)
        tree.SelectItem(root)

        for i in range(5):
            str1 = 'Subitem ' + str(i + 1)
            tree.AppendItem(item1, str1, 1)
        tree.Expand(item1)

        for i in range(5):
            str1 = 'Subitem ' + str(i + 1)
            tree.AppendItem(item2, str1, 1)

        for i in range(5):
            str1 = 'Subitem ' + str(i + 1)
            tree.AppendItem(item3, str1, 1)

        for i in range(5):
            str1 = 'Subitem ' + str(i + 1)
            tree.AppendItem(item4, str1, 1)
        tree.Expand(item4)

        for i in range(5):
            str1 = 'Subitem ' + str(i + 1)
            tree.AppendItem(item5, str1, 1)

        return tree


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
