from networktables import NetworkTables

'''
Sends data over to the user using NetworkTables.
'''
class Networking:

    '''
    Creates a Networking instance (see above description).
    Parameters:
        ip - The ip address to connect to.
        tablename - The name of the NetworkTable to connect to.
    '''
    def __init__(self, ip="roborio-2412-frc.local", tablename="PyDashboard"):
        # Setup NetworkTables
        NetworkTables.initialize(server=ip)
        self.table = NetworkTables.getTable(tablename)
        
    '''
    Sends data over to the user using NetworkTables.
    Assumes that the data is a string.
    '''
    def sendData(self, key, value):
        self.table.putString(key, value)
    '''
    Returns whether the robot is connected or not.
    '''
    def isConnected(self):
        return self.table.isConnected()


    '''
    Adds a connection listener that will be called when a connection is made.
    Parameters:
        listener - This function will be called when a new connection is made.
        immediateNotify - If the listener should be called immediately with any connection information.
    '''
    def addConnectionListener(self, listener, immediateNotify=False):
        NetworkTables.addConnectionListener(listener, immediateNotify)
