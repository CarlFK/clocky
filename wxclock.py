#!/usr/bin/python
# create nice Analog Clock using wxPython
# tested with Python24 and wxPython26  by  HAB
# sweep hand added by David Goodger

import wx
import analogclock as ac

class MyFrame(wx.Dialog):

    """use simple dialog box as frame"""

    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, -1, title, size=(800,600),
                           style=wx.DEFAULT_FRAME_STYLE)

        clock = ac.AnalogClock(
            self,
            clockStyle=(  ac.SHOW_HOURS_TICKS
                        | ac.SHOW_MINUTES_TICKS
                        | ac.SHOW_HOURS_HAND
                        | ac.SHOW_MINUTES_HAND
                        | ac.SHOW_SECONDS_HAND
                        | ac.SHOW_SWEEP_HAND),
            minutesStyle=ac.TICKS_CIRCLE,
            hoursStyle=ac.TICKS_DECIMAL,
            # sweep hand RPM:
            sweep_frequency=12,
            # milliseconds; 20ms == 50 updates/second:
            timer_interval=10)

        clock.SetHandSize(2, target=ac.SWEEP)
        clock.SetHandFillColour("black", target=ac.SWEEP)
        clock.SetHandBorderColour("red", target=ac.SWEEP)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(clock, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 10)

        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()

        self.ShowModal()
        self.Destroy()


app = wx.PySimpleApp()
frame = MyFrame(None, -1, "wx Analog Clock with Sweep Hand")
# show the frame
frame.Show(True)
print frame.GetHandle()
# start the event loop
app.MainLoop()
