from fastapi import APIRouter,WebSocket

router = APIRouter(
  prefix="/room",
  tags=["room",]
)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    await websocket.send_text(f"Message Text was: {data}")
