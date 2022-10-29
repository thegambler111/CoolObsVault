# MQTT packet format
- MQTT packet sits on top of the TCP layer
- **Maximum packet size is 256MB**
- 3 parts:
	- Fixed header
	- Variable header
	- Payload
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/Packet format.jpg]]

## Fixed header
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/Fixed header.png]]
- Always present
- 2-5 bytes in length
	- Control header:
		- 1 byte
		- = Message type + Header flag
	- Packet length:
		- 1-4 bytes length

### Message type
- [Source](https://openlabpro.com/guide/mqtt-packet-format/)
| Bit | Value | Direction | Description |
| --- | ----------- | ---------------- | ----------------------------------- |
| 0 | Reserved | x |                                     |
| 1 | Connect | Client -> Server | Client request to connect to server |
| 2 | ConnAck | Server -> Client | Connect acknowledgement |
| 3 | Publish | C -> S or S -> C | Publish message |
| 4 | PubAck | C -> S or S -> C | Publish acknowledgement |
| 5 | PubRec | C -> S or S -> C | Publish receive |
| 6 | PubRel | C -> S or S -> C | Publish release |
| 7 | PubComp | C -> S or S -> C | Publish complete |
| 8 | Subscribe | Client -> Server | Client subscribe request |
| 9 | SubAck | Server -> Client | Subscribe acknowledgement |
| 10 | Unsubscribe | Client -> Server | Unsubscribe request |
| 11 | UnsubAck | Server -> Client | Unsubscribe acknowledgement |
| 12 | PingReg | Client -> Server | Ping request |
| 13 | PingResp | Server -> Client | Ping response |
| 14 | Disconnect | Client -> Server | Client is disconnecting |
| 15 | Reserved | x |                                     |

### Header flag
- Header flag are only used by Publish message
	- In other message, all 4 bits will be set to 0
- Dup:
	- Value:
		- 0: First time deliver message
		- 1: Re-deliver message
	- Indicate to the receiver that this message may have already been received
	- Possible message type:
		- Publish
		- PubRel
		- Subscribe
		- Unsubscribe
- QoS level
	- 0: At most 1
	- 1: At least 1
	- 2: Exactly 1
	- 3: Reserved
- Retain:
	- 0: Broker will not hold the message
	- 1: Broker retain the last received PUBLISH message

## Remaining length
- Remaining length = Length of Variable header + Payload
- Each byte:
	- Most significant bit: Continuation flag
		- 0: This is the last byte of the remaining length 
		- 1: Next byte is also in the remaining length 
	- 7 other bit: Length information

# Specific MQTT packet format

## Connect
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/Connect.jpg]]
## ConnAck
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/ConnAck.jpg]]
## Publish
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/Publish.jpg]]

## PubAck
- Only use in QoS=1
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/QoS 1.png]]
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/PubAck.jpg]]

## PubRec
- Only use in QoS=2
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/QoS 2.png]]
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/PubRec.jpg]]

## PubRel
- Only use in QoS=2
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/PubRel.jpg]]

## PubComp
- Only use in QoS=2
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/PubComp.jpg]]
## Subscribe
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/Subscribe.jpg]]

## SubAck
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/SubAck.jpg]]

## Unsubcribe
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/Unsubscribe.jpg]]

## UnsubAck
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/UnsubAck.jpg]]

## PingReq, PingResp and Disconnect
![[01_Experience/IoT/MQTT/MQTT Master class/Section 2_MQTT packets/PingReq, PingResp and Disconnect.png]]


# Keepalive

- If `keepalive = 5 seconds`
	- After 5 seconds without communication with broker, client send a PingReq
	- The broker then response with PingResp
	- If the broker is unreachable for more than 1.5 x `keepalive` (7.5s), the client will close the connection with the broker











#
---
- Status: #done
- Tags: #IoT
- References:
	- [Source]()
- Related:
