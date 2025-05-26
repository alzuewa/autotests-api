import asyncio

import websockets


async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        await websocket.send('Hello, server!')

        for _ in range(5):
            server_message = await websocket.recv()
            print(server_message)


asyncio.run(client())
