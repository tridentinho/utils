import socketio, sys, time, os

API_BASE = os.getenv('API_BASE', None)
NAMESPACE = os.getenv('NAMESPACE', None)
TOKEN = os.getenv('TOKEN', None)

args = sys.argv[1:]
name = args[0]
status = args[1]

# standard Python
sio = socketio.Client()

sio.connect('http://localhost:8080', namespaces=['/', '/automations'], headers={'authorization':TOKEN})

sio.emit('status', {'automation':str(name), 'status':str(status)}, namespace='/automations')
#sio.emit('detail', {'automation':str(name), 'detail':{'name':'vpn', 'value':str(status)}}, namespace='/automations')
#sio.emit('command', {'automation':str(name), 'command':str(status)}, namespace='/automations')
#sio.emit('log', {'automation':str(name), 'log':str(status)}, namespace='/automations')

time.sleep(5)
sio.disconnect()