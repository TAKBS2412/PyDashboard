from tkinter import *
from tkinter import ttk

class Chooser(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
    def createWidgets(self):
        self.header = ttk.Label(self.master, text="Step 1:").grid(row=2, column=0)
        self.header2 = ttk.Label(self.master, text="sdf").grid(row=3, column=0)
        
class PyDashboard(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.header = ttk.Label(self, text="PyDashboard").grid(row=0, column=0)
        self.frame0 = Chooser(self).grid(row=1, column=0)
        
dashboard = PyDashboard(Tk())
dashboard.master.title("PyDashboard")
dashboard.mainloop()
