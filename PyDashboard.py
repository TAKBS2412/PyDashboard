from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import ImageTk, Image

# Called when the connect button is pressed
def connect():
    print("Connect attempt made.")

# Called when the send button is pressed.
def send():
    print("(hopefully) Sending values...")

'''
This class is a subclass of ttk.LabelFrame.
It contains 3 widgets: A header (a Label), a Combobox, and an image.
'''

class Chooser(ttk.LabelFrame):

    '''
    Creates a Chooser instance (see above description).
    Parameters:
        master - The master Frame.
        row - The row in the grid that this Chooser will occupy.
        column - The column in the grid that this Chooser will occupy.
        headertext - The text that the header Label will display.
        comboboxvalues - A tuple of values that the Combobox will display.
        imgpath - The path to the image (as a string) that will be displayed.
    '''
    def __init__(self, master=None, row=0, column=0, headertext="", comboboxvalues=(), imgpath="", **kw):
        ttk.LabelFrame.__init__(self, master, **kw) # Call the superclass's constructor.

        # Set the values that were passed in as parameters.
        self.row = row
        self.column = column
        self.headertext = headertext
        self.comboboxvalues = comboboxvalues
        self.imgpath = imgpath
        
        self.createWidgets() # Create the widgets that will be displayed to the user.
    def createWidgets(self):
        # Create a Label with the text specified (self.headertext).
        self.header = ttk.Label(self, text=self.headertext) # Create the Label itself.
        self.header.grid(row=self.row, column=self.column) # Add to Frame.

        # Create a drop down menu (AKA Combobox) from the values specified (self.comboboxvalues).
        self.dropdownvar = StringVar() # Create a string variable (StringVar) that will hold the currently selected value.
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdownvar) # Create the Combobox itself.
        self.dropdown["values"] = self.comboboxvalues # Set the values that were specified in the constructor.
        self.dropdown.grid(row=self.row+1, column=self.column) # Add to Frame.

        # Create an image from the path specified (self.imgpath) and display it to the user using a Label.
        self.image = ImageTk.PhotoImage(Image.open(self.imgpath)) # Load the image.
        self.imagelabel = ttk.Label(self, image=self.image) # Create the Label that will be used to display the image.
        self.imagelabel.image = self.image # Make sure to keep a reference to the image - see http://effbot.org/tkinterbook/photoimage.htm.
        self.imagelabel.grid(row=self.row+2, column=self.column) # Add to Frame.

'''
This class represents the GUI for PyDashboard.
It contains widgets that are laid out in the general fashion of this image: https://drive.google.com/file/d/0B_62XHEIagxyUi0yLV9uT1JFS3M/view?usp=sharing.
Each rectangle to the right of and in the same row as the rectangle labeled "Robot Status" (but not including the "Robot Status" rectangle itself) is a Chooser.
'''
class PyDashboard(ttk.Frame):

    '''
    Creates a PyDashboard instance (see above description).
    Parameters:
        master - The master Frame.
        headerlabeltext - The text that the header Label will display.
        headertexttup - A tuple. Each element in the tuple is the text that a Chooser's header Label will display.
        comboboxvaluestup - A tuple. Each element in the tuple is a tuple of values that a Chooser's Combobox will display.
        imgpathtup - A tuple. Each element in the tuple is a path to the image (as a string) that will be displayed by a Chooser.
        titletup - A tuple. Each element in the tuple is the text that will be displayed by the Chooser.
    titletup - A tuple. Each element in the tuple is the text that will be used as a title for the Chooser.
    The tuples must all be the same length, and the data within them must be "lined up" - therefore, the third element in headertexttup, the third element in comboboxvaluestup, and the third element in imgpathtup will all be used by the same Chooser.
    '''
    def __init__(self, master=None, headerlabeltext="", headertexttup=(), comboboxvaluestup=(), imgpathtup=(), titletup=(), **kw):
        ttk.Frame.__init__(self, master, **kw) # Call the superclass's constructor.

        self.grid() # Use the grid layout manager.
    
        # Set the values that were passed in as parameters.
        self.headerlabeltext = headerlabeltext
        self.headertexttup = headertexttup
        self.comboboxvaluestup = comboboxvaluestup
        self.imgpathtup = imgpathtup
        self.titletup = titletup

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

        # Create the Connect and Send buttons.
        self.connectbtn = ttk.Button(self, text="Connect", command=connect) # Create the Connect button.
        self.connectbtn.grid(row=4, column=1) # Add the Connect button to the PyDashboard.
        self.sendbtn = ttk.Button(self, text="Send", command=send) # Create the Send button.
        self.sendbtn.grid(row=4, column=2) # Add the Send button to the PyDashboard.

        # Create the Robot Status LabelFrame.
        self.robotstatus = ttk.LabelFrame(self, text="Robot Status") # Create the LabelFrame itself.
        self.robotstatus.label = ttk.Label(self.robotstatus, text="Robot Disconnected") # Create the Label that will be displayed within the LabelFrame.
        self.robotstatus.label.grid(row=1, column=0) # Add the Label to the LabelFrame.
        self.robotstatus.grid(row=1, column=0, rowspan=2) # Add the LabelFrame to the PyDashboard.

        # Create a PanedWindow, which will contain the Choosers for steps 1 and 2.
        self.pane1and2 = ttk.PanedWindow(self, orient=HORIZONTAL) # Create the PanedWindow.
        self.pane1and2.grid(row=1, column=1) # Add the PanedWindow to the PyDashboard.

        # Create and add Step 1 Chooser.
        self.step1 = Chooser(self.pane1and2, 1, 1, self.headertexttup[0], self.comboboxvaluestup[0], self.imgpathtup[0], text=self.titletup[0])
        self.step1.grid(row=1, column=1) # Add Step 1 Chooser to the PyDashboard.
        self.pane1and2.add(self.step1) # Add the Chooser to the PanedWindow.

        # Create and add Step 2 Chooser.
        self.step2 = Chooser(self.pane1and2, 1, 2, self.headertexttup[1], self.comboboxvaluestup[1], self.imgpathtup[1], text=self.titletup[1])
        self.step2.grid(row=1, column=2) # Add Step 2 Chooser to the PyDashboard.
        self.pane1and2.add(self.step2) # Add the Chooser to the PanedWindow.

        # Create a PanedWindow, which will contain the Choosers for steps 3 and 4.
        self.pane3and4 = ttk.PanedWindow(self, orient=HORIZONTAL) # Create the PanedWindow.
        self.pane3and4.grid(row=2, column=1) # Add the PanedWindow to the PyDashboard.

        # Create and add Step 3 Chooser.
        self.step3 = Chooser(self.pane3and4, 2, 1, self.headertexttup[2], self.comboboxvaluestup[2], self.imgpathtup[2], text=self.titletup[2])
        self.step3.grid(row=2, column=1) # Add Step 3 Chooser to the PyDashboard.
        self.pane3and4.add(self.step3) # Add the Chooser to the PanedWindow.

        # Create and add Step 4 Chooser.
        self.step4 = Chooser(self.pane3and4, 2, 2, self.headertexttup[3], self.comboboxvaluestup[3], self.imgpathtup[3], text=self.titletup[3])
        self.step4.grid(row=2, column=2) # Add Step 4 Chooser to the PyDashboard.
        self.pane3and4.add(self.step4) # Add the Chooser to the PanedWindow.

        '''
        # Create an array of all of the choosers and add them.
        self.choosers = []

        # Create and add Choosers to the PyDashboard.
        for zipobj in zip(range(len(self.headertexttup)), self.headertexttup, self.comboboxvaluestup, self.imgpathtup, self.titletup):
            self.choosers.append(Chooser(self.pane, zipobj[0]+1, zipobj[1], zipobj[2], zipobj[3], text=zipobj[4])) # Create a Chooser.
            self.choosers[zipobj[0]].grid(row=1, column=zipobj[0]+1) # Add the Chooser to the PyDashboard.
            self.pane.add(self.choosers[zipobj[0]]) # Add the Chooser to the PanedWindow.
        '''

title = "PyDashboard"
dashboard = PyDashboard(Tk(), title, ("Choose an autonomous mode:", "Falca will drive forward to the baseline using...", "Falca will turn towards the peg using...", "Falca will drive towards the peg using..."), (("Drive forward (if selected, ignore Steps 3 and 4)", "Left Peg", "Center Peg (if selected, ignore Step 3", "Right Peg"), ("Motion Profiling", "Time-Based", "Encoders"), ("Vision Processing", "Gyroscope"), ("Vision Processing", "Encoders")), ("imgs/Step1.png", "imgs/Step2.png", "imgs/Step3.png", "imgs/Step4.png"), ("Step 1", "Step 2", "Step 3", "Step 4"))
dashboard.master.title(title)
dashboard.mainloop()
