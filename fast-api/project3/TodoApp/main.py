from fastapi import FastAPI
import models
from database import engine

app = FastAPI()
"""
our fastapi application
"""

models.database.metadata.create_all(bind=engine)
