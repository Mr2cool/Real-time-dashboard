from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette import EventSourceResponse
from utils import SensorData, recent_readings
import json
import asyncio
import arel
import os

app = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")
sensor = SensorData()

# Hot reload magic for development (because restarting servers is for losers)
if os.getenv("DEBUG"):
    hot_reload = arel.HotReload(paths=["."])
    app.add_websocket_route("/hot-reload", route=hot_reload)
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chart-data", response_class=HTMLResponse)
async def chart_data(request: Request):
    return templates.TemplateResponse("chart_data.html", {"request": request})

@app.get("/sse")
async def sse_data():
    async def event_generator():
        while True:
            new_reading = sensor.generate_reading()
            recent_readings.append(new_reading)

            yield {"event": "new_data", "data": json.dumps(new_reading)}
            await asyncio.sleep(1) # Send data every 1 second
    return EventSourceResponse(event_generator())