import asyncio
import websockets

async def hello(websocket):
    print(f"Connection established from {websocket.remote_address}")
    await websocket.send("Hello from the server!")

async def main():
    # Use your computer's local IP address
    server = await websockets.serve(hello, "0.0.0.0", 8765)
    print("WebSocket server started at ws://0.0.0.0:8765")
    await server.wait_closed()

asyncio.run(main())
