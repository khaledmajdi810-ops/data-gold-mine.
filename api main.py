from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="background:black;color:gold;text-align:center;padding-top:50px">
        <h1>🔥 DATA GOLD MINE</h1>
        <p>Status: ACTIVE</p>
        <a href="/buy" style="background:gold;color:black;padding:10px 20px;text-decoration:none">
        BUY NOW $10
        </a>
    </body>
    </html>
    """

@app.get("/buy")
def buy():
    return {"message": "Payment coming"}
