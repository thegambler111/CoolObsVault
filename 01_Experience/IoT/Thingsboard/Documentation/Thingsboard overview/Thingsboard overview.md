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




#
---
- Status: #done
- Tags:
- References:
	- [Source](https://thingsboard.io/docs/)
- Related:
