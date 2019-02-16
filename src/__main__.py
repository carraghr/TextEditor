import os
import wx
from ctypes.test.test_pickling import name

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.dirname = ''
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        fileMenu.Append(wx.ID_NEW, "&New")
        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        
        fileMenu.Append(wx.ID_OPEN, "&Open")        
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        
        fileMenu.Append(wx.ID_SAVE, "&Save")
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        
        fileMenu.Append(wx.ID_SAVEAS, "&SaveAs")
        self.Bind(wx.EVT_MENU, self.OnSaveAs, id=wx.ID_SAVEAS)
        
        fileMenu.AppendSeparator()        
        fileMenu.Append(wx.ID_EXIT,'&Quite')
        self.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_EXIT)
        
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,1,wx.EXPAND)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

    def getFileName(self):
        for x in range(0,100):
            name = "Untitled"+str(x)+".txt"
            if not(os.path.exists("./"+name)):
                return name

    def OnNew(self, e):
        name = self.getFileName()   
        print(name)     
        self.fileName = name
        self.dirname = os.getcwd()
        fileHandle = open(os.path.join(self.dirname, self.fileName),'w')
        fileHandle.close();
        self.SetTitle(self.fileName)
        
    def OnOpen(self, e):
        dig = wx.FileDialog(self, "Choose a File", self.dirname, "", "Text Files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dig.ShowModal()==wx.ID_OK:
            self.fileName = dig.GetFilename()
            self.dirname = dig.GetDirectory()
            
            fileHandle = open(os.path.join(self.dirname, self.fileName),'r')
            self.control.SetValue(fileHandle.read())
            fileHandle.close();
            self.SetTitle(self.fileName)
         
        print(dig.GetPath())
        dig.Destroy()
      
    def OnSave(self, e):
        content = self.control.GetValue()
        fileHandle = open(os.path.join(self.dirname, self.fileName),'w')
        fileHandle.write(content)
        fileHandle.close();
        self.SetTitle(self.fileName)
  
    def OnSaveAs(self, e):
        dlg = wx.FileDialog(self,"Choose a file",self.dirname,"","Text Files (*.txt)|*.txt",wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal()==wx.ID_OK:
            content = self.control.GetValue()
            self.fileName = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            
            fileHandle = open(os.path.join(self.dirname, self.fileName),'w')
            fileHandle.write(content)
            fileHandle.close();
            self.SetTitle(self.fileName)
         
        print(dlg.GetPath())
        dlg.Destroy()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()