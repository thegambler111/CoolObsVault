# Gateway vision
## Goals
- An excellent middleware between Zigbee end devices and IoT platform with
	- Low latency
		- Average pairing time ~ 5s. Max pairing time < 60s [Tuya](https://developer.tuya.com/en/docs/iot/Zigbee_Wi-Fi_gateway?id=Kbg4vdcz4bbpr)
		- Average command + response cycle through internet is 120ms
	- Seamless connection (Low down time)
		- Working without internet
		- Connection monitoring
			- Check Tuya dynamic heartbeat management
		- Smart wakeup (check tuya ?)
		- Good number of concurrent connected devices
		- High number of concurrent messages
		- Zigbee network auto repair
			-  Change channel when the current channel becomes noisy
			- Change PAN ID if detecting another network with the same PAN ID
			    - Using extended PAN ID to tell all devices in the network to move
			- Frame counter wrap can cause errors -> change network key to reset frame counter
	- High compatibility (Connect and control devices from all vendors)
		- Auto configurating device definition
		- Local linkage?
		- Joining with Install-Code Derived Link Key
	- Best hardware
		- Cheap (Minimum hardware required)
		- Small
		- Good cover area
	- Easy to monitoring the whole system
		- Build a quality monitoring system
			- Test environment: Detailed
				- Execution time of each function in a request
			- Real-life: 
				- Execution time of each request
		- Zstack USB monitoring
			- Logging and debug
			- Monitoring
			- Auto repair
		- MQTT broker monitoring
			- Logging and debug
			- Monitoring
			- Auto repair
		- Z2M logs
			- Increase local storage
			- Synchronize with cloud logs storage
	- Good security:
		- Ensure Zigbee standard
		- Connection GW <-> MQTT broker
		- Connection MQTT broker <-> Platform
	- User friendly
		- OTA upgrade for devices and for system (GW + MQTT + Zstack USB)
		- Device group control
		- Hot swap GW: Migrate hardware without losing connections (PanID)
			- GW synchronization?
		- Easy to install
			- Connection LAN and WIFI
			- Multiple permit join timer
		- Status LED
			- WIFI LED, Zigbee LED
			- Permit join LED
		- Auto configuring Zigbee network
		- Accidental deletion prevention
		- Pairing multiple devices at the same time
		- Device linking between different gateway (through LAN or internet)
		- Reset button
	- Extend: Combine with multiple protocols
		- WIFI
		- Bluetooth

- Move to GW:
	- MQTT broker
	- Device health monitoring
	- Automation

- Additional tasks:
	- New OS
	- Using low level language like C


# Tuya Gateway capabilities
## Tuya Zigbee Gateway
- [Zigbee Gateway support](https://support.tuya.com/en/help/_list?category=Cb4xqgragqn84)
	- The gateway that supports LAN linkage, can realize the linkage of sub-devices of different gateways under the same LAN.
	- Can I connect a Tuya Zigbee module to a Zigbee gateway that I have developed to develop a product?
		- No. You must use a Tuya gateway or a Tuya OEM gateway. If you require an OEM gateway, contact Tuya business personnel.
	- Tuya SDK using C:
		- SDK is not a stand-alone program, it is provided to a third party system in the form of C static library (a file), and the third party system is responsible for the initialization and termination of the SDK as the host program. So to get SDK, user needs to provide corresponding compilation toolchain to generate, and the generated host program needs to run in the Linux environment, the communication between SDK and the third-party system can be achieved through function calls.
	- Tuya wired Zigbee gateways support the star, tree, and mesh topologies.
	- The working temperature of wired Zigbee gateway is -10℃ to 55℃.
	- Is there a limit to the number of low-power firmware devices that can access the wired Zigbee gateway?
		- Yes, only 32 low-power firmware devices can be accessed. If want to add more than 32 devices, you need to add high-power device as relay routes before you can add low-power devices. Each additional high-power device can add about 20 low-power devices, and so on, until the maximum number of gateways is added.
	- It is possible to link devices under different Zigbee gateways by using the same App account through cloud linkage
	- Datapoint:
		- Function datapoint: 0-200
		- System Datapoint: 201-255
	- The theoretical transmission rate is 250 kbit/s.

- [Wireless Zigbee Gateway](https://developer.tuya.com/en/docs/iot/Zigbee_Wi-Fi_gateway?id=Kbg4vdcz4bbpr)
	- Security features
		- The Transport Layer Security (TLS) protocol supports mutual device authentication and secures data transmission.
		- Business data is encrypted with random secret keys.
		- Data stored locally is protected by a one-key-per-device authentication mechanism.
	- *Support stable networking and broadcast in bulk.*
	- It only takes five seconds on average to connect a device and show it on the app.
	- It takes about 120 milliseconds for a command to be sent and responded over the internet without signal interference. This delivers a wonderful user experience.
	- Device control and smart scene execution over a local area network (LAN).
	- Reliable local linkage services across gateways.
	- Up to 50 sub-devices can be added to this gateway.



## [Wireless Zigbee Gateway](https://solution.tuya.com/projects/CMa4s3xhnq7vab)
- Communication Capability: Wi-Fi + Zigbee
- Applicable module: WRG1 + TYZS3_NS
- Development Mode: Zero-coding development
- Recommendation panel: Small fresh style
- Power consumption type: General power consumption
- Product adaptation: Zigbee sub-equipment such as electrician, lighting and sensing
- Number of nodes/Pcs: 35
- Communication distance (range of visibility)/m: indoor 35m, outdoor 200m+

- Smart Hotel
	- A user can carry out intelligent scene linkage of equipment by opening and closing doors, such as electronic curtains, lights, fresh air system, and the underfloor heating system, by opening or closing the door without additional manual operation. This is implemented through the linkage of devices connected to a gateway, which serves as an "interpreter" for devices designed with different protocols.
- Smart Security
	- A robust security system is essential to protect our personal and property safety. But the conventional security systems are costly and difficult to install. With a Tuya gateway, users only need to purchase devices supported by the Tuya ecosystem such as smart locks, peepholes, and PIR sensors to build an anti-theft system. If a user turns on the system before leaving home, the system will start working and immediately send an alert to the user when detecting any anomaly.

- Convenient networking
	- Users can connect multiple sub-devices simultaneously instead of doing it one by one. They can also connect sub-devices when there is no network connection.
- Accidental deletion prevention
	- Under normal conditions, a sub-device will be reset if it is disconnected by mistake. If the user does not pair the network for this sub-device, **it will be automatically connected to the previous gateway in three minutes**.
- Quick control in multicast/scenarios
	- The gateway supports large-scale multicast under normal conditions, and allows simultaneous and stable online operation of over 100 high-power devices. It supports both local scenario linkage and networked inter-gateway linkage.
- Dynamic heartbeat management
	- The online and offline status of the connected sub-devices can be dynamically detected based on a dynamic heartbeat algorithm. The whole process takes 10 seconds or longer, depending on the number of the connected sub-devices.
- Standard Zigbee 3.0 protocol
	- The gateway is developed based on the standard Zigbee 3.0 protocol. You can connect and manage your devices that are designed based on the standard Zigbee 3.0 protocol. Some non-standard functions can be implemented through custom development.
- Add and control sub-devices
	- Sub-devices can be added both online or offline for device scenario linkage, local linkage, and group control.
- Smart security
	- The gateway can be connected to the Smart security SaaS. You can configure the security attributes of the gateway to connect it to Smart security PaaS and acquire the permissions for arming and disarming in the cloud.
- OTA services
	- Tuya provides over-the-air (OTA) update services for the entire gateway system, including the gateway device, Zigbee master control board, Zigbee modules, and the MCUs connected to the Zigbee module. You can update their software through OTA without dismantling them.

## [Smart multi-functional Zigbee gateway](https://solution.tuya.com/projects/CMa8js486c2yqa)

- Development mode: TYZS4
- Number of nodes/Pcs: 128
- Communication distance (range of visibility)/m: indoor 35m, outdoor 200m+

- Smart wakeup
	- You can enable the wakeup mode and configure the alarm, water heater, air conditioner, speaker, and food processor. With a scheduled task, the water heater and air conditioner will be turned on before the alarm goes off. When the alarm goes off, the curtains automatically open, the speaker plays a selected playlist, and the food processor starts to work. A perfected indoor temperature and healthy breakfast energize your body to embrace a new day.
- Safety in the kitchen and bathroom
	- Detect the CO concentration, smoke density, and natural gas in real-time and send an alert of anomalies. It can be connected to the water level sensors near the sink and bathtub to prevent water from overflowing. When accidents occur, you can press the SOS button to ask for help. You can also remotely control the rice cooker and food processor to keep food in your control. Keep your kitchen and bathroom safe.

- Cost-effective
	- Integrate audible and visible alarms, nightlights, and Zigbee gateways, and provide reliable and fast responses with a maximum of 128 connected Zigbee devices.
- Excellent experience
	- Feature multilingual audio prompts, multi-color light control, timed multi-color lights, smart alarms, and PIR nightlights, delivering unlimited possibilities of convenience and pleasure.
- Reliable control
	- Enable remote control of Zigbee devices connected to the gateway with a mobile phone. Distance won't be a problem for device control. Support reliable local linkage and scene automation, as well as group control.
- Smart security
	- Integrate devices into smart security SaaS to enable arming and disarming on the app panel.
- Standard protocol
	- The gateway is developed based on the standard Zigbee 3.0 protocol. You can connect and manage your devices that are designed based on the standard Zigbee 3.0 protocol. Some non-standard functions can be implemented through custom development.
- Real-time logs reporting
	- Report real-time sub-device error code and gateway log sequence, enhancing subsequent maintenance.
- Multilingual audio
	- Synchronously update the device audio as per the language used in your mobile phone system language. It also provides you with dedicated and intimate audio prompt services.

## [Wired ZigBee gateway](https://solution.tuya.com/projects/CMa57ab4u2x1ji)

- Applicable module: RTL8196E+TYZS4-IPEX
- Number of nodes/Pcs: 128
- Communication distance（range of visibility）/m: indoor 35m, outdoor 200m+


- Linkage cross protocols and gateways
	- Provide local linkage capabilities across multiple gateways and protocols over a local area network (LAN), which are exclusive in the industry. Local linkage between various devices can be achieved over a LAN by presetting corresponding scenarios when devices are connected to the network.
- Pegasus
	- With the gateway activated, you can press the button on the gateway to enter the pairing mode that lasts for one hour. During this period, the sub-devices that are ready to be paired will be added automatically. To exit the pairing mode, you only need to press the button again.
- Project deployment
	- Project installation and deployment is supported. You can complete the local deployment of sub-devices without external network. In addition, scenario-specific configurations are supported. You can exit a specific scenario after the device deployment and scenario debugging. Users only need to configure the gateway to use locally deployed products with corresponding scenario configuration.
- Switchover for failures
	- If you need to replace the gateway in case of hardware failure, you can use this function to switch to the standby gateway. Configurations of sub-devices and corresponding linkage scenarios configured in the original gateway can be synchronized to the standby gateway.
























# 

---
- Status: #done

- Tags: #z2m 

- References:
	- [Tuya GW](https://solution.tuya.com/projects/CMa8js486c2yqa)

- Related:
	- 
