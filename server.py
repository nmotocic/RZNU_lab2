import websockets
import html
import asyncio


async def communication_handler(websocket, path):
    global clients
    name = await websocket.recv()
    clients.add(websocket)
    for client in clients:
        await client.send("{} join the converstaion!".format(name))

    while True:
        try:
            message = await websocket.recv()
            message = html.escape(message)
            new_message = "<b>{}:</b> {}".format(name, message)
            for client in clients:
                await client.send(new_message)
        except:
            client.remove(websocket)


if __name__ == "__main__":
    clients = set()
    start_server = websockets.serve(communication_handler, 'localhost', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
