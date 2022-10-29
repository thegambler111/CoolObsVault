# Retained message
- If `retainMessage=true`, Broker will store message and QoS of the topic
- Broker will retain only 1 message of a topic at 1 time
- A retained message is the last message of that topic with `retainFlag=1`
- Retain messages help newly subscriber clients to get a status update immediately

## Disable retain message
- To disable retain message feature for a topic , send an empty message with `retainFlag=1` to that topic
	- The broker will delete the retained message of that topic

![[01_Experience/IoT/MQTT/MQTT Master class/Section 6_Persistence/Section 6_Persistence#Retained message]]

#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
