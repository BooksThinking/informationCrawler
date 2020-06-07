import wx
import initData

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        panel = wx.Panel(self)

        self.static_text = wx.StaticText(panel, label="爬虫", pos=(10, 10))

        self.text_1 = wx.TextCtrl(panel, value="贴吧名称", pos=(10, 40))
        self.text_2 = wx.TextCtrl(panel, value="起始页码", pos=(10, 70))
        self.text_3 = wx.TextCtrl(panel, value="停止页码", pos=(10, 100))

        self.btn1 = wx.Button(panel, label="开始爬虫", pos=(200, 10))

        self.Bind(wx.EVT_BUTTON, self.OnButton1, self.btn1)

    def OnButton1(self, event):
        initData.init_data(self.text_1.GetValue(),int(self.text_2.GetValue()),int(self.text_3.GetValue()))
        # print(self.text_1.GetValue())
        # print(int(self.text_2.GetValue()))
        # print(int(self.text_3.GetValue()))
    # def OnButton2(self, event):
    #     self.static_text.Label += 'Hi'
    # def OnButton3(self, event):
    #     self.text_1.Value = 'Good'
    #     self.text_2.Value = 'GOOD'
    #     self.text_3.Value = 'Good\nbetter\nbest'
    #     self.text_4.Value = 'GOOD\nBetter\nBest'
    # def OnText1(self, event):
    #     self.text_3.Value = self.text_1.Value

app = wx.App()
frame = MyFrame(None, title="Multi_Text", size=(500, 300))
frame.Show()
app.MainLoop()