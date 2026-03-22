from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
    <head>
        <title>DATA GOLD MINE</title>
        <style>
            body {
                background-color: #000;
                color: #ffd700;
                font-family: Arial;
                text-align: center;
                padding-top: 50px;
            }
            .box {
                border: 2px solid #ffd700;
                padding: 20px;
                display: inline-block;
                border-radius: 10px;
            }
            a {
                background: #ffd700;
                color: #000;
                padding: 10px 20px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🔥 DATA GOLD MINE</h1>
            <p>System: ACTIVE</p>
            <p>Auto Data Selling Engine</p>
            <br>
            <a href="/buy">BUY NOW ($10)</a>
        </div>
    </body>
    </html>
    """

@app.get("/buy")
async def buy():
    return {"message": "Payment system will go here"}
