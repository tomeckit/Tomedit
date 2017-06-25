
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
  self.volumeboxctrls = {}
  self.volumeMethodCtrls={}
  self.toneboxctrls={}
  panel = wx.Panel(self)
  sizer = wx.BoxSizer(wx.VERTICAL)

  self.ctrls['listLabel'] = wx.StaticText(panel, label='pliki')
  self.ctrls['list'] = wx.ListView(panel)
  self.ctrls['list'].InsertColumn(0, 'nazwa pliku')
  self.ctrls['list'].InsertColumn(1, 'ścieżka')
  self.ctrls['listLabel'] = wx.StaticText(panel, label='pliki')

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
  self.volumeboxctrls['volumeChangeGroup'] = wx.StaticBox( panel, -1, "Zmiana głośności" )
  self.ctrls['volumeBoxSizer'] = wx.StaticBoxSizer(self.volumeboxctrls['volumeChangeGroup'], wx.VERTICAL)
  self.volumeboxctrls['volumeMethodManual'] = wx.RadioButton( panel, -1, " Ręcznie ", style = wx.RB_GROUP )
  self.volumeboxctrls['volumeMethodAuto'] = wx.RadioButton( panel, -1, " Automatycznie " )
  self.volumeboxctrls['volumeLabel'] = wx.StaticText(panel, label='DB')
  self.volumeboxctrls['volumeValue'] = wx.SpinCtrl(panel, value='0', min=-140, max=140)
  self.ctrls['limiter'] = wx.CheckBox(panel,label='nie dopuszczaj do przesterowania')

  self.ctrls['swapChannels'] = wx.CheckBox(panel,label='Zamień kanały')

  self.ctrls['changeTone'] = wx.CheckBox(panel,label='Zmień barwę')
  self.toneboxctrls['toneChangeGroup'] = wx.StaticBox( panel, -1, "Zmiana barwy" )
  self.ctrls['toneBoxSizer'] = wx.StaticBoxSizer(self.toneboxctrls['toneChangeGroup'], wx.VERTICAL)
  self.toneboxctrls['toneloLabel'] = wx.StaticText(panel, label='Bas')
  self.toneboxctrls['toneloValue'] = wx.SpinCtrl(panel, value='0', min=-12, max=12)
  self.toneboxctrls['tonehiLabel'] = wx.StaticText(panel, label='Góra')
  self.toneboxctrls['tonehiValue'] = wx.SpinCtrl(panel, value='0', min=-12, max=12)
  self.ctrls['convert'] = wx.CheckBox(panel,label='Konwertuj')
  self.formats = ['mp3', 'ogg', 'flac', 'wma', 'aac LC', 'mpc', 'opus']
  self.ctrls['convertlistLabel'] = wx.StaticText(panel, label='Konwertuj do')
  self.ctrls['convertList'] = wx.Choice(panel, choices =self.formats)

  self.ctrls['start'] = wx.Button(panel, label='Start')
  self.volumeMethodCtrls['volumeMethodAuto'] = self.volumeboxctrls['volumeMethodAuto']
  self.volumeMethodCtrls['volumeMethodManual'] = self.volumeboxctrls['volumeMethodManual']

  for ctrl in self.volumeboxctrls.iterkeys():
   if ctrl != 'volumeChangeGroup': self.ctrls['volumeBoxSizer'].Add(self.volumeboxctrls[ctrl])

  for ctrl in self.toneboxctrls.iterkeys():
   if ctrl != 'toneChangeGroup': self.ctrls['toneBoxSizer'].Add(self.toneboxctrls[ctrl])

  for ctrl in self.ctrls.itervalues():
   sizer.Add(ctrl)
  for ctrl in self.volumeboxctrls.iterkeys():
   self.ctrls[ctrl] = self.volumeboxctrls[ctrl]
  for ctrl in self.toneboxctrls.iterkeys():
   self.ctrls[ctrl] = self.toneboxctrls[ctrl]


  panel.SetSizerAndFit(sizer)

 def bindEvents(self):
  self.ctrls['addFile'].Bind(wx.EVT_BUTTON, self.onAddFile)

  self.ctrls['fadein'].Bind(wx.EVT_CHECKBOX, self.onFadein)
  self.ctrls['fadeout'].Bind(wx.EVT_CHECKBOX, self.onFadeout)
  self.ctrls['changeVolume'].Bind(wx.EVT_CHECKBOX, self.onChangeVolume)
  self.ctrls['volumeMethodManual'].Bind(wx.EVT_RADIOBUTTON, self.onManual)
  self.ctrls['volumeMethodAuto'].Bind(wx.EVT_RADIOBUTTON, self.onAuto)
  self.ctrls['changeTone'].Bind(wx.EVT_CHECKBOX, self.onChangeTone)
  self.ctrls['convert'].Bind(wx.EVT_CHECKBOX, self.onconvert)

 def onFadein(self, e):
  checkbox = e.GetEventObject()
  self.ctrls['fadeinValue'].Enable(checkbox.GetValue())

 def onFadeout(self, e):
  checkbox = e.GetEventObject()
  self.ctrls['fadeoutValue'].Enable(checkbox.GetValue())

 def onChangeVolume(self, e):
  checkbox = e.GetEventObject()
  for ctrl in self.volumeboxctrls.itervalues():
   ctrl.Enable(checkbox.GetValue())

 def onManual(self, e):
  self.ctrls['volumeValue'].Enable(True)

 def onAuto(self, e):
  self.ctrls['volumeValue'].Enable(False)

 def onChangeTone(self, e):
  checkbox = e.GetEventObject()
  for ctrl in self.toneboxctrls.itervalues():
   ctrl.Enable(checkbox.GetValue())

 def onconvert(self, e):
  checkbox = e.GetEventObject()
  self.ctrls['convertList'].Enable(checkbox.GetValue())


 def onAddFile(self, e):
  dlg = wx.FileDialog(self)
  if dlg.ShowModal() == wx.ID_OK:
   self.ctrls['list'].Append([dlg.GetPath()])

 def setDefaultValues(self):
  self.ctrls['fadeinValue'].Enable(self.ctrls['fadein'].GetValue())
  self.ctrls['fadeoutValue'].Enable(self.ctrls['fadeout'].GetValue())
  for ctrl in self.volumeboxctrls.itervalues():
   ctrl.Enable(self.ctrls['changeVolume'].GetValue())
  for ctrl in self.toneboxctrls.itervalues():
   ctrl.Enable(self.ctrls['changeTone'].GetValue())
  self.ctrls['convertList'].Enable(self.ctrls['convert'].GetValue())

class Controller:
 def __init__(self, app):
  self.mainWindow = MainWindow(None)
  self.mainWindow.Show(True)

if __name__=='__main__':
 app = wx.App(False)
 controller = Controller(app)
 app.MainLoop()