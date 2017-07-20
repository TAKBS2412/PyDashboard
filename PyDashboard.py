from tkinter import *
from tkinter import ttk

class Chooser(ttk.LabelFrame):
    def __init__(self, master=None, column=0, **kw):
        ttk.LabelFrame.__init__(self, master, **kw)
        self.column = column
        self.createWidgets()
    def createWidgets(self):
        self.header = ttk.Label(self, text="Step 1:")
        self.header.grid(row=1, column=self.column)
        self.header2 = ttk.Label(self, text="sdf")
        self.header2.grid(row=2, column=self.column)
        
class PyDashboard(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.header = ttk.Label(self, text="PyDashboard")
        self.header.grid(row=0, column=0)
        
        self.pane = ttk.PanedWindow(self, orient=HORIZONTAL)
        self.pane.grid(row=1, column=0, columnspan=2)
        
        self.robotStatus = Chooser(self.pane, 0, text="Robot Status", width=500, height=500)
        self.robotStatus.grid(row=1, column=0, rowspan=2, columnspan=2)
        
        self.pane.add(self.robotStatus)
        
dashboard = PyDashboard(Tk())
dashboard.master.title("PyDashboard")
dashboard.mainloop()
