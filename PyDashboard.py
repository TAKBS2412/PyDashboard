import tkinter as tk

class Chooser(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
    def createWidgets(self):
        self.header = tk.Label(self, text="Step 1:").grid(row=0, column=0)
        self.header2 = tk.Label(self, text="sdf").grid(row=1, column=0)
        
class PyDashboard(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.header = tk.Label(self, text="PyDashboard").grid(row=0, column=0)
        self.frame0 = Chooser().grid(row=1, column=0)
        
dashboard = PyDashboard()
dashboard.master.title("PyDashboard")
dashboard.mainloop()
