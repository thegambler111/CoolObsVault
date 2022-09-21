# 
- An excellent middleware between Zigbee end devices and IoT platform with
	- Low latency
		- [x] Average pairing time ~ 5s. Max pairing time < 60s [Tuya](https://developer.tuya.com/en/docs/iot/Zigbee_Wi-Fi_gateway?id=Kbg4vdcz4bbpr)
		- [x] Average command + response cycle through internet is 120ms
		- The theoretical transmission rate is 250 kbit/s.
		- [x] Check all modules, replace unnecessary modules
	- Seamless connection (Low down time)
		- [x] Working without internet
		- [x] Connection monitoring
			- Check Tuya dynamic heartbeat management
		- [x] Good number of concurrent connected devices
		- [x] High number of concurrent messages
		- [x] Zigbee network auto repair
			-  Change channel when the current channel becomes noisy
			- Change PAN ID if detecting another network with the same PAN ID
			    - Using extended PAN ID to tell all devices in the network to move
			- Frame counter wrap can cause errors -> change network key to reset frame counter
	- High compatibility (Connect and control devices from all vendors)
		- [x] Auto configurating device definition
		- [x] Local linkage?
		- [x] Joining with Install-Code Derived Link Key
	- Best hardware
		- [x] Cheap (Minimum hardware required)
		- [x] Small
		- [x] Good cover area
			- Tuya communication distance: indoor 35m, outdoor 200m+
	- Easy to monitoring the whole system
		- [x] Build a quality monitoring system
			- Test environment: Detailed
				- Execution time of each function in a request
			- Real-life: 
				- Execution time of each request
		- [x] Zstack USB monitoring
			- Logging and debug
			- Monitoring
			- Auto repair
		- [x] MQTT broker monitoring
			- Logging and debug
			- Monitoring
			- Auto repair
		- [x] Z2M logs
			- Increase local storage
			- Synchronize with cloud logs storage
	- Good security:
		- [x] Ensure Zigbee standard
		- [x] Connection GW <-> MQTT broker
		- [x] Connection MQTT broker <-> Platform
	- User friendly
		- [x] OTA upgrade for devices and for system (GW + MQTT + Zstack USB)
		- [x] Device group control
		- [x] Hot swap GW: Migrate hardware without losing connections (PanID)
			- GW synchronization?
		- [x] Easy to install
			- Connection LAN and WIFI
			- Multiple permit join timer
		- [x] Status LED
			- WIFI LED, Zigbee LED
			- Permit join LED
		- [x] Optimize Zigbee network starting behavior
			- Auto configuring Zigbee network
		- [x] Accidental deletion prevention
		- [x] Pairing multiple devices at the same time
		- [x] Device linking between different gateway (through LAN or internet)
		- [x] Reset button
		- [x] Device schedule
			- Smart wakeup (check tuya)
	- [x] Extend: Combine with multiple protocols
		- WIFI
		- Bluetooth

- Move to GW:
	- MQTT broker
	- Device health monitoring
	- Automation

- Additional tasks:
	- New OS
	- Using low level language like C




































# 

---
- Status: #done

- Tags: #

- References:
	- 

- Related:
	- 