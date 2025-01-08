from fastapi import FastAPI

print("starting the api")
app = FastAPI() # instantiate the FastAPI class, which we'll be attaching methods to

# creating a method that'll listen to GET requests on the / route of our server
@app.get("/")
def say_hello():
    return {"message": "Hello, World!"}
