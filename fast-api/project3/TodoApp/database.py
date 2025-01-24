from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_ALCHEMY_CONNECTION_STRING="sqlite:///./todos.db"
"""
connection string to the database which SQLAlchemy will connect to.
"""

engine = create_engine(SQL_ALCHEMY_CONNECTION_STRING, connect_args={"check_same_thread": False})
"""
our database engine (driver)
"""

local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
"""
local session, without autoflush or autocommits, to our database.
"""

database = declarative_base()
"""
our abstracted database.
"""
