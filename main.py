from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pandas as pd
import requests
import stripe
import time, threading, os

# ---------------- CONFIG ----------------
# ضع مفتاح Stripe الخاص بك هنا (تأكد من شحن 5 دولار في OpenAI لاحقاً)
STRIPE_SECRET = "sk_test_51QuQk0P2O6u..." 
STRIPE_PRICE = 10 
DOMAIN = "https://data-gold-mine.onrender.com"
FILE = "leads.csv"

stripe.api_key = STRIPE_SECRET
app = FastAPI()

# ---------------- DATA ENGINE ----------------
def collect_data():
    # هنا قمنا بتغيير المصدر لبيانات أكثر قيمة (مثال: شركات تقنية)
    data = [
        {"Company": "Emaar", "Industry": "Real Estate", "Location": "Dubai"},
        {"Company": "NEOM", "Industry": "Tech/Urban", "Location": "Saudi Arabia"},
        {"Company": "Damac", "Industry": "Real Estate", "Location": "Dubai"}
    ]
    df = pd.DataFrame(data)
    df.to_csv(FILE, index=False)

def loop():
    while True:
        collect_data()
        time.sleep(86400)

threading.Thread(target=loop, daemon=True).start()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="font-family:Arial;text-align:center;background:#f4f4f4;padding-top:100px">
        <h1 style="color:#2c3e50">🔥 Premium Middle East Business Leads</h1>
        <p>Verified data for Real Estate and Tech sectors. Updated daily.</p>
        <a href="/buy" style="background:#27ae60;color:white;padding:15px 30px;text-decoration:none;border-radius:5px;font-weight:bold">Buy Leads Pack ($10)</a>
    </body>
    </html>
    """

@app.get("/buy")
def buy():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price_data": {"currency": "usd", "product_data": {"name": "Business Leads Pack"}, "unit_amount": STRIPE_PRICE * 100}, "quantity": 1}],
        mode="payment",
        success_url=DOMAIN + "/download",
        cancel_url=DOMAIN,
    )
    return {"url": session.url}

@app.get("/download")
def download():
    if os.path.exists(FILE):
        return FileResponse(FILE, filename="premium_leads.csv")
    return {"error": "File generation in progress..."}
