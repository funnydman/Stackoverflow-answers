#!/usr/bin/env python

import asyncio

import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    greeting = f"Hello {name}!"

    await websocket.send(greeting)


HOST = '0.0.0.0'
PORT = 8765

start_server = websockets.serve(
    hello, HOST, PORT
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
