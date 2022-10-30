# Device management
- Device management (DM):
	- Provisioning
	- Configurations
	- Update on firmware
	- Status
	- Diagnostic information
- IoT DM characteristics
	- Resource constraint devices
	- Machine-to-machine communication
	- Efficient, autonomous, and secure management operations
	- Support deployment at scale
	- Address the entire life cycle of a device
- Advantages:
	- Support deployment at scale
	- Reduce operational and maintenance costs
	- Mitigate security risks
	- Reduce business risks

# Device classification
 - Hardware capability attributes
	- Compute power
	- Storage
	- Network connectivity options
	- Sensing capability
	- Power
- Communication:
	- Unidirectional: Send or receive data
	- Bidirectional: Send and receive data
- Functions
	- M2M gateway
	- M2M devices
	- Proxy/relay devices

# DM architecture

# DM functionalities
- Pre-deployment
	- Security credentials and policies
	- Initializing device metadata
- Post-deployment
	- Device provisioning or re-provisioning
	- Device onboarding
- Operation/Maintenance
	- Device configuration
	- Change device metadata
	- Securely changing or updating device software/firmware
	- Creating event alerts, diagnostic information, or event logs
- Decommission
	- Decommissioning or removing a device from the DM registry on DM servers

# DM standards for IoT/M2M
- TR-069
	- Version 1.4 - 2014
	- Functions: 
		- Auto-configuration and dynamic service provisioning
		- Firmware image management
		- Software module management
		- Status and performance monitoring and diagnostics
- OMA DM
	- Version 2.0 - 2016
	- Functions:
		- Setting initial configuration information:
			- Provision, installation and updates of persistent information
		- Retrieval of management information
		- Processing, events and alarms 
- OMA LightweightM2M (LwM2M)
- oneM2M

# Message transfer protocols
- HTTP: "heavy-weight"
- MQTT and CoAP: 'light-weight'
- MQTTSN is used when TCP connection is not available

## CoAP
- Constrained Application Protocol
- CoAP endpoints can directly interoperate with each other, or with HTTP and RESTful web services through CoAP proxies
- CoAP runs over connectionless UDP datagrams, and is possible to run over SMS or TCP bears

# LwM2M













#
---
- Status: #done
- Tags: #IoT
- References:
	- [Source](https://www.linkedin.com/learning/iot-foundations-device-management)
- Related:
