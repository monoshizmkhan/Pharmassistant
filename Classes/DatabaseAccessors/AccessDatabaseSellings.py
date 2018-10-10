from abc import ABC, abstractmethod
from Classes.Utilities import Iterator, Container
from Classes import Statics

class AccessDatabaseSellings(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseSellings.DatabaseSellings()



    class DatabaseSellings(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.medNames.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.medNames.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd, quantity):
            temp=toAdd
            temp2=quantity
            #pass temp to a database management class method

        def remove(self, toBeRemove, quantity):
            temp=toBeRemove
            temp2=quantity
            #pass temp to a database management class method

        def update(self, medName, attribute, newValue):
            temp=medName
            #dowork

        def search(self, toSearch):
            temp=""
            #pass temp to a database management class method which returns the search result
            return temp