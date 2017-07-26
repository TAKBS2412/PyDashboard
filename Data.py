'''
This class contains the data for a single Chooser that will be sent to the user.
'''

class DataItem:

    '''
    Creates a DataItem instance (see above description).
    Parameters:
        key - The key to be sent to NetworkTables.
        value - The value to be sent to NetworkTables.
    '''
    def __init__(self, key, value):
        # Set the values that were passed in as parameters.
        self.key = key
        self.value = value

'''
This class contains the data that will be sent to the user.
'''

class Data:

    '''
    Creates a Data instance (see above description).
    '''
    def __init__(self):
        self.dataitems = [] # Create an empty array of DataItems.

    '''
    Adds a DataItem.
    '''
    def addDataItem(self, dataitem):
        self.dataitems.append(dataitem)
        
