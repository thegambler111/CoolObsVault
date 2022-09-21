# 
- When a device is added to the network with a Zigbee-Herdsman controller, the controller uses the low-level configuration clusters to interview the device and find out what the device is, what endpoints it has, and what clusters each of those endpoints implements. 
- The Zigbee-Herdsman-Converters then record, for each model of device, which clusters the controller should bind to, and how the conversion to MQTT should be handled.
- Most devices in Zigbee-Herdsman-Converters use generic converters that bind to each Zigbee cluster and provide a standard MQTT interface for that cluster.





# 

---
- Status: #writing

- Tags: #zigbee

- References:
	- 

- Related:
	- 
