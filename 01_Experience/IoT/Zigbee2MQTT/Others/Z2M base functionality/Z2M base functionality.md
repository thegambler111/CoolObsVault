# From z2m guide

## Allow device to join
- Pairing new devices

## Integration
- Integration into some platforms

## Touchlink
- Connect to new Zigbee devices through a device in network then reset the new one for pairing

## Scenes
- Save states of devices or groups 

## Binding
- Device control other devices (or groups) directly without z2m (even when z2m is offline)

## Groups
- Control multiple devices using a single command
- Coordinator does not know which device belong to which group
	- When controlling a group, coordinator send command to all device. If device belong to the group, it will execute the command ([Source](https://www.zigbee2mqtt.io/guide/usage/groups.html#how-do-groups-work))

## OTA updates
- Update Zigbee device OTA

## MQTT topics and messages
- Control devices through MQTT message
- FRIENDLY_NAME = IEEE addr (MAC) or defined friendly name
- FRIENDLY_NAME/availability: device-availability
- FRIENDLY_NAME/set: Control devices
- FRIENDLY_NAME/get: Get devices status
- bridge/: Most of 
	- info: Information of the bridge
	- state: State of the bridge (online/offline)
	- logging: All logs are published in this topic
	- devices: List of devices connected to the bridge and their info
	- groups: List of groups and their members
	- event: Possible types are "device_joined", "device_interview", "device_leave", "device_announce"
	- extension: Add/remove user extensions
	- 

## Exposes
- Showing device capabilities in "exposes" tab

## Debug
- Debug z2m, herdsman




# 

---
- Status: #done

- Tags: #z2m 

- References:
	- [z2m guide]

- Related:
	- 
