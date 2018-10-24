

class Medicine(object):

    def __init__(self,medID,name,type,qty,price,expDate,shelf,imgLink):
        self.medID = medID
        self.name = name
        self.type = type
        self.qty = qty
        self.price = price
        self.expDate = expDate
        self.shelf = shelf
        self.imgLink = imgLink

    def __str__(self):

        jsonTypeString =  '{"medID": "'+ self.medID+'", "name": "'+self.name+'", "qty": "'+self.qty+'", "'\
                        + 'expDate": "'+self.expDate+'", "' \
                        + 'type": "' + self.type + '", "' \
                        + 'shelf": "'+self.shelf+'", "'\
                        + 'imgLink": "'+self.imgLink+'"}'
        return jsonTypeString


# ####
# medNames=["Para01#Napa#Paracetamol#5#20#01-01-2020#22C#/static/Images/napa.jpg",
#           "Para02#Ace#Paracetamol#6#15#01-01-2020#22D#/static/Images/ace.jpg",
#           "Util01#Bandages#Utilities#2#50#01-01-2020#12B#/static/Images/bandages.jpg",
#           "Saline01#Orsaline#Saline#1#50#01-07-2019#11A#/static/Images/orsaline.jpg"
#           ]
# ####

m1 = Medicine("Para01", "Napa", "Paracetamol", "5", "20", "01-01-2020", "22C", "/static/Images/napa.jpg")
m2 = Medicine("Para02", "Ace", "Paracetamol", "6", "15", "01-01-2020", "22D", "/static/Images/ace.jpg")
m3 = Medicine("Util01", "Bandages", "Utilities", "2", "50", "01-01-2020", "12B", "/static/Images/bandages.jpg")
m4 = Medicine("Saline01", "Orsaline", "Saline", "1", "50", "01-01-2020", "11A", "/static/Images/orslaine.jpg")
#m5 = Medicine("Para01#", "Napa", "Paracetamol", "5", "20", "01-01-2020", "22C", "/static/Images/napa.jpg")
