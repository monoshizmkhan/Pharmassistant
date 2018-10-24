class NotificationManager(object):

    def __init__(self):
        pass

    m = MedicineList()
    m.printList()
    m.sendCountNotifications()
    print("Expired: ")
    print(m.sendExpiryNotifications())

