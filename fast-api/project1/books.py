from fastapi import FastAPI
import logging

logger = logging.getLogger("uvicorn") # use the FastAPI (uvicorn) logger

logger.info("starting the FastAPI server...")
app = FastAPI() # instantiate the FastAPI class, which we'll be attaching methods to

# creating a method that'll listen to GET requests on the / route of our server
@app.get("/")
def say_hello():
    logger.info("greeting an user")
    return {"message": "Hello, World!"}
