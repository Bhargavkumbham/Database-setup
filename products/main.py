from fastapi import FastAPI
from products.database import engine
from products.models import Base
from products.routes import products

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product API")

# Include product routes
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Welcome to Product API!"}
