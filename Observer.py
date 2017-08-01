from abc import ABC, abstractmethod

'''
An abstract class that represents an Observer of the Data class.
'''

class Observer(ABC):
    # An abstract method that is called when the Data class receives an update.
    @abstractmethod
    def update(self, changeditem):
        pass
