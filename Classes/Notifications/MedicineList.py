#from Classes.Notifications.Observable import Observable
from Classes.Models.medicine import Medicine
import json
import datetime


class MedicineList(object):

    """all the medicines"""

    def __init__(self):
        self.medicines = self.createMedList()

    def createMedList(self):

        medicines = [] #list of objects, will be collected from database
        m1 = Medicine("Para01", "Napa", "Paracetamol", "0", "20", "01-01-2020", "22C", "/static/Images/napa.jpg")
        m2 = Medicine("Para02", "Ace", "Paracetamol", "6", "15", "01-01-2018", "22D", "/static/Images/ace.jpg")
        m3 = Medicine("Util01", "Bandages", "Utilities", "2", "50", "01-01-2020", "12B", "/static/Images/bandages.jpg")
        m4 = Medicine("Saline01", "Orsaline", "Saline", "0", "50", "01-01-2020", "11A", "/static/Images/orslaine.jpg")

        medicines.append(m1)
        medicines.append(m2)
        medicines.append(m3)
        medicines.append(m4)

        return medicines

    def printList(self):

        for item in self.medicines:
            itemDict = vars(item)
            print(itemDict['medID']+" : "+itemDict['qty'] +" : "+itemDict['expDate'])

    def sendNotifications(self):

        notifications = [] #array of strings

        for item in self.medicines:
            itemDict= vars(item)
            cnt = int(itemDict['qty'])

            if cnt == 0:
                notification_string = "empty#"+ item.__str__()
                notifications.append(notification_string)
                #print(item.__str__())

            expDate = itemDict['expDate']
            expDate = datetime.datetime.strptime(expDate, "%d-%m-%Y").date()
            today = datetime.datetime.now().date()
            if today >= expDate:
                notification_string = "expired#" + item.__str__()
                notifications.append(notification_string)

        return notifications


# m = MedicineList()
# m.printList()
# print(m.sendCountNotifications())
# print("Expired: ")
# print(m.sendExpiryNotifications())


