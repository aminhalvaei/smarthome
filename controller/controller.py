from fastapi import FastAPI, HTTPException, BackgroundTasks
from datetime import datetime, timedelta
import asyncio
import httpx

from configs import configs

app = FastAPI()

async def get_weather_condition():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{configs.SERVER_URL}/api/cservice/weather-condition/", params={"physical_id": configs.CONTROLLER_PHYSICAL_ID})
        response.raise_for_status()
        return response.json()

async def set_status():
    async with httpx.AsyncClient() as client:
        payload = {"physical_id": configs.CONTROLLER_PHYSICAL_ID}
        response = await client.post(f"{configs.SERVER_URL}/api/cservice/set-status/", json=payload)
        response.raise_for_status()

async def periodic_task():
    while True:
        # Get new status data from weather-condition endpoint
        weather_condition = await get_weather_condition()
        print("Received new status data:", weather_condition)
        
        # TODO to debug: remove it in production
        await asyncio.sleep(5)

        # Acknowledge the arrival and register of new status data using set-status endpoint
        await set_status()
        print("Acknowledged arrival and registered new status data.")

        # Sleep for 5 minutes before the next iteration
        await asyncio.sleep(configs.VALIDATION_INTERVAL_IN_SECONDS)

@app.on_event("startup")
async def startup_event():
    # Start the periodic task in the background
    asyncio.create_task(periodic_task())

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
