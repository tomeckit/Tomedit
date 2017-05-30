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
  panel = wx.Panel(self)
  sizer = wx.BoxSizer(wx.VERTICAL)

  self.listLabel = wx.StaticText(panel, label='pliki')
  self.list = wx.ListView(panel)
  self.list.InsertColumn(0, 'nazwa pliku')
  self.list.InsertColumn(1, '�cie�ka')
  self.addFile = wx.Button(panel, label='dodaj plik')
  self.addFolder = wx.Button(panel, label='dodaj folder')
  self.subFolders = wx.CheckBox(panel,label='uwzgl�dniaj podfoldery')
  self.fadein = wx.CheckBox(panel,label='�agodny start')
  self.fadeinLabel = wx.StaticText(panel, label='Ms')
  self.fadeinValue = wx.SpinCtrl(panel, value='0', min=0, max=20000)
  self.fadeout = wx.CheckBox(panel,label='�agodne zciszenie')
  self.fadeoutLabel = wx.StaticText(panel, label='Ms')
  self.fadeoutValue = wx.SpinCtrl(panel, value='0', min=0, max=20000)
  self.changeVolume = wx.CheckBox(panel,label='Zmie� g�o�no��')

  self.volumeMethodTitle = wx.StaticBox( panel, -1, "Zmiana g�o�no�ci" )
  self.volumeMethod = wx.StaticBoxSizer( self.volumeMethodTitle, wx.VERTICAL )
  self.volumeMethod.ctrls = []
  self.volumeMethod.Manual = wx.RadioButton( panel, -1, " R�cznie ", style = wx.RB_GROUP )
  self.volumeMethod.Auto = wx.RadioButton( panel, -1, " Automatycznie " )
  self.volumeMethod.ctrls.append((self.volumeMethod.Manual))
  self.volumeMethod.ctrls.append((self.volumeMethod.Auto))



  self.volumeLabel = wx.StaticText(panel, label='DB')

  self.volumeValue = wx.SpinCtrl(panel, value='0', min=-140, max=140)
  self.limiter = wx.CheckBox(panel,label='nie dopuszczaj do przesterowania')
  self.swapChannels = wx.CheckBox(panel,label='Zamie� kana�y')
  self.start = wx.Button(panel, label='Start')
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
  sizer.Add(self.changeVolume)
  sizer.Add(self.volumeMethod)
  sizer.Add(self.volumeMethod.Manual)
  sizer.Add(self.volumeMethod.Auto)
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


 def onFadein(self, e):
  checkbox = e.GetEventObject()
  self.fadeinValue.Enable(checkbox.GetValue())

 def onFadeout(self, e):
  checkbox = e.GetEventObject()
  self.fadeoutValue.Enable(checkbox.GetValue())

 def onChangeVolume(self, e):
  checkbox = e.GetEventObject()
  self.volumeValue.Enable(checkbox.GetValue())


 def onAddFile(self, e):
  dlg = wx.FileDialog(self)
  if dlg.ShowModal() == wx.ID_OK:
   self.list.Append([dlg.GetPath()])

 def setDefaultValues(self):
#  self.volumeMethod.Enable(self.changeVolume.GetValue())
# ta etykieta pokazuje si� tak czy inaczej i nie wiem jak zrobi� �eby znikn�a po odznaczeniu pola wyboru.
  self.volumeMethod.Manual.Enable(self.changeVolume.GetValue())
  self.volumeMethod.Auto.Enable(self.changeVolume.GetValue())
# to si� ukry�o z jakiego� powodu na sztywno.
  self.volumeValue.Enable(self.changeVolume.GetValue())
  self.fadeinValue.Enable(self.fadein.GetValue())
  self.fadeoutValue.Enable(self.fadeout.GetValue())


class Controller:
 def __init__(self, app):
  self.mainWindow = MainWindow(None)
  self.mainWindow.Show(True)

if __name__=='__main__':
 app = wx.App(False)
 controller = Controller(app)
 app.MainLoop()