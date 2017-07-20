from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
class Chooser(ttk.LabelFrame):
    def __init__(self, master=None, column=0, **kw):
        ttk.LabelFrame.__init__(self, master, **kw)
        self.column = column
        self.createWidgets()
    def createWidgets(self):
        self.header = ttk.Label(self, text="Step 1:")
        self.header.grid(row=1, column=self.column)

        self.dropdownvar = StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdownvar)
        self.dropdown["values"] = ("Test", "Test #2", "Test #3")
        self.dropdown.grid(row=2, column=self.column)

        self.image = ImageTk.PhotoImage(Image.open("imgs/Steampunk RT_icon.png"))
        self.imagelabel = ttk.Label(self, image=self.image)
        self.imagelabel.image = self.image
        self.imagelabel.grid(row=3, column=self.column)
        
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
        
        self.robotStatus = Chooser(self.pane, 0, text="Robot Status", width=1920, height=1080)
        self.robotStatus.grid(row=1, column=0, rowspan=2, columnspan=2)
        
        self.pane.add(self.robotStatus)
        
dashboard = PyDashboard(Tk())
dashboard.master.title("PyDashboard")
dashboard.mainloop()
