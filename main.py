from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def getHealth ():
    return{"status":"ok"}