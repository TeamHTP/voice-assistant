import asyncio
import websockets

connected_sockets = []


def send_start():
    global connected_sockets
    for ws in connected_sockets:
        ws.send('start')


def send_stop():
    global connected_sockets
    for ws in connected_sockets:
        ws.send('stop')


async def conn(ws, path):
    global connected_sockets
    connected_sockets.append(ws)

start_server = websockets.serve(conn, "localhost", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()