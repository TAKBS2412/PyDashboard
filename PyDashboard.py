from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
class Chooser(ttk.LabelFrame):
    def __init__(self, master=None, column=0, headertext="", comboboxvalues=(), imgpath="", **kw):
        ttk.LabelFrame.__init__(self, master, **kw)
        self.column = column
        self.headertext = headertext
        self.comboboxvalues = comboboxvalues
        self.imgpath = imgpath
        self.createWidgets()
    def createWidgets(self):
        self.header = ttk.Label(self, text=self.headertext)
        self.header.grid(row=1, column=self.column)

        self.dropdownvar = StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdownvar)
        self.dropdown["values"] = self.comboboxvalues
        self.dropdown.grid(row=2, column=self.column)

        self.image = ImageTk.PhotoImage(Image.open(self.imgpath))
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
        
        self.robotStatus = Chooser(self.pane, 0, "Step 1", ("A", "B", "C"), "imgs/Steampunk RT_icon.png", text="Robot Status", width=1920, height=1080)
        self.robotStatus.grid(row=1, column=0, rowspan=2, columnspan=2)
        
        self.pane.add(self.robotStatus)
        
dashboard = PyDashboard(Tk())
dashboard.master.title("PyDashboard")
dashboard.mainloop()
