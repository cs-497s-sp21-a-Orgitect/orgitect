#~/service/actor-server/app/api/db.py
import os
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY,ForeignKey)

from databases import Database

DATABASE_URL ='postgresql://gyd:secret@localhost/postgres'
#DATABASE_URL = 'postgresql://localhost:5432/postgres'

engine = create_engine(DATABASE_URL)

metadata = MetaData()

actor = Table(
    'actor',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('ac_name', String(50)),
    Column('ac_email', String(250)),
    Column('ac_dept', String),
    Column('ac_customer', ARRAY(String)),
    Column('sid',ARRAY(Integer))
)


database = Database(DATABASE_URL)