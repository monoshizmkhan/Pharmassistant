from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask_sqlalchemy import SQLAlchemy
import Classes.DatabaseHandlers.create_table as create_table
from operator import is_not
from functools import partial
import sqlalchemy

#import Classes.Statics.userList as userList, Classes.Statics.vendorList as vendorList, Classes.Statics.medList as medList, Classes.Statics.notificationList as notificationList, Classes.Statics.orderList as orderList, Classes.Statics.sellList as sellList, Classes.Statics.expenseList as expenseList
import Classes.Statics

userList = Classes.Statics.userList
vendorList = Classes.Statics.vendorList
medList = Classes.Statics.medList
notificationList = Classes.Statics.notificationList
orderList = Classes.Statics.orderList
sellList = Classes.Statics.sellList
expenseList = Classes.Statics.expenseList

Base = declarative_base()


engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/pharmassistant')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def Fetch():
    users = session.query(Classes.DatabaseHandlers.create_table.Users).all()
    s=""
    for user in users:
        m = str(user.user_id)
        s = m + '#' + user.username + '#' + user.password + '#' + user.full_name + '#' + user.user_type
        #print(s)
        userList.append(s)
    #filter(partial(is_not, None), userList)
    print(userList)


    users = session.query(Classes.DatabaseHandlers.create_table.Vendors).all()
    for user in users:
            m = str(user.vendor_id)
            s = m + '#' + user.company_name + '#' + user.contact_number
            vendorList.append(s)
    print(vendorList)

    users = session.query(Classes.DatabaseHandlers.create_table.Medicines).all()
    for user in users:
            m = str(user.medicine_id)
            s = m + '#' + user.medicine_name + '#' + user.medicine_type + '#' + user.company_name + '#' + str(user.price) + '#' + str(user.quantity) + '#' + str(user.expiry_date) + '#' + user.shelf + '#' + user.image_link
            medList.append(s)
    print(medList)

    users = session.query(Classes.DatabaseHandlers.create_table.Notifications).all()
    for user in users:
            m = str(user.notification_id)
            s = m + '#' + user.notification + '#' + str(user.time)
            notificationList.append(s)
    print(notificationList)

    users = session.query(Classes.DatabaseHandlers.create_table.Orders).all()
    for user in users:
            m = str(user.id)
            s = m + '#' + user.order_id + '#' + str(user.vendor_id) + '#' + user.company_name + '#' + user.medicine + '#' + str(user.quantity) + '#' + str(user.due_date) + '#' + str(user.status) + '#' + str(user.cost)
            orderList.append(s)
    print(orderList)

    users = session.query(Classes.DatabaseHandlers.create_table.Sellings).all()
    for user in users:
            m = str(user.sellings_id)
            s = m + '#' + str(user.money) + '#' + str(user.quantity) + '#' + str(user.date) + '#' + user.item + '#' + user.customer_name
            sellList.append(s)
    print(sellList)

    users = session.query(Classes.DatabaseHandlers.create_table.Expenses).all()
    for user in users:
            m = str(user.expenses_id)
            s = m + '#' + str(user.money) + '#' + str(user.quantity) + '#' + str(user.date) + '#' + user.item + '#' + user.vendor
            expenseList.append(s)
    print(expenseList)



Fetch()
session.close()