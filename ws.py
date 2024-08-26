import asyncio
import websockets
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

s = servo.ContinuousServo(pca.channels[0], min_pulse=700, max_pulse=2500)


async def handler(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")

        if message == "open":
            s.throttle = 1
        elif message == "close":
            s.throttle = -1
        elif message == "stop":
            s.throttle = 0
        else:
            s.throttle = 0

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
    finally:
        pca.deinit()
