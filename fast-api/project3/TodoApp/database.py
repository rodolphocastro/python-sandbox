from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
connection string to the database which SQLAlchemy will connect to.
"""
SQL_ALCHEMY_CONNECTION_STRING="sqlite:///./todos.db"

"""
our database engine (driver)
"""
engine = create_engine(SQL_ALCHEMY_CONNECTION_STRING, connect_args={"check_same_thread": False})

"""
local session, without autoflush or autocommits, to our database.
"""
local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

"""
our abstracted database.
"""
database = declarative_base()
