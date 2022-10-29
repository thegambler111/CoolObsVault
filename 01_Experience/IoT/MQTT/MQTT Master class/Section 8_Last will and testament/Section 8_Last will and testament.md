# Ungraceful disconnected
- Ungraceful disconnection happens when client disconnect from broker without sending a Disconnect message
	- Usually, when a client intentionally disconnected from a broker, it send a Disconnect message
	- However, when a disconnection happens due to loss of connection or hardware failure, the broker will not receive any Disconnect message

# Last will and testament (LWT)
- The last will and testament help client to response to ungraceful disconnection
- Using LWT, client tell broker to publish a predefined message if the client disconnect ungracefully
- You can not change properties of the LWT message

## How LWT works
- When connecting to a broker, the client send last will message and its properties in Connect message
	- LW topic
	- LW message
	- QoS
	- Retain message flag
- When ungraceful connection happens, the broker sends the LW message to all subscribers of the LW topic
- On the other hand, when the client disconnect gracefully, the broker will discard the LW message

# Real life implementation of LWT
- There are 5 scenarios which LWP is invoked
	- The broker detects an I/O Error
	- The broker detects a network failure
	- The client fails to communicate within the defined keep alive period
	- The client ungracefully disconnects
	- The broker closes connection due to Protocol error



#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
