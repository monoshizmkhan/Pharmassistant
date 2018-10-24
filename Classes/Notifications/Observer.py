import abc


class Observer(object):

    """abstract class of observers"""
    def update(self, observed):
        pass


class NotificationObserver(Observer):

    """will store notifications"""

    def update(self, observed):

        print("I am notified by "+observed.getName())
