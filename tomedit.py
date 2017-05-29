# -*- coding: utf-8 -*-
import wx
from wx.lib.pubsub import pub
class MainWindow(wx.Frame):
 def __init__(self, parent):
  wx.Frame.__init__(self, parent, title="Tomedit")
  self.initUi()
  self.bindEvents()
 def initUi(self):
  panel = wx.Panel(self)
  sizer = wx.BoxSizer(wx.VERTICAL)
  self.listLabel = wx.StaticText(panel, label='pliki')
  self.list = wx.ListView(panel)
  self.list.InsertColumn(0, 'plik')
  self.addFile = wx.Button(panel, label='dodaj plik')
  self.addFolder = wx.Button(panel, label='dodaj folder')
  self.subFolders = wx.CheckBox(panel,label='uwzglêdniaj podfoldery')
  self.fadein = wx.CheckBox(panel,label='£agodny start')
  self.fadeinValue = wx.TextCtrl(panel)
  self.increaseVolume = wx.CheckBox(panel,label='Zwiêksz g³oœnoœæ')
  self.volume = wx.TextCtrl(panel)
  self.start = wx.Button(panel, label='Start')
  sizer.Add(self.listLabel)
  sizer.Add(self.list)
  sizer.Add(self.addFile)
  sizer.Add(self.addFolder)
  sizer.Add(self.subFolders)
  sizer.Add(self.fadein)
  sizer.Add(self.fadeinValue)
  sizer.Add(self.increaseVolume)
  sizer.Add(self.volume)
  sizer.Add(self.start)

  panel.SetSizerAndFit(sizer)

 def bindEvents(self):
  self.addFile.Bind(wx.EVT_BUTTON, self.onAddFile)

 def onAddFile(self, e):
  dlg = wx.FileDialog(self)
  if dlg.ShowModal() == wx.ID_OK:
   self.list.Append([dlg.GetPath()])
class Controller:
 def __init__(self, app):
  self.mainWindow = MainWindow(None)
  self.mainWindow.Show(True)

if __name__=='__main__':
 app = wx.App(False)
 controller = Controller(app)
 app.MainLoop()