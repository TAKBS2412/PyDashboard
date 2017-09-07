import Observer
import Data
import Networking
from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import ImageTk, Image

'''
This class is a subclass of ttk.LabelFrame and Observer.
It contains 3 widgets: A header (a Label), a Combobox, and an image.
'''

class Chooser(ttk.LabelFrame, Observer.Observer):

    '''
    Creates a Chooser instance (see above description).
    Parameters:
        subject - The subject to observe.
        master - The master Frame.
        row - The row in the grid that this Chooser will occupy.
        column - The column in the grid that this Chooser will occupy.
        headertext - The text that the header Label will display.
        comboboxvalues - A tuple of values that the Combobox will display.
        imgdict - A dictionary. Each key is an option that can be selected by the master Chooser. Each value is the path to the image (as a string) that will be displayed.
        networking - A Networking instance (see Networking module).
        keyname - The name of the key that this Chooser is associated with. The key will be sent (along with the currently selected mode) using networking.
    '''
    def __init__(self, subject, master=None, row=0, column=0, headertext="", comboboxvalues=(), imgdict={}, networking=None, keyname="", **kw):
        ttk.LabelFrame.__init__(self, master, **kw) # Call the superclass's constructor.

        # Set the values that were passed in as parameters.
        self.subject = subject
        self.row = row
        self.column = column
        self.headertext = headertext
        self.comboboxvalues = comboboxvalues
        self.imgdict = imgdict
        self.networking = networking
        self.keyname = keyname

        self.subject.attach(self)
        self.subject.addDataItem(Data.DataItem(keyname, ""))
        
        self.createWidgets() # Create the widgets that will be displayed to the user.
    def createWidgets(self):
        # Create a Label with the text specified (self.headertext).
        self.header = ttk.Label(self, text=self.headertext) # Create the Label itself.
        self.header.grid(row=self.row, column=self.column) # Add to Frame.

        # Create a drop down menu (AKA Combobox) from the values specified (self.comboboxvalues).
        self.dropdownvar = StringVar() # Create a string variable (StringVar) that will hold the currently selected value.
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdownvar) # Create the Combobox itself.
        self.dropdown["values"] = self.comboboxvalues # Set the values that were specified in the constructor.
        self.dropdown["state"] = "readonly"
        self.dropdown.bind("<<ComboboxSelected>>", self.sendData)
        self.dropdown.grid(row=self.row+1, column=self.column) # Add to Frame.

        # Create an image from the path specified (self.imgdict) and display it to the user using a Label.
        self.image = ImageTk.PhotoImage(Image.open(self.imgdict["Drive forward"])) # Load the image.
        self.imagelabel = ttk.Label(self, image=self.image) # Create the Label that will be used to display the image.
        self.imagelabel.image = self.image # Make sure to keep a reference to the image - see http://effbot.org/tkinterbook/photoimage.htm.
        self.imagelabel.grid(row=self.row+2, column=self.column) # Add to Frame.

    # Called when an option is selected.
    # Notifies the subject.
    def sendData(self, event):
        self.dropdown.selection_clear()
        self.subject.notify(Data.DataItem(self.keyname, self.dropdownvar.get()))

    # Called when something in the subject changes.
    # Parameter:
    #     changeditem - The DataItem that was changed.
    def update(self, changeditem):
        if changeditem.key == "Step1":
            # Set the image that will be displayed according to what was selected by the master Chooser.
            selectedval = self.imgdict[changeditem.value]
            self.imagelabel.image = ImageTk.PhotoImage(Image.open(selectedval))
            self.imagelabel.configure(image=self.imagelabel.image)
            if "Ignore" in selectedval:
                if str(self.dropdown["state"]) != "disabled":
                    self.dropdown["state"] = "disabled"
                    self.subject.notify(Data.DataItem(self.keyname, "DoNothing"))
            else:
                if str(self.dropdown["state"]) != "readonly":
                    self.dropdown["state"] = "readonly"
                    self.subject.notify(Data.DataItem(self.keyname, self.dropdownvar.get()))

'''
This class represents the GUI for PyDashboard.
It contains widgets that are laid out in the general fashion of this image: https://drive.google.com/file/d/0B_62XHEIagxyUi0yLV9uT1JFS3M/view?usp=sharing.
Each rectangle to the right of and in the same row as the rectangle labeled "Robot Status" (but not including the "Robot Status" rectangle itself) is a Chooser.
'''
class PyDashboard(ttk.Frame, Observer.Observer):

    '''
    Creates a PyDashboard instance (see above description).
    Parameters:
        subject - The subject to observe.
        master - The master Frame.
        headerlabeltext - The text that the header Label will display.
        networking - A Networking instance (see Networking module).
    The tuples must all be the same length, and the data within them must be "lined up" - therefore, the third element in headertexttup, the third element in comboboxvaluestup, and the third element in imgpathtup will all be used by the same Chooser.
    '''
    def __init__(self, subject, master=None, headerlabeltext="", networking=None, **kw):
        ttk.Frame.__init__(self, master, **kw) # Call the superclass's constructor.

        self.grid() # Use the grid layout manager.
    
        # Set the values that were passed in as parameters.
        self.subject = subject
        self.headerlabeltext = headerlabeltext

        self.networking = networking

        self.subject.attach(self)

        self.bodyfont = font.Font(family="BankGothic", size=11)

        self.defaultfont = font.nametofont("TkDefaultFont")
        self.defaultfont.configure(family="BankGothic")
        self.option_add("*Font", self.bodyfont)

        # Create theme
        self.bodystyle = ttk.Style(self) # Create a style.
        self.bodystyle.theme_create("Test", parent="default") # Create the theme.
        self.bodystyle.configure("TFrame", background="#575757", foreground="white") # Configure the style for the PyDashboard.
        self.bodystyle.configure("TButton", foreground="black") # Configure the style for a Button.
        #self.bodystyle.configure("TButton.Label", background="#575757", foreground="white") # Configure the style for a Button.
        self.bodystyle.configure("TLabel", background="#575757", foreground="white") # Configure the style for a Label.
        self.bodystyle.configure("TLabelframe.Label", background="#575757", foreground="white") # Configure the style for a Labelframe.
        self.bodystyle.configure("TLabelframe", background="#575757", foreground="white")
        self.bodystyle.configure("TCombobox", selectbackground="#575757", bordercolor="white")

        self.option_add("*TCombobox*Listbox.background", "#575757")
        self.option_add("*TCombobox*Listbox.foreground", "white")
        self.option_add("*TCombobox*Listbox.selectForeground", "#575757")
        self.option_add("*TCombobox*Listbox.selectBackground", "white")
        
        self.bodystyle.theme_use("vista")
        
        self.createWidgets() # Create the widgets that will be displayed to the user.
    def createWidgets(self):
        # Create the header Label
        self.header = ttk.Label(self, text=self.headerlabeltext) # Create the Label.
        self.header.grid(row=0, column=1) # Add the Label to the PyDashboard.
        
        # Create the Robot Status LabelFrame.
        self.robotstatus = ttk.LabelFrame(self, text="Robot Status") # Create the LabelFrame itself.
        self.robotstatus.label = ttk.Label(self.robotstatus, text="Robot Disconnected") # Create the Label that will be displayed within the LabelFrame.
        self.robotstatus.label.grid(row=1, column=0) # Add the Label to the LabelFrame.
        self.robotstatus.grid(row=1, column=0, rowspan=2, sticky=(N, S)) # Add the LabelFrame to the PyDashboard.

        # Create a PanedWindow, which will contain the Choosers for steps 1 and 2.
        self.pane1and2 = ttk.PanedWindow(self, orient=HORIZONTAL) # Create the PanedWindow.
        self.pane1and2.grid(row=1, column=1, sticky=(E, W)) # Add the PanedWindow to the PyDashboard.

        # Create a PanedWindow, which will contain the Choosers for steps 3 and 4.
        self.pane3and4 = ttk.PanedWindow(self, orient=HORIZONTAL) # Create the PanedWindow.
        self.pane3and4.grid(row=2, column=1) # Add the PanedWindow to the PyDashboard.

    # Adds the Choosers to the PyDashboard.
    def addChoosers(self, choosers):
        # Add Step 1 Chooser.
        self.step1 = choosers[0]
        self.step1.grid(row=1, column=1, sticky=(E, W)) # Add Step 1 Chooser to the PyDashboard.
        self.pane1and2.add(self.step1) # Add the Chooser to the PanedWindow.

        # Add Step 2 Chooser.
        self.step2 = choosers[1]
        self.step2.grid(row=1, column=2) # Add Step 2 Chooser to the PyDashboard.
        self.pane1and2.add(self.step2) # Add the Chooser to the PanedWindow.

        # Add Step 3 Chooser.
        self.step3 = choosers[2]
        self.step3.grid(row=2, column=1) # Add Step 3 Chooser to the PyDashboard.
        self.pane3and4.add(self.step3) # Add the Chooser to the PanedWindow.

        # Add Step 4 Chooser.
        self.step4 = choosers[3]
        self.step4.grid(row=2, column=2) # Add Step 4 Chooser to the PyDashboard.
        self.pane3and4.add(self.step4) # Add the Chooser to the PanedWindow.
        
    # Called when something in the subject changes.
    # Parameter:
    #     changeditem - The DataItem that was changed.
    def update(self, changeditem):
        if changeditem.key == "connectionstatus":
            # Update GUI.
            if changeditem.value:
                self.robotstatus.label["text"] = "Robot Connected"
            else:
                self.robotstatus.label["text"] = "Robot Disconnected"
subject = Data.Data()
networking = Networking.Networking(subject, "10.24.12.2") # Try to connect to 10.24.12.51.

title = "PyDashboard"
root = Tk()
dashboard = PyDashboard(subject, root, title, networking)
dashboard.master.title(title)
choosers = [
    Chooser(subject, dashboard.pane1and2, 1, 1, "Choose an autonomous mode:", ("Drive forward", "Left Peg", "Center Peg", "Right Peg"), {"Drive forward" : "imgs/Step1/Step1_Drive_forward.png", "Left Peg" : "imgs/Step1/Step1_left.png", "Center Peg" : "imgs/Step1/Step1_center.png", "Right Peg" : "imgs/Step1/Step1_right.png"}, networking, "Step1", text="Step 1"),
    Chooser(subject, dashboard.pane1and2, 1, 2, "Falca will drive forward to the baseline using...", ("Motion Profiling", "Time-Based", "Encoders"), {"Drive forward" : "imgs/Step2/Step2_Drive_forward.png", "Left Peg" : "imgs/Step2/Step2_left.png", "Center Peg" : "imgs/Ignore this step.png", "Right Peg" : "imgs/Step2/Step2_right.png"}, networking, "Step2", text="Step 2"),
    Chooser(subject, dashboard.pane3and4, 2, 1, "Falca will turn towards the peg using...", ("Vision Processing", "Gyroscope"), {"Drive forward" : "imgs/Ignore this step.png", "Left Peg" : "imgs/Step3/Step3_left.png", "Center Peg" : "imgs/Ignore this step.png", "Right Peg" : "imgs/Step3/Step3_right.png"}, networking, "Step3", text="Step 3"),
    Chooser(subject, dashboard.pane3and4, 2, 2, "Falca will drive towards the peg using...", ("Vision Processing", "Encoders"), {"Drive forward" : "imgs/Ignore this step.png", "Left Peg" : "imgs/Step4/Step4_left.png", "Center Peg" : "imgs/Step4/Step4_center.png", "Right Peg" : "imgs/Step4/Step4_right.png"}, networking, "Step4", text="Step 4")
]
dashboard.addChoosers(choosers)
root.iconbitmap("Steampunk RT_icon.ico")
dashboard.mainloop()
