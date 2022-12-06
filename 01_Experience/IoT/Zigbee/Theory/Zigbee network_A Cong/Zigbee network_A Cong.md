# Layers
![[01_Experience/IoT/Zigbee/Theory/Zigbee network_A Cong/dwg_zigbee_stack_layers_549x350.png]]
![[01_Experience/IoT/Zigbee/Theory/Zigbee network_A Cong/Zigbee layers from Zigbee Specification.png]]
- PHY:
	- Define type of signal transportation:
	- For Zigbee: 2.4 GHz include channel 11-26
	- Transmit power: dbm
- MAC (ieee): 64 bits
	- Unique for each device
	- Each device can have multiple MACs
	- Control devices
- PHY and MAC Zigbee ~ WIFI
- NWK: 24 bits
	- Coordinator create a NWK addr each time a device join
	- Coordinator is always 0x0000
	- Broadcast to all devices is 0xFFFF
	- Broadcast to all coordinators and routers (no end devices) is 0xFFFD
	- PanID
	- Network key: To decode message between Zigbee nodes
	- An endpoint = an entity
	- Cluster (16 bits) is group of functions
	- Cluster defines input and output of a profile
		- Input is for other devices to call
		- Output is to call other devices
	- Each cluster has some attributes
	- Cluster definition and usage is defined by Zigbee alliance
- Zigbee herdsman converter: Provide additional information that is not in common definition

# Docs
- Zigbee alliance
	- Base device behavior
	- ZigBee Cluster Library Specification revision 7 or 8
	- Smart home use case ?
- Texas Instruments

# Firmware
- Firmware configuration is default configuration and can be changed
- Transmit power is limited by hardware power amplification

#
---
- Status: #done
- Tags: #zigbee
- References:
	- [Image source](https://www.digi.com/resources/documentation/Digidocs/90002002/Content/Reference/r_zb_stack.htm?TocPath=zigbee%20networks%7C_____3)
- Related:
