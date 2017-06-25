# -*- coding: utf-8 -*-


import wx
from wx.lib.pubsub import pub
class MainWindow(wx.Frame):
 def __init__(self, parent):
  wx.Frame.__init__(self, parent, title="Tomedit")
  self.initUi()
  self.bindEvents()
  self.setDefaultValues()
  self.Maximize(True)
 def initUi(self):
  self.ctrls={}
  self.staticBoxCtrls = {}
  self.volumeMethodCtrls={}
  panel = wx.Panel(self)
  sizer = wx.BoxSizer(wx.VERTICAL)

  self.ctrls['listLabel'] = wx.StaticText(panel, label='pliki')
  self.ctrls['list'] = wx.ListView(panel)
  self.ctrls['list'].InsertColumn(0, 'nazwa pliku')
  self.ctrls['list'].InsertColumn(1, 'ścieżka')
  self.ctrls['addFile'] = wx.Button(panel, label='dodaj plik')
  self.ctrls['addFolder'] = wx.Button(panel, label='dodaj folder')
  self.ctrls['subFolders'] = wx.CheckBox(panel,label='uwzględniaj podfoldery')
  self.ctrls['fadein'] = wx.CheckBox(panel,label='Łagodny start')
  self.ctrls['fadeinLabel'] = wx.StaticText(panel, label='Ms')
  self.ctrls['fadeinValue'] = wx.SpinCtrl(panel, value='0', min=0, max=20000)
  self.ctrls['fadeout'] = wx.CheckBox(panel,label='Łagodne zciszenie')
  self.ctrls['fadeoutLabel'] = wx.StaticText(panel, label='Ms')
  self.ctrls['fadeoutValue'] = wx.SpinCtrl(panel, value='0', min=0, max=20000)
  self.ctrls['changeVolume'] = wx.CheckBox(panel,label='Zmień głośność')
  self.staticBoxCtrls['volumeChangeGroup'] = wx.StaticBox( panel, -1, "Zmiana głośności" )
  self.ctrls['staticBoxSizer'] = wx.StaticBoxSizer(self.staticBoxCtrls['volumeChangeGroup'], wx.VERTICAL)
  self.staticBoxCtrls['volumeMethodManual'] = wx.RadioButton( panel, -1, " Ręcznie ", style = wx.RB_GROUP )
  self.staticBoxCtrls['volumeMethodAuto'] = wx.RadioButton( panel, -1, " Automatycznie " )

  self.staticBoxCtrls['volumeLabel'] = wx.StaticText(panel, label='DB')

  self.staticBoxCtrls['volumeValue'] = wx.SpinCtrl(panel, value='0', min=-140, max=140)

  self.ctrls['limiter'] = wx.CheckBox(panel,label='nie dopuszczaj do przesterowania')
  self.ctrls['swapChannels'] = wx.CheckBox(panel,label='Zamień kanały')
  self.ctrls['start'] = wx.Button(panel, label='Start')
  self.volumeMethodCtrls['volumeMethodAuto'] = self.staticBoxCtrls['volumeMethodAuto']
  self.volumeMethodCtrls['volumeMethodManual'] = self.staticBoxCtrls['volumeMethodManual']

  for ctrl in self.staticBoxCtrls.iterkeys():
   if ctrl != 'volumeChangeGroup': self.ctrls['staticBoxSizer'].Add(self.staticBoxCtrls[ctrl])

  for ctrl in self.ctrls.itervalues():
   sizer.Add(ctrl)
  for ctrl in self.staticBoxCtrls.iterkeys():
   self.ctrls[ctrl] = self.staticBoxCtrls[ctrl]

  panel.SetSizerAndFit(sizer)

 def bindEvents(self):
  self.ctrls['addFile'].Bind(wx.EVT_BUTTON, self.onAddFile)

  self.ctrls['fadein'].Bind(wx.EVT_CHECKBOX, self.onFadein)
  self.ctrls['fadeout'].Bind(wx.EVT_CHECKBOX, self.onFadeout)
  self.ctrls['changeVolume'].Bind(wx.EVT_CHECKBOX, self.onChangeVolume)
  self.ctrls['volumeMethodManual'].Bind(wx.EVT_RADIOBUTTON, self.onManual)
  self.ctrls['volumeMethodAuto'].Bind(wx.EVT_RADIOBUTTON, self.onAuto)


 def onFadein(self, e):
  checkbox = e.GetEventObject()
  self.ctrls['fadeinValue'].Enable(checkbox.GetValue())

 def onFadeout(self, e):
  checkbox = e.GetEventObject()
  self.ctrls['fadeoutValue'].Enable(checkbox.GetValue())

 def onChangeVolume(self, e):
  checkbox = e.GetEventObject()
  for ctrl in self.staticBoxCtrls.itervalues():
   ctrl.Enable(checkbox.GetValue())

 def onManual(self, e):
  self.ctrls['volumeValue'].Enable(True)

 def onAuto(self, e):
  self.ctrls['volumeValue'].Enable(False)


 def onAddFile(self, e):
  dlg = wx.FileDialog(self)
  if dlg.ShowModal() == wx.ID_OK:
   self.ctrls['list'].Append([dlg.GetPath()])

 def setDefaultValues(self):
  self.ctrls['fadeinValue'].Enable(self.ctrls['fadein'].GetValue())
  self.ctrls['fadeoutValue'].Enable(self.ctrls['fadeout'].GetValue())
  for ctrl in self.staticBoxCtrls.itervalues():
   ctrl.Enable(self.ctrls['changeVolume'].GetValue())

class Controller:
 def __init__(self, app):
  self.mainWindow = MainWindow(None)
  self.mainWindow.Show(True)

if __name__=='__main__':
 app = wx.App(False)
 controller = Controller(app)
 app.MainLoop()