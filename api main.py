from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Impero Protocol | Data Gold Mine</title>
            <style>
                body { background-color: #000; color: #ffd700; font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }
                .container { border: 2px solid #ffd700; display: inline-block; padding: 20px; border-radius: 10px; }
                h1 { letter-spacing: 5px; }
                button { background-color: #ffd700; color: #000; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>IMPERO PROTOCOL</h1>
                <p>Status: ONLINE | System: DATA GOLD MINE</p>
                <hr>
                <p>Welcome, Commander Khaled Magdy.</p>
                <button onclick="alert('Payment System Ready')">Access Protocol</button>
            </div>
        </body>
    </html>
    """
