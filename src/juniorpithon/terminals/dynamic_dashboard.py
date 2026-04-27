import asyncio
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from juniorpithon.ide.dynamic_sandbox import SovereignSandbox
from juniorpithon.core.token_economy import PiTokenEcosystem

app = FastAPI(title="JuniorPiThon Ecosystem")
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

sandbox = SovereignSandbox()
economy = PiTokenEcosystem()
active_clients = set()

# Mock script demonstrating IDE capability
MOCK_USER_SCRIPT = """
# User-defined logic executed in JuniorPiThon IDE
import random

battery_v = 48.0 + random.uniform(-1.0, 1.0)
rsi = random.uniform(20, 80)

jc_ui.metric("JuniorHome 48V SoC", round(battery_v, 2), "positive" if battery_v > 47.5 else "negative")
jc_ui.metric("BTC-USD RSI", round(rsi, 2), "negative" if rsi > 70 else "neutral")
jc_ui.log("Executing edge analysis cycle...")
"""

@app.get("/")
async def serve_dashboard():
    return FileResponse(os.path.join(static_dir, "index.html"))

async def broadcast_loop():
    while True:
        if active_clients:
            # Execute the user's IDE script to generate the UI payload
            script_result = sandbox.execute_user_script(MOCK_USER_SCRIPT)
            manifest = json.dumps({"engine": script_result})
            
            for client in list(active_clients):
                try: await client.send_text(manifest)
                except: active_clients.remove(client)
        await asyncio.sleep(2.0)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(broadcast_loop())

@app.websocket("/ws/terminal")
async def terminal_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_clients.add(websocket)
    try:
        while True: await websocket.receive_text()
    except WebSocketDisconnect:
        active_clients.remove(websocket)
