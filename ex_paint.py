import wx
import time
import numpy as np

class DrawPanel(wx.Frame):

    def __init__(self, parent):
        self.TIMER_PLAY_ID = 101
        wx.Frame.__init__(self, parent, title="Draw on Panel")
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.playTimer = wx.Timer(self, self.TIMER_PLAY_ID)
        wx.EVT_TIMER(self, self.TIMER_PLAY_ID, self.OnPaint)
        self.playTimer.Start(10)

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        #dc.SetPen(wx.Pen(wx.BLACK, 4))
        #dc.DrawLine(0, 0, 50, 50)
        xpos = int(20*np.cos(time.time())+20)
        ypos = int(20*np.sin(time.time())+20)
        dc.DrawText('this is a test', xpos, ypos)


app = wx.App(False)
frame = DrawPanel(None)
frame.Show()
app.MainLoop()



