from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

latest_data = {
    "intent": "-",
    "topic": "-",
    "sentiment": "-",
    "escalation_risk": "-"
}

@app.get("/")
def home():
    with open("templates/dashboard.html") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    global latest_data

    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()

            latest_data = data

            print("Received:", latest_data)

    except WebSocketDisconnect:
        print("Client disconnected")

@app.websocket("/dashboard")
async def dashboard_ws(websocket: WebSocket):

    global latest_data

    await websocket.accept()

    try:
        while True:
            await websocket.send_json(latest_data)

            import asyncio
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        print("Dashboard disconnected")