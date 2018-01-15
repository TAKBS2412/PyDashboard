from networktables import NetworkTables
import Data
import Observer
'''
Sends data over to the user using NetworkTables.
'''
class Networking(Observer.Observer):

    '''
    Creates a Networking instance (see above description).
    Parameters:
        subject - The subject to observe.
        ip - The ip address to connect to.
        tablename - The name of the NetworkTable to connect to.
    '''
    def __init__(self, subject, ip="roborio-2412-frc.local", tablename="PyDashboard"):
        self.subject = subject
        self.subject.attach(self)
        
        # Setup NetworkTables
        NetworkTables.initialize(server=ip)
        self.table = NetworkTables.getTable(tablename)
        NetworkTables.addConnectionListener(self.listener, False)

        self.subject.addDataItem(Data.DataItem("connectionstatus", self.isConnected()))
        
    '''
    Sends data over to the user using NetworkTables.
    Assumes that the data is a string.
    '''
    def sendData(self, key, value):
        print(value)
        self.table.putString(key, value)
    '''
    Returns whether the robot is connected or not.
    '''
    def isConnected(self):
        return self.table.isConnected()

    '''
    Called when the connection status changes.
    '''
    def listener(self, connected, info):
        self.subject.notify(Data.DataItem("connectionstatus", connected))

    '''
    Called when something in the subject changes.
    Parameter:
        changeditem - The DataItem that was changed.
    '''
    def update(self, changeditem):
        self.sendData(changeditem.key, changeditem.value)
