# 1. Setup project

## Flash firmware for Zigbee 3.0 USB Dongle Plus
- [[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/How to flash firmware for Zigbee 3.0 USB]]

## Setup new Z2M gateway
- [[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M setup Orange Pi Zero/Z2M setup Orange Pi Zero]]
- [Original Z2M Configuration](https://www.zigbee2mqtt.io/guide/configuration/)

## Additional tools

### MQTT Explorer

### Wireshark

### Sniffer
- [Flash firmware for sniffer USB](https://www.zigbee2mqtt.io/advanced/zigbee/04_sniff_zigbee_traffic.html)
- Setup software
- Tuya datapoint plugin

# 2. Support new device profile
- [[01_Experience/IoT/Zigbee2MQTT/Documentations/Z2M ultimate guide to configure a device in converters/Z2M ultimate guide to configure a device in converters|Z2M ultimate guide to configure a device in converters]]

# 3. Viettel Z2M changes

## Zigbee2mqtt
- Track MQTT command execution times in 2 files:
	- `lib/controller.ts`
		- Remove execution time from device state in `publishEntityState()`
	- `lib/extension/publish.ts`
		- Track and calculate execution time in `onMQTTMessage()`

## Zigbee-herdsman
- Add `MatchDescriptor` procedure
	- Add `MatchDescriptor` function in `adapter/[adapter_type]/adapter/[adapter_type].ts` for all 4 adapters
		- deconz
		- ezsp
		- z-stack (mainly used)
		- zigate
	- Add `MatchDescriptor` procedure in `controller/model/device.ts` in `interviewInternal()`
- Add auto set `_defaultSendRequestWhen` for all devices when interviewing in `controller/model/device.ts/interviewInternal()`
	- `_defaultSendRequestWhen` is 'active' for sleepy device (store all commands and only send when device is awake)
	- `_defaultSendRequestWhen` is 'immediate' for non-sleepy device
- Return `rxOnWhenIdle`, `fullFunctionDevice`, `acPower` in `nodeDescriptorInternal()` of all 4 adapters
- Add many attributes and functions in ZCL in `zcl/definition/cluster.ts`

## Zigbee-herdsman-converters
- Add 5 new files:
	- `converters/vtFromZigbee.js`
	- `converters/vtToZigbee.js`
	- `devices/viettel.js`
	- `lib/viettel.js`
	- `lib/vt_reporting.js`
- Most of the work are in those 5 files
- All other file changes are in device files in folder `devices`
	- The only type of changes in these files is replacing original device profile with our device profiles
- The changes in 5 new files are:

### devices/viettel.js
- This file contains all new device profiles
- It includes new device profiles and replaced profiles
	- Replaced profiles are profiles modified from original Z2M profiles
- For a device profile structure, please refer to [[#2. Support new device profile]]

### converters/vtFromZigbee.js
- This file contains new functions to process Zigbee messages received from devices
	- This file is the same as `converters/fromZigbee.js` but for new functions created by Viettel engineers
- These functions will update new attribute values of the device

### converters/vtToZigbee.js
- This file contains new functions to send Zigbee commands to devices
	- This file is the same as `converters/toZigbee.js` but for new functions created by Viettel engineers
- When receiving MQTT command messages, Z2M translates them to Zigbee messages through functions stored in `toZigbee` files
- Z2M use functions in `toZigbee` to translate MQTT commands to Zigbee messages

### lib/viettel.js
- This file contains utility functions created by Viettel engineers
	- These functions mostly used in `vtFromZigbee` and `vtToZigbee`
- This file also contained new Tuya datapoints for newly supported devices

### lib/vt_reporting.js
- This file contains the new `configureReporting` for new device profiles
	- `configureReporting` is a Zigbee command which tell device to periodically report of some attributes

# 4. Additional documentations
- [[01_Experience/IoT/Zigbee2MQTT/Documentations/Tuya documentation/Tuya documentation|Tuya]]
- [[01_Experience/IoT/Zigbee2MQTT/Documentations/Aqara hub M1S connnect to Mi home Android/Aqara hub M1S connnect to Mi home Android|Aqara]]

## 1. [**zigbee2mqtt/FRIENDLY_NAME**](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html#zigbee2mqtt-friendly-name)
- This is a reported topic, published when a device changes its state
	- We use this topic when
		- initialize z2m
		- rename the device 
		- send a control message,...
	- `FRIENDLY_NAME` is the IEEE-address or user-defined `friendly_name` of a device
	- Published messages are **always** in a JSON format
 - Message A:
	 - Type
		 - AREQ
	 - Subsystem = ZDO
	 - command = leaveInd

#
---
- Status: #done
- Tags: #z2m
- References:
- Related:
	- [[01_Experience/IoT/Zigbee2MQTT/Documentations/Final legacy/Theory legacy/Theory legacy]]
