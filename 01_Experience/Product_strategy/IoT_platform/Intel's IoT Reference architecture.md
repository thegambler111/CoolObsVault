- 8: [source](http://d885pvmm0z6oe.cloudfront.net/hubs/intel_80616/assets/downloads/general/Architecture_Specification_Of_An_IOT_Platform.pdf)
	- ![[Images/IoT_platform/IoT_platform_Intel_layers.png]]
		- White blocks are user layers
		- Dark blue blocks are major runtime layers!
		- Light blue blocks are layers for developers


- Description of Data flow
	- ![[Images/IoT_platform/IoT_platform_Intel_data_flow.png]]

| Component            | Software type                                | Functionality                                                                                                                                                | Interfaces                                                                                                                                                                                                         |
| -------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sensor               | Hardware and firmware for intelligent things | Gathers sensory information like temperature, pressure, vibration, energy, etc.                                                                              | Connects to the gateway or sensor hub via wired (e.g., I^2 C, GPIO, SPI) or wireless (e.g., BTLE, ZigBee*, USB)                                                                                                    |
| Actuator             | Same as above                                | Performs actuation (e.g., turn on LED)                                                                                                                       | Same as above                                                                                                                                                                                                      |
| Sensor Hub           | Hardware and firmware                        | Connects to sensors and actuators, and aggregates data.                                                                                                      | Same as above                                                                                                                                                                                                      |
| Sensor Handler       | Middleware                                   | Middleware Interfaces with sensors using device drivers or API libraries (e.g., Protocol Abstraction or Mapping Layer (PMA) APIs).                           | Communicates via API calls to sensor libraries (or PMA) or directly to device drivers (in the absence of APIs).                                                                                                    |
| Local Database       | Third-party or open-source software          | Locally stores sensor data, logging or configuring information from the cloud.                                                                               | Uses REST, ODBC, JDBC, etc. on SQL, JSON, streaming, time and spatial data.                                                                                                                                        |
| Data Agent           | Software                                     | Gathers and formats data (for the cloud) from the different sensors and controls actuators based on commands from the cloud.                                 | Communicates with the sensor handler via API calls to sensor libraries (or PMA) or directly to device drivers (in the absence of APIs). Communicates with the cloud via different protocols, like MQTT, REST, etc. |
| Edge Analytics Agent | Software                                     | Learns actionable data in local context and near real time.                                                                                                  | Communicates with major deviceto-device and device-to-cloud API for rules on data streams, their alerts, and local processing                                                                                      |
| Security Agent       | Software and middleware                      | Handles security primitives for gateways and sensors/actuators, including authentication keys and certificates.                                              | Communicates with the security management software component in the cloud.                                                                                                                                         |
| Management Agent     | Software and middleware                      | Software and middleware Handles manageability primitives for gateways and sensors/actuators, including provisioning, error handling, alerting, and eventing. | Communicates with the device management software component in the cloud.                                                                                                                                           |

- Description of Software Components
	- ![[Images/IoT_platform/IoT_platform_Intel_software_components.png]]

| Component                          | Description                                                                                                                                                     | Interfaces                                                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Cloud Data Ingestion Software      | Interacts with the edge data agent and ingests data coming from edge devices, making it available to other cloud software via the Enterprise Service Bus (ESB). | Communicates with the data agent via different protocols, like MQTT, REST, DDS, etc., and publishes to ESB. |
| Cloud Security Management Software | Interacts with the edge security agent in the edge, and configures and controls security primitives of onpremise equipment.                                     | Communicates with the edge security agent and configuration database.                                       |
| Cloud Device Management software   | Interacts with the edge management agent in the edge, and configures and controls manageability primitives of on-premise equipment.                             | Communicates with the edge device management agent and configuration database.                              |
| Enterprise Service Bus             | Assists in the design and implementation of communications between mutually interacting software applications.                                                  | Supports cloud analytics and service orchestration software, and can subscribe to data from the ESB.        |
| Operational Database               | Manages dynamic data end-to-end, allowing real-time data modifications (add, change or delete). Examples include MongoDB* and Hadoop*.                          | Supports cloud analytics and service orchestration software, and can access the operational database.       |
| Configuration Database             | Contains all relevant information about the edge components and the relationships between those components.                                                     | Includes security and management software that can access the configuration database.                       |
| Analytics Software                 | Runs big data analysis on the data gathered from edge components.                                                                                               | Can access the operational database and data from the ESB.                                                  |
| Service Orchestration Software     | Centrally ensures service level agreements (SLA) across resource managers workflow and provisioning applications and services                                   | Can access the operational database and data from the ESB.                                                  |
| Configuration Management           | Centrally ensures on-premises configuration management, including devices and security.                                                                         | Updates the configuration database.                                                                         | 




- Intel's IoT Reference architecture
	- Communication and connectivity layer: ![[Images/IoT_platform/IoT_platform_Intel_communication_layer.png]]
		- Enable multi-protocol data communication between:
			- Devices at the edge
			- Endpoint devices/gateways <-> the network <-> data center
		- 3 types of networks:
			- Proximity networks and local area networks (PAN/LAN):
				- Connect inside edge nodes: sensors, actuators, devices <-> control systems and assets
				- PANs are usually wireless
			- Wide area network (WAN):
				- Connect endpoint devices <-> remote data centers services
				- May use corporate networks, overlays of private networks over public internet, 4G/5G or satellite networks
				- Gateways perform protocol normalization, ingest data from things, and control things
				- Gateways are characterized by:
					- Low cost
					- Low power
					- Purpose-built
					- Limited
					- Disjoint features
	- Data layer with analytics: ![[Images/IoT_platform/IoT_platform_Intel_data_layer.png]]
		- Analytics are distributed across the cloud, gateways, and smart endpoint devices
		- Control is distributed across cloud and endpoint devices
		- Analytics at gateways allows faster responses and local focused resolutions
	- Management layer (both devices and data):![[Images/IoT_platform/IoT_platform_Intel_management_layer.png]]
		- Each managed device has a management agent that executes the  management and communicates with the cloud
		- Device cloud  connect to devices directly (connected devices) or through gateway (unconnected devices)
		- Device cloud functionality:
			- Discover, register, and provision new devices
			- Update applications and operating systems
			- **Manage data flows from devices**
			- Upload or stream data via an ActiveMQ client interface
			- Stop/reboot selected devices
			- Define and manage events, alarms, and notifications
			- Use cloud-side rules to initiates actions
			- Extend platform capabilities using scripts
			- Mange devices directly through its command shell
			- Manage organizations, users, and access rights
			- Upload and download files to/from a device
	- Control layer: (device management layer trigger the action and control layer execute it)
		- Can be on devices and on-premise
		- Or on cloud
	- Security layer
		- This layer provides end-to-end protections from endpoint devices to the network, and the cloud
			- Endpoint device level:
				- Protect device and user identities
				- Ensure device integrity
				- Protect operational and personal data (privacy)
			- Network level:
				- Ensure secure application, traffic; data security through any types of connections
			- Cloud level:
				- Deliver the necessary trust for data centers and multitenant public cloud environments

