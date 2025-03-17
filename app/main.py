from fastapi import FastAPI
from datetime import datetime
import zoneinfo
from models import Transaction, Invoice
from db import SessionDep, create_all_tables
from sqlmodel import select
from .routers import customers

app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)

@app.get("/")
async def root():
    return {"message": "Hola Mi nombre es Wilmer"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}
     
@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data
