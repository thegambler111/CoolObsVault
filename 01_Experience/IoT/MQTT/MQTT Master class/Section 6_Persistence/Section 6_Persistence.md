# Persistence
- Persistence is preserve the communication when the client and broker connection is interrupted
	- To prevent reconnection
		- No Subscribe message
		- No new session
- To activate Persistence, in Connect message, set `CleanSession` flag to 0
	- All information and messages queues in previous session will be stored
- Stored information in broker:
	- Topics subscribed or published by client
	- QoS 1 and QoS 2 undelivered messages
	- QoS 2 messages that are not yet ack by client
- Stored information in client:
	- QoS 1 and QoS 2 messages that are not yet ack by broker
	- All QoS 2 messages received from the broker that are not yet completely ack
- Broker matches sessionID with clientID to find the persistence session of a specific client
- Number of undelivered messages stored in a persistence session by broker depends on broker setup

## Use cases of persistence session
- The client must get all the messages from a certain topic, even if it is offline
- The client has limited resources and connectivity
- The client needs to resume all QoS 1 and 2 publish messages after a reconnect

## Use cases of clean session
- The client needs to publish message to topics, and does not need to subscribe to topics
- You don't want the broker to store session information or retry transmission for QoS 1 and 2 messages
- The client does not need to get messages that it messes when offline

# Retained message
- When `retainedMessage = true`, the subscriber will always receive to the last published message
- When `cleanSession = false` (persistence session) and QoS of both subscribe and publish is >= 1, all undelivered messages will be retained and retransmitted
- => Retain is independent of the session persistence
- => Retain only stores message while persistence store both undelivered messages and subscriber client information
- QoS 1 and QoS 2 react the same way for session persistence
![[01_Experience/IoT/MQTT/MQTT Master class/Section 6_Persistence/Retained messages.png]]

#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
