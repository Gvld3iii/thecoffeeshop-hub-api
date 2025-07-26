from fastapi import FastAPI
from app.routes import auth, lemonsqueezy_routes

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(auth.router, prefix="/auth")
app.include_router(lemonsqueezy_routes.router, prefix="/payment")
