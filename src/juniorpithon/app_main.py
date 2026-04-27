import asyncio
import json
import os
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from juniorpithon.pi_network.pi_sdk import PiNetworkAppEngine
from juniorpithon.modules.edge_engines import JuniorHomeIoT, MarketTracker
from juniorpithon.modules.python_ide import OpenSourceIDE

app = FastAPI(title="JuniorPiThon App")

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

pi_engine = PiNetworkAppEngine()
iot_engine = JuniorHomeIoT()
market_engine = MarketTracker()
ide_engine = OpenSourceIDE()
active_clients = set()

class ScriptPayload(BaseModel):
    code: str
    user_id: str

@app.get("/")
async def root():
    return FileResponse(os.path.join(static_dir, "app.html"))

@app.post("/api/execute")
async def execute_code(payload: ScriptPayload):
    gas_receipt = pi_engine.charge_compute_gas(payload.user_id)
    result = ide_engine.execute(payload.code)
    return {"status": result["status"], "output": result["output"], "gas_paid": gas_receipt}

async def telemetry_stream():
    while True:
        if active_clients:
            payload = {"markets": market_engine.get_market_state(), "iot": iot_engine.get_telemetry()}
            manifest = json.dumps(payload)
            for client in list(active_clients):
                try: await client.send_text(manifest)
                except: active_clients.remove(client)
        await asyncio.sleep(1.0)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(telemetry_stream())

@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_clients.add(websocket)
    try:
        while True: await websocket.receive_text()
    except WebSocketDisconnect:
        active_clients.remove(websocket)

def launch():
    print("[*] Igniting JuniorPiThon Edge-Native App...")
    uvicorn.run("juniorpithon.app_main:app", host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    launch()
