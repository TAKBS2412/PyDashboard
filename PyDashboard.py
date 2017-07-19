import tkinter as tk

class PyDashboard(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.header = tk.Label(self, text="PyDashboard").grid(row=0, column=0)
dashboard = PyDashboard()
dashboard.master.title("PyDashboard")
dashboard.mainloop()
