import asyncio
import websockets

async def hello():
    uri = "ws://xxx.xxx.xxx.xxx:8765"  # The URI must match the port on the server
    try:
        async with websockets.connect(uri) as websocket:
            response = await websocket.recv()  # Receive the message from the server
            print(f"Server response: {response}")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    asyncio.run(hello())
