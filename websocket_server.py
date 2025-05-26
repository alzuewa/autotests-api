import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f'Got a message {message}')
        response = f'Server got: {message}'

        for _ in range(5):
            await websocket.send(response)


async def main():
    server = await websockets.serve(handler=echo, host='localhost', port=8765)
    print('Websocket Sever is running on ws://localhost:8765')
    await server.wait_closed()


asyncio.run(main())
