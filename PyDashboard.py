from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

'''
This class is a subclass of ttk.LabelFrame.
It contains 3 widgets: A header (a Label), a Combobox, and an image.
'''

class Chooser(ttk.LabelFrame):

    '''
    Creates a Chooser instance (see above description).
    Parameters:
        master - The master Frame.
        column - The column in the grid that this Chooser will occupy.
        headertext - The text that the header Label will display.
        comboboxvalues - A tuple of values that the Combobox will display.
        imgpath - The path to the image (as a string) that will be displayed.
    '''
    def __init__(self, master=None, column=0, headertext="", comboboxvalues=(), imgpath="", **kw):
        ttk.LabelFrame.__init__(self, master, **kw) # Call the superclass's constructor.

        # Set the values that were passed in as parameters.
        self.column = column
        self.headertext = headertext
        self.comboboxvalues = comboboxvalues
        self.imgpath = imgpath
        
        self.createWidgets() # Create the widgets that will be displayed to the user.
    def createWidgets(self):
        # Create a Label with the text specified (self.headertext).
        self.header = ttk.Label(self, text=self.headertext) # Create the Label itself.
        self.header.grid(row=1, column=self.column) # Add to Frame.

        # Create a drop down menu (AKA Combobox) from the values specified (self.comboboxvalues).
        self.dropdownvar = StringVar() # Create a string variable (StringVar) that will hold the currently selected value.
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdownvar) # Create the Combobox itself.
        self.dropdown["values"] = self.comboboxvalues # Set the values that were specified in the constructor.
        self.dropdown.grid(row=2, column=self.column) # Add to Frame.

        # Create an image from the path specified (self.imgpath) and display it to the user using a Label.
        self.image = ImageTk.PhotoImage(Image.open(self.imgpath)) # Load the image.
        self.imagelabel = ttk.Label(self, image=self.image) # Create the Label that will be used to display the image.
        self.imagelabel.image = self.image # Make sure to keep a reference to the image - see http://effbot.org/tkinterbook/photoimage.htm.
        self.imagelabel.grid(row=3, column=self.column) # Add to Frame.

'''
TODO ADD DOCUMENTATION RIGHT NOW
'''
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
