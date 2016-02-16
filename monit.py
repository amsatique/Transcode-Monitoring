import websocket
import json

def on_error(ws, error):
	print error

def on_close(ws):
	print "### closed ###"

def on_message(ws, message):
	msg_as_JSON = json.loads(message)
	type = msg_as_JSON.get("type")
	if type:
		if type == "auth":
			print("Auth completed")
		elif type != "user-notifications":
			print("{}:{}:{}".format(type, msg_as_JSON.get("state"), msg_as_JSON.get("resource_uri")))

def on_open(ws):
	print "Connected"

if __name__ == "__main__":
	websocket.enableTrace(True)
	token = 'e3b8ac3468b51b9116d3e4d8a25a9a30e937e9bc50384dfc';
	username = 'amsatique';

	ws = websocket.WebSocketApp('wss://stream.tutum.co/v1/events?token={}&user={}'.format(token, username),
		on_message = on_message,
		on_error = on_error,
		on_close = on_close,
		on_open = on_open)

	ws.run_forever() 