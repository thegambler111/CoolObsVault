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


# Plan
- 4/2022: 2 weeks devices <-> 2 weeks new features
	- Master code flow
		- Event handling
		- Znp
		- MQTT
	- Setup a process to update code from KKoen without conflicts
	- Redesign DB
	- Change z2m log settings: better storage management
	- Build a process to evaluate device response time
	- Build a monitoring system for GW -> send to Platform
	- 100 devices
	- Backup:
		- Accidental deletion prevention
		- Test GW capability
			- Max concurrent connected devices
			- Max concurrent command
		- Build a monitoring system for GW + platform connection

- 1/2022
	- Create universal way to check device connection status
	- Accidental deletion prevention
	- Optimize execution time
		- Improve command - response cycle
		- Improve pairing time: Can multiple devices be paired at the same time
		- Improve boot time, restart time
	- Create log for MQTT connection
	- Test GW capability
		- Max concurrent connected devices
		- Max concurrent command
	- Build a monitoring system for GW + platform connection

- 2/2022
	- Device automation
	- Check local linkage feature
	- Optimize Zigbee network optimization behavior
	- Implement GW hot swap (replace GW without down time)
	- Check group management
		- And group control
	- Read about USB
		- How it work
		- Log
		- What to improve
		- Auto repair

- 3+4/2022
	- OTA update for devices
	- OTA update for GW + USB
	- Auto create device definition
	- Joining with Install-Code Derived Link Key
	- Design GW physical requirement
		- Hardware requirement <-> performance: Should be in 2-3 levels
		- Physical appearance: buttons, lights, ports

- Future consideration
	- Improve security
	- Change language, OS
	- Zigbee network auto repair


# Old vision
- Features:
	- [ ] Gateway functionality
		- [ ] Create CTKT
	- [ ] Create new GW flash image
	- [ ] Cannot connect to MQTT server
	- [ ] SRSP - AF - dataRequest after 6000ms -> Failed to open system journal: No space left on device
	- [x] Fix PIR bugs? -> Broadcast binding
	- [x] Auto check device online status
	- [x] Converter for new devices
		- [x] Making changes in new files only
	- [ ] Bigger and controllable log storage: Currently store ~ logs of 3 days
	- [ ] Zigbee2mqtt front end: file npm run build != file npm install
	- [ ] Logging and reset USB from GW
	- [x] Fix error: changing configuration -> have to delete coordinator_backup ??
	- [ ] Get OTA link for devices
	- [ ] Update GW, USB, devices firmware on the fly
	- [ ] Control GW from platform: Create APIs
	- [ ] Migrate GW to GW using PanID: To replace GW
	- [ ] White list for permit joins: Auto permit join when receive request from devices in this list -> Seem impossible
	- [ ] Disable router ability of some device types
	- [ ] Low LQI warning
		- [ ] Individual device routing
	- [ ] Control all devices of the same type (or have the same function like onOff) (Can we use group?)
- [ ] Dev environments
	- [x] Windows alias
	- [x] Windows auto sync files
	- [x] npm debug -> Save to file
- [ ] Request
	- [ ] Not connect to MQTT server
	- [ ] Accidental deletion prevention
	- [ ] PIR frozen



















# 

---
- Status: #done

- Tags: #

- References:
	- 

- Related:
	- 
