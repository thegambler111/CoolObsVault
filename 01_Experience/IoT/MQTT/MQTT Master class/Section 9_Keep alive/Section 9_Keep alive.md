# Keep alive
- Keep alive feature is used to keep a connection alive
- In MQTT, keep alive let the application layer know that both sides are still connected

## How to setup Keep alive
- When establish connection, the client includes Keep alive timer in seconds in Connect message
- Keep alive timer is the maximum time that the broker and the client may not communicate
- You can disable Keep alive by setting the timer to 0

## How Keep alive works
- If the client does not send any message during the keep alive period, it must send a Ping request to the broker
	- To confirm that the client is still available
	- And make sure the broker is also still available
- If the broker is still available, it will response with a Ping response
- When the client receive the Ping response message, the keep alive timer is reset
- If there are any message exchange during keep alive period, there is no need to send Ping request

# Disconnection
- There are 2 causes of disconnection between the client and the broker:
	- The broker closes the connection to client if there are no message or request in 1.5 x keep alive time windows
	- The client closes the connection if it does not receive Ping response from the broker
- The client always try to reconnect

## Half connection
- Half-open connection is when one side of the connection is still functioning but does not know that the other side has disconnected.
- Sometimes, when a disconnected client tries to reconnect, the broker still has a half-open connection for that client
- If the broker detects a half open connection to a client, it perform client takeover:
	- The broker close the previous connection
	- Then establish new connection with the client
- For MQTT v3.1.1 client, the broker will terminate the TCP connection when performing client takeover
- For MQTT v5 client, the broke will send a Disconnect message before terminating the TCP connection
- Client takeover ensures that the half-open connection does not stop the disconnected client from re-establishing a connection.
#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
