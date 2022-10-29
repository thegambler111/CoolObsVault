# Quality of service

## QoS 0
- QoS 0 = Best effort delivery model
	- No Ack -> No guarantee of delivery
	- No re-transmission
- Usage:
	- When data is send frequently
		- Some information lost is acceptable
	- When the connection is very stable
	- When the power consumption is limited

## QoS 1
- QoS 1 guarantees that the message is received at least 1 time
	- After a predefined time without Ack, the message is  published again
- Usage:
	- The application must receive every message
	- The application can filter duplicates
	- The application can not handle the overhead of QoS 2

## QoS 2
- QoS 2 guarantees that the message is received only 1 time
	- The delivery guarantee is achieved by a 4 part handshake
- This is the slowest method
- 4 part handshake:
	- Publisher -> BrokerPublish with QoS 2
	- 



# 

---
- Status: #done 

- Tags: #mqtt

- References:
	- [Source]()

- Related:
