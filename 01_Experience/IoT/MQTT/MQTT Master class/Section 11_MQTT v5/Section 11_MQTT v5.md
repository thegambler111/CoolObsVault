# MQTT v5 functional objectives
- Enhancement for scalability and large scale systems
- Improved error reporting
- Formalize common patterns including discovery and request-response
- Extensibility mechanisms including user properties
- Performance improvements and support for small clients

## User properties
- Similar to HTTP, MQTT client and broker can add several custom or predefined headers to carry metadata
- This metadata can be used for application specific data
- Metadata are string key-value pair
- Metadata can be applied to any MQTT packets
![[01_Experience/IoT/MQTT/MQTT Master class/Section 11_MQTT v5/Metadata.png]]

## Auth packet
- Auth packet is used for authentication

![[01_Experience/IoT/MQTT/MQTT Master class/Section 11_MQTT v5/Auth packet.png]]

## More reason codes
- Improve client feedback
- Reason code is carried in Ack packets
- Reason code allows clients and brokers interpret error condition and find a workaround
- [List of reason codes](https://www.emqx.com/en/blog/mqtt5-new-features-reason-code-and-ack)

### Reason string
- You can also use a reason string instead of code for more human readable

## Server capability information
- In properties field of ConnAck packet, the server can provide capability information to the client

## Clean start replace Clean session
- A client can initiate a clean start by using `cleanStart` flag in the Connect message
- How it work:
	- The broker will discard any data of the previous session
	- Then the client start with a fresh session

## Session expiry interval
- In the CONNECT packet, a connecting client can set a session expiry interval in seconds
	- This interval defines the period of time that the broker stores the session information of the client after disconnection

## Message expiry interval
- A client can set the message expiry interval in seconds for each PUBLISH message individually
- This interval defines the period of time that the broker stores the PUBLISH message for any matching subscribers that are not currently connected
- When no message expiry interval is set, the message is stored indefinitely.
- When the `retained=true`, this interval also defines how long a message is retained on a topic.

## Bi-direction disconnect packet
- The broker is now able to send Disconnect packet with reasons when it want to close the connection
- There are 4 reason code for broker disconnection:
	- Server busy
	- Server shutdown
	- Keep alive timeout
	- Session taken over

## Shared subscription
- Clients are able to share the same subscription on the broker
- All clients in the same subscription group receive messages in an alternating fashion.
- This mechanism is sometimes called client load balancing

## Using password without username
- This feature is useful when authenticating using token

## Topic alias
- Topic alias is used to reduce the size of topic field
- Topic alias is integer value that can be used as a substitute for topic names
- Publisher can send topic alias
- Publisher can set the topic alias value in the Publish message following the topic name.
- The Broker then created a mapping between the Topic Alias and Topic Name
- Any following PUBLISH message of the same topic can then be sent with Topic Alias and empty topic name
![[01_Experience/IoT/MQTT/MQTT Master class/Section 11_MQTT v5/Topic alias.png]]

## Properties
- Connection properties
	- Maximum packet size:
		- Maximum packet size that the broker can send to the client
	- Topic alias maximum:
		- Limit the topic alias the client can hold
- Authentication:
	- Authentication method
	- Authentication data
		- Authentication data depends on Authentication method
- User properties:
	- Payload structure
	- Publisher information
	- Message number
	- Timestamp
	- Routing information
	- etc.
- Payload format indicator:
	- 0: Unspecific byte stream (This is default value)
	- 1: UTF-8
- Content type:
	- Define the payload specific

## Subscription identifier
- You can define subscription identifier
- Subscription identifier can be used to filter message

## Nonlocal publishing
- If you subscribe to the same topic you publish on:
	- In MQTTv3, you will receive your messages
	- In MQTTv5, the broker will no longer send you your messages

## Retain message control
- The Subscribe message can control what retained message the client want to received
	- Retain handling = 0, the broker will send all retained messages
	- Retain handling = 1,
		- If the subscription has not already existed, the broker will send all retained messages of that topic
		- f the subscription has already existed, the broker will send retained messages
	- Retain handling = 2the broker will not send any retained messages






# MQTTv5 disadvantage
- If no new MQTTv5 features are used, there are almost no increment of computational and bandwidth cost
- User properties is the new feature that introduces the most extra computational overhead
- MQTTv5have limited client and broker library support (only in limited languages)

#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
