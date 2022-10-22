# 2 types of MQTT
- MQTT:
	- Based on TCP/IP
- MQTT-SN
	- Based on UDP
	- ?? For devices such as Zigbee

# How MQTT works
- There are 2 components in MQTT:
	- Broker
	- Client: which can be both
		- Publisher
		- Subscriber
- Publishers publish data to broker
- Clients subscribe to topic to broker
- Both broker and clients need to have a TCP/IP stack
- All data published in a topic is received by all clients who subscribe that topic
- A client can publish and subscribe at the same time
- **Clients are not aware of each other's existence**
- **Clients never contact each other directly**
- Broker does all the heavy lifting works in MQTT
	- Receiving, filtering and sending messages to subscribers
	- Storing session data for persistence sessions
	- Handle authentication and authorization of clients
- MQTT is not Message queuing
	- In message queue, data is consumed by only 1 client
	- Message queue must be created explicitly before any message is stored

# MQTT methods
- MQTT has 5 methods:

| HTTP   | MQTT        |        |
| ------ | ----------- | ------ |
| GET    | Connect     | Read   |
| POST   | Subscribe   | Create |
| PUT    | Unsubscribe | Update |
| PATCH  | Publish     | Change |
| DELETE | Disconnect  | Delete |

- Connect:
	- Client establishes a connection with broker
- Disconnect:
	- Client finishes all remaining work and close the TCP/IP connection
- Subscribe:
	- Client request broker to subscribe specific topics
- Unsubscribe
	- Client request broker to unsubscribe specific topics
- Publish:
	- Client send data to broker in order to publish in a topic

# Establish connection
- 3 stages:
	- TCP connection establishment
		- 3-way handshake between the client and broker
	- MQTT connection establishment and MQTT operation
	- TCP connection termination
		- Symmetric release

# MQTT features
- Wildcards
	- Subscribe multiple topics
- Quality of service
- Persistence session
- Retained message
- Last will
- Keep alive

# MQTT vs HTTP
- HTTP
	- Is synchronous
- MQTT
	- Is persistent
	- Reuse single connection to send multiple message

# MQTT vs AMQP and MQTT vs XMPP
- AMQP require high computation capability
- XMPP
	- Require more resource on both devices and network

# MQTT vs CoAP
- CoAP:
	- Is not yet standardized
	- Less reliable than TCP
	- Use for devices that sleep a long time
	- Prioritize battery consumption and computational overhead more than reliability of the message

# Assignment 1
1. Can multiple clients publish to the same topic?
	- Yes
2. Is it possible to know the identity of the client that published a message?
	- Only broker can identity the client because of TCP connection
3. What happens to messages that get published to topics that no one subscribes to?
	1. No one will receive the message
4. Can I subscribe to a topic that no one is publishing to?
	1. Yes
5. Are messages stored on the broker?
	1. Only if the connection is persistence or the message is retained message
6. In a Publish/Subscribe model, how does the publisher know who is subscribing?
	1. Publisher does not know, only broker knows
7. MQTT transmits data to and from a broker in which format?
	1. In Byte format
8. Each client that connects to a broker must have a unique client-id?
	1. yes
9. An MQTT broker can use any port, but by default, it uses port 1883. True or False?
	1. True
10. Messages sent to an MQTT broker are encrypted by default. True or False?
	1. False

#
---
- Status: #done
- Tags: #IoT
- References:
	- [Source](https://www.udemy.com/course/mqtt-masterclass/)
- Related:
