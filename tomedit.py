# -*- coding: utf-8 -*-


import wx
from wx.lib.pubsub import pub
class MainWindow(wx.Frame):
 def __init__(self, parent):
  wx.Frame.__init__(self, parent, title="Tomedit")
  self.initUi()
  self.bindEvents()
  self.setDefaultValues()

 def initUi(self):
  self.staticBoxCtrls = []
  self.volumeMethodCtrls=[]
  panel = wx.Panel(self)
  sizer = wx.BoxSizer(wx.VERTICAL)

  self.listLabel = wx.StaticText(panel, label='pliki')
  self.list = wx.ListView(panel)
  self.list.InsertColumn(0, 'nazwa pliku')
  self.list.InsertColumn(1, 'ścieżka')
  self.addFile = wx.Button(panel, label='dodaj plik')
  self.addFolder = wx.Button(panel, label='dodaj folder')
  self.subFolders = wx.CheckBox(panel,label='uwzględniaj podfoldery')
  self.fadein = wx.CheckBox(panel,label='Łagodny start')
  self.fadeinLabel = wx.StaticText(panel, label='Ms')
  self.fadeinValue = wx.SpinCtrl(panel, value='0', min=0, max=20000)
  self.fadeout = wx.CheckBox(panel,label='Łagodne zciszenie')
  self.fadeoutLabel = wx.StaticText(panel, label='Ms')
  self.fadeoutValue = wx.SpinCtrl(panel, value='0', min=0, max=20000)
  self.changeVolume = wx.CheckBox(panel,label='Zmień głośność')
  self.volumeChangeGroup = wx.StaticBox( panel, -1, "Zmiana głośności" )
  staticBoxSizer = wx.StaticBoxSizer(self.volumeChangeGroup, wx.VERTICAL)
  self.volumeMethodManual = wx.RadioButton( panel, -1, " Ręcznie ", style = wx.RB_GROUP )
  self.volumeMethodAuto = wx.RadioButton( panel, -1, " Automatycznie " )

  self.volumeLabel = wx.StaticText(panel, label='DB')

  self.volumeValue = wx.SpinCtrl(panel, value='0', min=-140, max=140)

  self.limiter = wx.CheckBox(panel,label='nie dopuszczaj do przesterowania')
  self.swapChannels = wx.CheckBox(panel,label='Zamień kanały')
  self.start = wx.Button(panel, label='Start')

  self.staticBoxCtrls.append(self.volumeMethodManual)
  self.staticBoxCtrls.append(self.volumeMethodAuto)
  self.staticBoxCtrls.append(self.volumeLabel)
  self.staticBoxCtrls.append(self.volumeValue)
  self.volumeMethodCtrls.append(self.volumeMethodManual)
  self.volumeMethodCtrls.append(self.volumeMethodAuto)
  for ctrl in self.staticBoxCtrls:
   staticBoxSizer.Add(ctrl)

  sizer.Add(self.listLabel)
  sizer.Add(self.list)
  sizer.Add(self.addFile)
  sizer.Add(self.addFolder)
  sizer.Add(self.subFolders)
  sizer.Add(self.fadein)
  sizer.Add(self.fadeinLabel)
  sizer.Add(self.fadeinValue)
  sizer.Add(self.fadeout)
  sizer.Add(self.fadeoutLabel)
  sizer.Add(self.fadeoutValue)
  sizer.Add(staticBoxSizer)
  sizer.Add(self.changeVolume)
  sizer.Add(self.volumeMethodManual)
  sizer.Add(self.volumeMethodAuto)
  sizer.Add(self.volumeLabel)
  sizer.Add(self.volumeValue)
  sizer.Add(self.limiter)
  sizer.Add(self.swapChannels)
  sizer.Add(self.start)


  panel.SetSizerAndFit(sizer)

 def bindEvents(self):
  self.addFile.Bind(wx.EVT_BUTTON, self.onAddFile)

  self.fadein.Bind(wx.EVT_CHECKBOX, self.onFadein)
  self.fadeout.Bind(wx.EVT_CHECKBOX, self.onFadeout)
  self.changeVolume.Bind(wx.EVT_CHECKBOX, self.onChangeVolume)
  self.volumeMethodManual.Bind(wx.EVT_RADIOBUTTON, self.onManual)
  self.volumeMethodAuto.Bind(wx.EVT_RADIOBUTTON, self.onAuto)


 def onFadein(self, e):
  checkbox = e.GetEventObject()
  self.fadeinValue.Enable(checkbox.GetValue())

 def onFadeout(self, e):
  checkbox = e.GetEventObject()
  self.fadeoutValue.Enable(checkbox.GetValue())

 def onChangeVolume(self, e):
  checkbox = e.GetEventObject()
  for ctrl in self.staticBoxCtrls:
   ctrl.Enable(checkbox.GetValue())

 def onManual(self, e):
  self.volumeValue.Enable(True)

 def onAuto(self, e):
  self.volumeValue.Enable(False)


 def onAddFile(self, e):
  dlg = wx.FileDialog(self)
  if dlg.ShowModal() == wx.ID_OK:
   self.list.Append([dlg.GetPath()])

 def setDefaultValues(self):
  self.fadeinValue.Enable(self.fadein.GetValue())
  self.fadeoutValue.Enable(self.fadeout.GetValue())
  for ctrl in self.staticBoxCtrls:
   ctrl.Enable(self.changeVolume.GetValue())

class Controller:
 def __init__(self, app):
  self.mainWindow = MainWindow(None)
  self.mainWindow.Show(True)

if __name__=='__main__':
 app = wx.App(False)
 controller = Controller(app)
 app.MainLoop()