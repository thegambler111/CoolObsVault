# Overview
>“MQTT is a Client Server publish/subscribe messaging transport protocol. It is light weight, open, simple, and designed so as to be easy to implement. These characteristics make it ideal for use in many situations, including constrained environments such as for communication in Machine to Machine (M2M) and Internet of Things (IoT) contexts where a small code footprint is required and/or network bandwidth is at a premium.“
>_Citation from the official [MQTT 3.1.1 specification](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html)_

- MQTT is a Client Server publish/subscribe messaging transport protocol
- It is light weight, open, simple, and easy to implement
- It requires small footprint and limited bandwidth

# MQTT Topics
## Definition
- A topic is an UTF-8 string that the broker uses to filter messages for each connected client
- Topic format:
	- The topic consists of one or more topic levels.
		- Each topic level is separated by a forward slash "/" (topic level separator).
	- Each topic must contain at least 1 character
	- Topic string permits empty spaces.
	- Topics are case-sensitive.
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT topic level.png]]
- Example:
```
myhome/groundfloor/livingroom/temperature
USA/California/San Francisco/Silicon Valley
5ff4a2ce-e485-40f4-826c-b1a5d81be9b6/status
Germany/Bavaria/car/2382340923453/latitude
```

- In comparison to a message queue, MQTT topics are very lightweight
- The broker accepts each valid topic without any prior initialization.

## MQTT Wildcards
- Wildcards is used to subscribe to multiple topics simultaneously
- You cannot use wildcards to publish
- There are two different kinds of wildcards: single-level and multi-level

### Single Level: +

- A single-level wildcard (plus symbol "+") replaces one topic level

![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT single level wildcard.png]]
- Any topic matches a topic with single-level wildcard if it contains an arbitrary string instead of the wildcard.
- For example: a subscription to _myhome/groundfloor/+/temperature_ can produce the following results:
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT single level wildcard example.png]]

### Multi Level: # 
- A multi-level wildcard (hash symbol "#") covers many topic levels
- The multi-level wildcard must be placed as the last character and preceded by a forward slash "/".
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT multi level wildcard.png]]
- When a client subscribes to a topic with a multi-level wildcard, it receives all messages from topics starting with the pattern before the wildcard character
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT multi level wildcard example.png]]

## MQTT Topics beginning with $
- Topics that start with a "$" symbol are reserved for internal statistics of the MQTT broker.
- These topics are not part of the subscription when you subscribe to the multi-level wildcard topic
- Clients cannot publish messages to these topics
- At the moment, there is no official standardization for such topics
	- Commonly, `$SYS/` is used for all internal information

## MQTT topic best practices

### Never use a leading forward slash
- The leading forward slash introduces an unnecessary topic level with a zero character at the front

### Never use spaces in a topic
- Spaces make it much harder to read and debug topics

### Keep the MQTT topic short and concise
- Each topic is included in every message in which it is used -> Long topic = long message

### Use only ASCII characters, avoid non printable characters
- Non-ASCII UTF-8 characters often display incorrectly -> Harder to debug

### Embed a unique identifier or the Client Id into the topic
- The unique identifier in the topic helps you identify who sent the message
- You can increase authorization by allowing only client with ID in the topic to publish to said topic

### Don’t subscribe to topic "#" 
- Subscribing to topic "#" means you will receive all messages going through a broker
- Frequently, the subscribing client will not be able to process all of those messages

### Extendable topics
- Topics should be extendable to allow for new features or products

### No multi-purpose topic
- Do not use a topic for multiple purpose
- For example, if you have three sensors in your living room, use 3 topics `livingroom/temperature`,`livingroom/brightness` and `livingroom/humidity` instead of 1 topic `livingroom`

# MQTT Publish/Subscribe Pattern

## Decoupling Pattern
- The decoupling pub/sub model: 
	- The connection between publisher and subscribers is handled by a third component (the broker) (no direct communication)
- Decoupling dimensions:
	- Space decoupling: Publisher and subscriber do not need to know each other (for example, no exchange of IP address and port).
	- Time decoupling: Publisher and subscriber do not need to run at the same time. Broker can store messages for clients that are not online
	- Synchronization decoupling: Operations on both components do not need to be interrupted during publishing or receiving.

## Scalability
- MQTT Pub/Sub scales better than the traditional client-server approach:
	- Broker operations are highly parallelized and messages are processed in an event-driven way
	- Scaling up to millions of connections can be achieved with clustered broker nodes and load balancers

## Message Filtering
- Broker manage to deliver correct messages to client using 3 filters:
- Subject-based filtering:
	- This filtering is based on the subject or topic that is part of each message
- Content-based filtering:
	- The broker filters the message based on a specific content filter-language
	- The downside of this method is that message content must be known beforehand and cannot be encrypted or easily changed.
- Type-based filtering:
	- This filter is based on the type/class of a message (event) in object-oriented languages

## Challenges
- You need to known the structure of published data beforehand
- For subject-based filtering, both publisher and subscriber need to know which topics to use
- It is possible that no subscriber reads a particular message


## MQTT vs Message queues
- MQTT stands for MQ Telemetry Transport
- A message queue stores message until they are consumed
- A message is only consumed by one client

| Message queue                                                     | MQTT                             |
| ----------------------------------------------------------------- | -------------------------------- |
| A message must be processed by a client or get stuck in the queue | A topic can have no subscriber   |
| A message is only consumed by one client                          | Every subscriber get the message |
| Queues are named and must be created beforehand                   | Topic can be created on the fly  | 

# MQTT connection between client and broker

## Client
- Both publishers and subscribers are MQTT clients
- An MQTT client is any device that runs an MQTT library and connects to an MQTT broker over a network
- The client implementation of the MQTT protocol is very straight forward, streamlined and is available for a huge variety of programming languages

## Broker
- The broker is responsible for
	- Receiving all messages
	- Filtering the messages
	- Determining who is subscribed to each message
	- Sending the message to these subscribed clients
	- Holding session data including subscriptions and missed messages
	- Authenticating and authorizing clients
- Your broker need to be:
	- Highly scalable
	- Integratable into backend systems
	- Easy to monitor
	- Failure-resistant

## MQTT connection
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT connect and connack.png]]
- The MQTT protocol is based on TCP/IP.
- 2 steps to initiate a connection
	- The client sends a CONNECT message to the broker.
	- The broker responds with a CONNACK message and a status code
- The broker keeps the connection until the client sends a disconnect command or the connection breaks
- There is no problem with clients that are located behind a network address translation (NAT) like router.

## CONNECT message
- MQTT 3.1.1 CONNECT message has the following components:
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT Connect message.png]]
### ClientId:
- The client identifier should be unique per client and broker
- You can send an empty ClientId to connect without any state but clean session flag must be set (NOTE: can set to any value or must be specific value?)

### Clean Session:
- The clean session flag tells the broker whether the client wants to establish a persistent session or not
- `CleanSession = false` -> Persistent session:
	- The broker stores all subscriptions for the client
	- If Quality of Service (QoS) level is 1 or 2, the broker will also store all missed messages
- `CleanSession = true` -> Not persistent session:
	- The broker does not store anything for the client 
	- The broker purges all information from any previous persistent session.

### Username/Password
- Username and password is used for client authentication and authorization
- Username and password should be encrypted or hashed

### Will Message
- The last will message is part of the Last Will and Testament (LWT) feature of MQTT
- The client can provide the broker with a last will in the form of an MQTT message and topic within the CONNECT message
- If the client disconnects ungracefully, the broker sends the LWT message on behalf of the client

### KeepAlive
- The keep alive defines the longest period of time that the broker and client can endure without sending a message
- The client send `PING Request`, the broker send `PING Response` to determine if other one is still available

## CONNACK message
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT Connack message.png]]
- The CONNACK message contains two data entries:

### Session Present flag
- The session present flag tells the client whether the broker already has a persistent session available from previous interactions with the client
- If client connects with `CleanSession = true`, the session present flag is always false
- If client connects with `CleanSession = false`:
	- If the broker stored session information for the clientId, `SessionPresent = true`
	- If the broker does not have any session information for the clientId, `SessionPresent = false`

### Connect return code
- This flag is a code that tells whether the connection attempt was successful or not.

| Return Code | Return Code Response                             |
| ----------- | ------------------------------------------------ |
| 0           | Connection accepted                              |
| 1           | Connection refused, unacceptable protocol versio |
| 2           | Connection refused, identifier rejected          |
| 3           | Connection refused, server unavailable           |
| 4           | Connection refused, bad user name or password    |
| 5           | Connection refused, not authorized               | 

# MQTT Publish, Subscribe & Unsubscribe
## Publish
![[01_Experience/IoT/MQTT/MQTT Essentials/MQTT Publish.png]]
- Each message *must* contain a topic that the broker can use to forward the message to interested clients.
- Each message *should* has a payload which contains the data to transmit in byte format.
- The publisher decides payload format
- When receiving a message, the broker
	- Reads the message
	- Acknowledges the message (according to the QoS Level)
	- Processes the message: Identify and send the message to subscribers

### Packet Identifier
- The packet identifier uniquely identifies a message 
- The packet identifier is only relevant for QoS levels greater than zero
- If `QoS = 0`, `packetId = 0`

### Topic Name
- Topic name is used to filter message

### QoS
- This number indicates the Quality of Service Level (QoS) of the message
- There are three levels: 0, 1, and 2.
- It determines what kind of guarantee a message has for reaching the intended recipient (client or broker)

### Retain Flag
- This flag defines whether the message is saved by the broker for a specified topic
- When a new client subscribes to a topic, they receive the last retained message on that topic

### Payload
- This is the actual content of the message

### DUP flag
- The flag indicates that the message was resent because the intended recipient (client or broker) did not acknowledge the original message
- This only happens when QoS > 0

## Subscribe












# 

---
- Status: #done

- Tags: #mqtt

- References:
	- [Source](https://www.hivemq.com/mqtt-essentials/)

- Related:
	- 
