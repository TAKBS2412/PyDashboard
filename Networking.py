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
