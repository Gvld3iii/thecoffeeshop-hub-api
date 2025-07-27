from fastapi import FastAPI
from app.routes import auth, lemonsqueezy_routes

app = FastAPI()

@app.get("/")
def home():
    return {"message": "The Brew API is running"}

app.include_router(auth.router)
app.include_router(lemonsqueezy_routes.router)
