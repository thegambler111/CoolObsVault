# How coordinator selects channel
![[01_Experience/IoT/Zigbee/Theory/Coordinator startup/Coordinator channel selection.png]]
- To select a correct channel and PAN ID, the coordinator performs an energy scan and PAN scan.
	- 'Scan Channels' and 'Scan Duration' are used to determine the duration and the list of channels to scan.
	- 'Extended PAN ID' is used to select an ID different from zero.
	- After completing the scans, the coordinator uses the results to select the channel with less energy and a PAN ID unused in other PAN.
	- If security should be set at startup, please see chapter 13 "Synchronizing the Network".

# Security
- Only the coordinator can serve as a Trust Center.
- Managing Security Keys
	- Modules define a network key and a link key (trust center link key).
	- Both keys are 128-bits and are used to apply AES encryption to RF packets.
- When a device joins a secure network, it must obtain the network key from the coordinator.
	- The coordinator will either transmit the network key using a pre-installed link key.
	- The coordinator will transmit the network key unencrypted:
		- If the 'Encryption Options' bit is set to transmit the network key unencrypted
		- Or if the 'Link Key' parameter is set to 0 on the coordinator (select a random link key)
	- Otherwise, the coordinator will encrypt the network key with the link key
		- If the 'Encryption Options' bit is not set and 'Link Key' is > 0,
- If a joining device does not have the right preconfigured link key, and the network key is being sent encrypted, the joining device will not be able to join the network.
- Network security requires a 32bits frame counter maintained by each device.
	- This frame counter is incremented after each transmission and cannot wrap to 0.
	- If a neighbor receives a transmission with a frame counter that is less than or equal to the last received frame counter, the packet will be discarded.
- To prevent an eventual lockup where the frame counter on a device reaches 0xFFFFFFFF, the network key should be periodically updated (changed) on all devices in the network.
- To update the network key in the network, the coordinator should issue the 'Encryption Key' parameter with a new security key.
	- This will send a broadcast transmission throughout the network causing the frame counters on all devices to reset to 0, and causing devices to begin using the new network key.
	- All devices will also retain the previous key for a short time until everyone has switched to the new key.

#
---
- Status: #done
- Tags: #zigbee
- References:
	- [Source](https://development.libelium.com/zigbee-networking-guide/starting-a-network)
- Related:
