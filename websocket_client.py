import asyncio

import websockets


async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        message = 'Hello, server!'
        print(f'Sending: {message}')
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f'Server response: {response}')


asyncio.run(client())
