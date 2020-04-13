import request
import sqlalchemy
import psycopg2

import sqlalchemy as db
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, Float, Boolean, DateTime, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import func
from sqlalchemy import Table, MetaData

#POST an HHTP request with a valid expression to the server Examine the response and confirm that the correct answer is returned.
def test_post_valid(self):
    expected_result = { "expression": "1+1"}
    r = requests.post('https://localhost:5000/add', data = expected_result)
    assert r.status_code is 200

#Establish a connection to the database directly and verify that the string you sent has been correctly stored in the database. 
#For this step, you can use SQLAlchemy, or write the SQL directly if you prefer, however note that this is a postgres database which does have subtly different syntax from sqlite. (For simple queries this shouldn't be a big issue.)
Base = declarative_base()
class Data(Base):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))

DATABASE_URI = 'postgresql://cs162_user:cs162_password@db/cs162'
engine = create_engine(DATABASE_URI)

metadata = MetaData(engine)
data = Table('Data', metadata, autoload=True)

Session = sessionmaker(bind=engine)
session = Session() 

def test_input(self):
	session.add(text="Hello CS162")
	q = db.select([Data.columns.id, Data.columns.text]).select_from(Data)
	result = connection.execute(q).fetchall()[-1]

	assertEqual(result, "Hello CS162")

# #POST an HTTP request with an invalid expression to the server. Examine the response and confirm that an error is raised.
def test_post_invalid(self):
    expected_result = { "expression": "hello"}
    r = requests.post('https://localhost:5000/add', data = expected_result)
    assertFalse(r.status_code == 200) 
#Confirm that no more rows have been added to the database since the last valid expression was sent to the server. 
#(For the purposes of this class, you can assume that no-one else is accessing the database while the tests are running.)

#If any of the tests fail, then your program should raise an exception, and stop running. Your program should only complete successfully if all tests pass.
