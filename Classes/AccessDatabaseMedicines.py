from abc import ABC, abstractmethod
from Classes.Utilities import Iterator, Container


medNames=["Para01#Napa#Paracetamol#5#20#01-01-2020#22C#/static/Images/napa.jpg",
          "Para02#Ace#Paracetamol#6#15#01-01-2020#22D#/static/Images/ace.jpg",
          "Util01#Bandages#Utilities#2#50#01-01-2020#12B#/static/Images/bandages.jpg",
          "Saline01#Orsaline#Saline#1#50#01-07-2019#11A#/static/Images/orsaline.jpg"
          ]

searchKey=""
result=""

class AccessDatabaseMedicines(Container.Container, Iterator.Iterator):

    def __init__(self, index=0):
        self.index=index


    def getIterator(selfself):
        return AccessDatabaseMedicines()

    def hasNext(self):
        if self.index < medNames.__len__():
            return True
        else:
            return False

    def next(self):
        if self.hasNext():
            a = medNames.__getitem__(self.index)
            self.index += 1
            return a
        else:
            self.index=0

    def add(self, toAdd):
        temp=toAdd
        #pass temp to a database management class method

    def remove(self, toBeRemove):
        temp=toBeRemove
        #pass temp to a database management class method

    def search(self, toSearch):
        temp=""
        #pass temp to a database management class method which returns the search result
        if temp=="":
            return "No matches"
        else:
            return temp