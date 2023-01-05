# What is IoT platform

## IoT parts
- ![[Images/IoT_platform/IoT_platform_4_parts_of_IoT.png]][image source](https://smartfactoryvn.com/technology/internet-of-things/iot-platform-la-gi-co-nhung-loai-iot-platform-nao/)


## IoT platform

- IoT platform enable:
	- Device management
	- Connection management
	- Data collection and management
	- Data analysis and visualization
	- IT and cloud integration


## IoT platform structure
 ![[Images/IoT_platform/IoT_platform_structure_4.png]][image source](https://smartfactoryvn.com/technology/internet-of-things/iot-platform-la-gi-co-nhung-loai-iot-platform-nao/)


- Edge interface, message broker and message bus:
	- Communicate with devices and sensors
	- Should be able to handle all communication technologies such as WiFi, Bluetooth, LoRaWAN, GPRS, etc.
	- Consolidate the data in a unified manner and push it to the common message bus.
- Message router and communication management:
	- Enrich existing data messages
	- Publish additional contextual information and more messages after the main message arrives
	- Eliminate or discard multiple duplicate messages or redundant data packets from the devices
	- Convert format
	- Tag the messages as appropriate
	- Re-broadcast them to the message bus
- Time-series storage and data management
	- Store and parse all data from message bus in sequential (i.e. time-series styles)
	- Usually be the temporary storage before data is pushed to application data warehouse for further processing
- Rule engine:
	- monitor the message bus and events across the platform and take an action based on set rules with fast execution speed
	- Trigger when communication block puts decoded data packet on to message bus
	- Can broadcast another message (Alert) on to the message bus
	- ❓ Rule engine also helps in building modular rules for decoding and enriching existing or received data from the devices and would, therefore, augment communication module’s functionality. In addition to that, it is easy to implement callbacks to other modules, applications, programs, and systems.
- ReST API interface
	- Useful for support functions and utilities which do not need constant or real-time connectivity and access
- Microservices
	- Are support functions exposed to the blocks within and outside of the platform
	- Frequently used functionality within the platform can also be bundle and packaged under this block
- Device manager
	- Provide the generic functionality of managing devices such as:
		- Listing of all the devices
		- Active-inactive status
		- Battery levels
		- Network conditions
		- Access keys
		- Readings, stored data access
		- Device details
		- Session information
		- ... 
	- Manage air updates of devices
- Application and user management
	-  Provide user management functionality such as:
		- Password and credentials
		- Access keys
		- Logins
		- Permissions
	-  Provide user management functionality such as:
		- Password and credentials
		- Access keys
		- Logins
		- Permissions
		- ...
	- For upstream applications and various other integrated systems:
		- API keys
		- Credentials
		- Access
		- ...


