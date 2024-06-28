import socketio
from aiohttp import web
sio=socketio.AsyncServer(cors_allowed_origins="*")
app=web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ):
    print(f"client {sid} conected to normal room")
    await sio.enter_room(sid, 'common_room')
@sio.event 
async def disconnect(sid):
    print(f"client {sid} off in normal room")
    await sio.leave_room(sid, 'common_room')
@sio.event
async def message(sid, data):
    print(f"conected from {sid}:{data}")
    await sio.emit('message', data, room="common_room", skip_sid=sid)
if __name__ == '__main__':
    web.run_app(app,port=5000)
