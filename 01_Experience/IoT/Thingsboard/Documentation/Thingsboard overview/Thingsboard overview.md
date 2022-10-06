# Features
- With ThingsBoard, you are able to:
	- Provision **devices, assets and customers**, and define **relations** between them.
	- Collect and visualize **data** from devices and assets.
	- Analyze incoming **telemetry** and **trigger alarms** with complex event processing.
	- **Control** your devices using remote procedure calls (RPC).
	- Build **work-flows** based on a device life-cycle event, REST API event, RPC request, etc.
	- Design dynamic and responsive **dashboards** and present device or asset telemetry and insights to your customers.
	- Enable use-case specific features using **customizable rule chains**.
	- Push device data to **other systems**.
	- Much more…

# Built-in transport protocols
- Devices communicating over those protocols are able to connect directly to ThingsBoard:
	- [MQTT API reference](https://thingsboard.io/docs/reference/mqtt-api)
	- [CoAP API reference](https://thingsboard.io/docs/reference/coap-api)
	- [HTTP API reference](https://thingsboard.io/docs/reference/http-api)
	- [LwM2M API reference](https://thingsboard.io/docs/reference/lwm2m-api)
	- [SNMP API reference](https://thingsboard.io/docs/reference/snmp-api)
- Most of these protocols support JSON, Protobuf or own data format.

# IoT Gateway
- The gateway converts the data from devices to internal ThingsBoard format and upload it over MQTT to the platform.
- 80% of current (10/2022) devices go through IoT Gateway
- ThingsBoard IoT Gateway helps to connect devices that are located in the local network and do not have access to the internet or use specific non-IP protocols.
- IoT Gateway supports MQTT, OPC-UA, Modbus, BLE, HTTP, CAN, BACnet, ODBC, SNMP and other protocols.
- See [What is IoT Gateway?](https://thingsboard.io/docs/iot-gateway/what-is-iot-gateway/) for more info.

# LoRaWAN ChirpStack
- It is possible to integrate ChirpStack network server with ThingsBoard Community Edition using this [guide](https://www.chirpstack.io/application-server/integrations/thingsboard/).

# ThingsBoard Professional Edition
- ThingsBoard PE supports:
	- [LoRaWAN](https://thingsboard.io/docs/user-guide/integrations/)
	- [Sigfox](https://thingsboard.io/docs/user-guide/integrations/sigfox/)
	- [NB IoT and other protocols](https://thingsboard.io/docs/user-guide/integrations/)

---

# Entities and relations

## Entities
- List of supported entities:
	- [Tenants](https://thingsboard.io/docs/user-guide/ui/tenants/): This is an individual or an organization who owns or produce devices and assets
	- [Customers](https://thingsboard.io/docs/user-guide/ui/customers/): This is an individual or organization who purchase or uses tenant devices and/or assets
	- [Users](https://thingsboard.io/docs/user-guide/ui/users/): Users are able to browse dashboards and manage entities
	- [Devices](https://thingsboard.io/docs/user-guide/ui/devices/): These are basic IoT entities that may produce telemetry data and handle RPC commands.
	- [Assets](https://thingsboard.io/docs/user-guide/ui/assets/): These are abstract IoT entities that may be related to other devices and assets. For example factory, field, vehicle.
	- [Entity Views](https://thingsboard.io/docs/user-guide/entity-views/): You can use this to share only part of device or asset data to the customers;
	- [Alarms](https://thingsboard.io/docs/user-guide/alarms/): These events identify issues with your assets, devices, or other entities;
	- [Dashboards](https://thingsboard.io/docs/user-guide/dashboards/): They are used to visualize your IoT data and to control particular devices through the user interface
	- Rule Node: These are processing units for incoming messages, entity lifecycle events, etc.
	- Rule Chain: It defines the flow of the processing in the [Rule Engine](https://thingsboard.io/docs/user-guide/rule-engine-2-0/re-getting-started/). May contain many rule nodes and links to other rule chains
- Each entity supports:
	- [Attributes](https://thingsboard.io/docs/user-guide/attributes/) are static and semi-static key-value pairs associated with entities.
	- [Time-series data](https://thingsboard.io/docs/user-guide/telemetry/) are data points available for storage, querying and visualization. For example temperature, humidity, battery level.
	- [Relations](https://thingsboard.io/docs/user-guide/entities-and-relations/#relations) are directed connections to other entities. For example contains, manages, owns, produces.
- Some entities support profiles:
	- [Tenant Profiles](https://thingsboard.io/docs/user-guide/tenant-profiles/): Each tenant has only one profile which contains common settings: entity, API and rate limits, etc
	- [Device Profiles](https://thingsboard.io/docs/user-guide/device-profiles/): Each device has only one profile which contains common settings: processing and transport configuration, etc

## Relations
- Entity relation defines connection between two entities that belong to the same Tenant
- The relation has an arbitrary type: Contains, Manages, Supports, etc
- The relation is directional

#
---
- Status: #done
- Tags:
- References:
	- [Source](https://thingsboard.io/docs/)
- Related:
