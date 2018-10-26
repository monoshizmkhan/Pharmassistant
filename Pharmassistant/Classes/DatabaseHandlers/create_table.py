from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Numeric, Date, Time, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    user_id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50), unique=True)
    password = Column('password', String(50))
    full_name = Column('full_name', String(50))
    user_type = Column('user_type', String(50))


class Vendors(Base):
    __tablename__ = "vendors"

    vendor_id = Column('vendor_id', Integer, primary_key=True)
    company_name = Column('company_name', String(50), unique=True)
    contact_number = Column('contact_number', String(50))


class Medicines(Base):
    __tablename__ = "medicines"

    medicine_id = Column('medicine_id', Integer, primary_key=True)
    medicine_name = Column('medicine_name', String(50))
    medicine_type = Column('medicine_type', String(50))
    company_name = Column('company_name', String(50))
    price = Column('price', Float)
    quantity = Column('quantity', Numeric(50))
    expiry_date = Column('expiry_date', Date)
    shelf = Column('shelf', String(50))
    image_link = Column('image_link', String(50))



class Orders(Base):
        __tablename__ = "orders"

        id = Column('id', Integer, primary_key=True)
        order_id = Column('order_id', String(50))
        vendor_id = Column('vendor_id', Integer)
        company_name = Column('company_name', String(50))
        medicine = Column('medicine', String(50))
        quantity = Column('quantity', Numeric(50))
        due_date = Column('due_date', Date)
        status = Column('status', String(50))
        cost = Column('cost', Numeric(50))


class Notifications(Base):
    __tablename__ = "notifications"

    notification_id = Column('notification_id', Integer, primary_key=True)
    notification = Column('notification', String(50))
    time = Column('time', Time)


class Sellings(Base):
        __tablename__ = "sellings"

        sellings_id = Column('sellings_id', Integer, primary_key=True)
        money = Column('money', Numeric(50))
        quantity = Column('quantity', Numeric(50))
        date = Column('date', Date)
        item = Column('item', String(50))
        customer_name = Column('customer_name', String(50))


class Expenses(Base):
            __tablename__ = "expenses"

            expenses_id = Column('expenses_id', Integer, primary_key=True)
            money = Column('money', Numeric(50))
            quantity = Column('quantity', Numeric(50))
            date = Column('date', Date)
            item = Column('item', String(50))
            vendor = Column('vendor', String(50))

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/pharmassistant')
Base.metadata.create_all(bind=engine)
