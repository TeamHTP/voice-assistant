import asyncio
import websockets

async def send(message):
    uri = "ws://localhost:5678"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)


def send_start():
    asyncio.get_event_loop().run_until_complete(send('start'))


def send_stop():
    asyncio.get_event_loop().run_until_complete(send('stop'))