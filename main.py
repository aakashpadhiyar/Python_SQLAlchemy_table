from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from datetime import datetime
now = datetime.now()

Session = sessionmaker(bind = engine)
session = Session()


formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

meta = MetaData()

destination_table = Table(
   'destination', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('destination_id', Integer, primary_key = True), 
   Column(formatted_date, String), 
)

users_table = Table(
   'users', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('destination_id', Integer, primary_key = True), 
   Column(formatted_date, String), 
)


for d, u in session.query(destination_table, users_table).filter(destination.id == users.destination_id).all():
   print ("ID: {} Name: {} Destination No: {}".format(d.id,u.name, u.destination_id))