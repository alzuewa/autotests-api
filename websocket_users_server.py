import asyncio

import websockets
from websockets import ServerConnection


async def handle_connection(websocket: ServerConnection):
    async for message in websocket:
        print(f'Got a message from user: {message}')
        response = f'User message: {message}'

        for i in range(5):
            await websocket.send(f'{i + 1} {response}')


async def main():
    server = await websockets.serve(handler=handle_connection, host='localhost', port=8765)
    await server.wait_closed()


asyncio.run(main())
