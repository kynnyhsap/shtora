import asyncio
import websockets

from gpiozero import Motor
from time import sleep

motor = Motor(25, 24)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")

        if message == "open":
            motor.forward(1)
        elif message == "close":
            motor.backward(1)
        elif message == "stop":
            motor.stop()
        else:
            motor.stop()

        await websocket.send(f"Echo: {message}")


async def main():
    server = await websockets.serve(handler, "0.0.0.0", 3000)

    print("ws server started")

    await server.wait_closed()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("server stopped by user")
