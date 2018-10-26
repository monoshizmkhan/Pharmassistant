from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask_sqlalchemy import SQLAlchemy
import Classes.DatabaseHandlers.create_table as create_table, Classes.DatabaseHandlers.fetch as fetch
import sqlalchemy

Base = declarative_base()


engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/pharmassistant')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()


def Add(table, list):
    s = str(table)
    sp = list.split('#')

    if s == "<class 'Classes.DatabaseHandlers.create_table.Users'>":
        user = create_table.Users()
        user.username = sp[1]
        user.full_name = sp[2]
        user.password = sp[3]
        user.user_type = sp[4]
        session.add(user)
        session.commit()

    elif s == "<class 'Classes.DatabaseHandlers.create_table.Vendors'>":
        user = create_table.Vendors()
        user.company_name = sp[1]
        user.contact_number = sp[2]
        session.add(user)
        session.commit()


    elif s == "<class 'Classes.DatabaseHandlers.create_table.Medicines'>":
        user = create_table.Medicines()
        user.company_name = sp[3]
        user.medicine_name = sp[1]
        user.medicine_type = sp[2]
        user.shelf = sp[7]
        user.image_link = sp[8]
        user.quantity = sp[5]
        user.price = sp[4]
        user.expiry_date = sp[6]
        session.add(user)
        session.commit()

    elif s == "<class 'Classes.DatabaseHandlers.create_table.Orders'>":
        user = create_table.Orders()
        user.order_id = sp[1]
        user.vendor_id = sp[2]
        user.company_name = sp[3]
        user.medicine = sp[4]
        user.quantity = sp[5]
        user.due_date = sp[6]
        user.status = sp[7]
        user.cost = sp[8]
        session.add(user)
        session.commit()


    elif s == "<class 'Classes.DatabaseHandlers.create_table.Notifications'>":
        user = create_table.Notifications()
        user.notification = sp[1]
        user.time = sp[2]
        session.add(user)
        session.commit()


    elif s == "<class 'Classes.DatabaseHandlers.create_table.Sellings'>":
        user = create_table.Sellings()
        user.money = sp[1]
        user.quantity = sp[2]
        user.date = sp[3]
        user.item = sp[4]
        user.customer_name = sp[5]
        session.add(user)
        session.commit()


    elif s == "<class 'Classes.DatabaseHandlers.create_table.Expenses'>":
        user = create_table.Expenses()
        user.money = sp[1]
        user.quantity = sp[2]
        user.date = sp[3]
        user.item = sp[4]
        user.vendor = sp[5]
        session.add(user)
        session.commit()


addList = '01#Flonase#Allergies#Flonase#30#3#2020-01-01#20C#/static/Images/flonase.jpg'
#Add(create_table.Medicines, addList)
session.close()