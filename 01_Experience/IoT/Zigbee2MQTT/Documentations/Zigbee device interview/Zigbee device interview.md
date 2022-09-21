# Device interview
- Start: `herdsman/controller/controller.ts/onDeviceJoined`

- When a device is added to the network with a Zigbee-Herdsman controller, the controller uses the low-level configuration clusters to interview the device and find out what the device is, what endpoints it has, and what clusters each of those endpoints implements. 
- The Zigbee-Herdsman-Converters then record, for each model of device, which clusters the controller should bind to, and how the conversion to MQTT should be handled.
- Most devices in Zigbee-Herdsman-Converters use generic converters that bind to each Zigbee cluster and provide a standard MQTT interface for that cluster.




- Device definition is created after Interview
	- `herdsman/controller/controller.ts/onDeviceJoined()/this.selfAndDeviceEmit()` line 545

# Device interview Zigbee command flow

## Establish Communication:

| Command             | Direction                | Purpose                                                                                                     |
| ------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Permit join request | Coordinator -> Broadcast | ?                                                                                                           |
| Beacon request      | Device -> Broadcast      | Find Zigbee channel and coordinator to connect                                                              |
| Beacon              | Coordinator -> Device    | Initiate the communication between Coordinator and Device                                                   |
| Association request | Device -> Broadcast      | - Accept the communication with Coordinator<br>- Provide basic communication behavior of Device             |
| Request key         | Device -> Coordinator    | Ask Coordinator for Trust Center Link key (network key)                                                     |
| Transport key       | Coordinator -> Device    | Provide Device with a networkID and networkKey to secure the communication                                  |
| Verify key          | Device -> Coordinator    | Verify networkKey                                                                                           |
| Confirm key         | Coordinator -> Device    | Confirm networkKey                                                                                          |
| Route Request       | Coordinator -> Device    | Find the best route to communicate with Device                                                              |
| Route Record        | Device -> Coordinator    | Inform Coordinator of Device's communication route                                                          |
| Device Announcement | Device -> Broadcast      | - Inform all Nodes in Zigbee network about new device joining<br>- Along with some of device's capabilities | 


- Permit join request
	- Coordinator -> Broadcast
	- Payload:
		- Sequence number
		- Duration
		- Significance
	- Purpose: ?
- Beacon request
	- Device -> Broadcast
	- Purpose:
		- Find Zigbee channel and coordinator to connect
- Beacon:
	- Coordinator -> Device
	- Payload:
		- PanID
		- Extended PanID
		- ...
	- Purpose:
		- Initiate the communication between Coordinator and Device
- Association request
	- Device -> Coordinator
	- Purpose:
		- Accept the communication with Coordinator
		- Provide basic communication behavior of Device
- Request key:
	- Device -> Coordinator
	- Purpose:
		- Ask Coordinator for Trust Center Link key (network key)
- Transport key
	- Coordinator -> Device
	- Purpose:
		- Provide Device with a networkID and networkKey to secure the communication
- Verify key:
	- Device -> Coordinator
	- Purpose:
		- Verify networkKey
- Confirm key
	- Coordinator -> Device
	- Purpose:
		- Confirm networkKey
- Route Request:
	- Coordinator -> Device
	- Purpose:
		- Find the best route to communicate with Device
- Route Record:
	- Device -> Coordinator
	- Purpose:
		- Inform Coordinator of Device's communication route
- Device Announcement:
	- Device -> Broadcast
	- Purpose:
		- Inform all Nodes in Zigbee network about new device joining
		- Along with some of device's capabilities

## Device interview:

| Command                    | Direction             | Purpose                                                                                                |
| -------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------ |
| Node descriptor request    | Coordinator -> Device | Ask for device's capabilities                                                                          |
| Node descriptor response   | Device -> Coordinator | Response device capabilities: Connection capability, Security capabilities, Zigbee router capabilities |
| Match descriptor request   | Coordinator -> Device | Ask for endpoints with Security related Cluster (i.e. IASZone 0x0500)                                  |
| Match descriptor response  | Device -> Coordinator | Return list of endpoints with Security related Cluster                                                 |
| Active endpoint request    | Coordinator -> Device | Ask for list of device's endpoints                                                                     |
| Active endpoint response   | Device -> Coordinator | Return list of device's endpoints                                                                      |
| Simple descriptor request  | Coordinator -> Device | In each endpoint, ask for its list of clusters                                                         |
| Simple descriptor response | Device -> Coordinator | Return list of endpoint's cluster                                                                      |


- Node descriptor request:
	- Coordinator -> Device
	- Purpose:
		- Ask for device's capabilities
- Node descriptor response:
	- Device -> Coordinator
	- Purpose:
		- Response device capabilities:
			- Connection capability
			- Security capability
			- Zigbee router capability
- Match descriptor request:
	- Coordinator -> Device
	- Purpose:
		- Ask for endpoints with Security related Cluster (i.e. IASZone 0x0500)
- Match descriptor response:
	- Device -> Coordinator:
	- Purpose:
		- Return list of endpoints with Security related Cluster
- Active endpoint request:
	- Coordinator -> Device
	- Purpose:
		- Ask for list of device's endpoints
- Active endpoint response:
	- Device -> Coordinator
	- Purpose:
		- Return list of device's endpoints
- Simple descriptor request:
	- Coordinator -> Device
	- Purpose:
		- In each endpoint, ask for its list of clusters
- Simple descriptor response:
	- Device -> Coordinator:
	- Purpose:
		- Return list of endpoint's cluster


## Device configure:
| Command             | Direction             | Purpose                                                                                                  |
| ------------------- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| Read attributes     | Coordinator -> Device | Read some basic attributes of the device: Time, Hardware and firmware information, Model and manufacture |
| Bind                | Coordinator -> Device | Bind device's endpoint to coordinator's endpoint so that endpoint reports any changes to coordinator     |
| Configure reporting | Coordinator -> Device | Endpoint report its attributes to coordinator periodically or when there are any changes                 |


- Read attributes:
	- Coordinator -> Device
	- Purpose:
		- Read some basic attributes of the device:
			- Time
			- Hardware and firmware information
			- Model and manufacture
			- ...
- Bind:
	- Coordinator -> Device
	- Purpose:
		- Bind device's endpoint to coordinator's endpoint so that endpoint reports any changes to coordinator
- Configure reporting
	- Coordinator -> Device
	- Purpose:
		- Endpoint report its attributes to coordinator periodically or when there are any changes


## Device control:
| Command                   | Direction             | Purpose                                                                                 |
| ------------------------- | --------------------- | --------------------------------------------------------------------------------------- |
| Read attributes           | Coordinator -> Device | Read attributes of devices                                                              |
| Read attributes Response  | Device -> Coordinator |                                                                                         |
| Write attributes          | Coordinator -> Device | Change attributes of devices                                                            |
| Write attributes Response | Device -> Coordinator |                                                                                         |
| Report attributes         | Device -> Coordinator | Report attributes of devices<br>- Trigger periodically or when attribute change happens |


- Read attributes:
	- Coordinator -> Device
	- Purpose:
		- Read attributes of devices
- Read attributes Response:
	- Device -> Coordinator
- Write attributes:
	- Coordinator -> Device
	- Purpose:
		- Change attributes of devices
- Write attributes Response:
	- Device -> Coordinator
- Report attributes:
	- Device -> Coordinator
	- Purpose:
		- Report attributes of devices
		- Trigger periodically or when attribute change happens

## Device leave
| Command      | Direction           | Purpose                                                                                                       |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------- |
| Device leave | Device -> Broadcast | Inform all nodes in Zigbee network that it is leaving. Included information: Rejoin, request, remove children | 

- Device leave:
	- Device -> Broadcast
	- Payload:
		- Rejoin: False
		- Request: False
		- Remove Children: False
	- Purpose:
		- Inform all nodes in Zigbee network that it is leaving



# Device interview Z2M

## Establish Communication:
- ?


## Device interview:
- The current SONOFF USB messages are handled in file:
	- File: `herdsman/src/adapter/z-stack/adapter/zStackAdapter.ts`
- Trigger:  `herdsman/src/adapter/z-stack/adapter/zStackAdapter.ts/onZnpRecieved()/this.emit(Events.Events.deviceJoined, payload);`
- Handle `onDeviceJoined` event:
	- File: `herdsman/src/controller/controller.ts/onDeviceJoined()`
	- This function create new `device` object and initiate interview process: `await device.interview();`
- **Start interviewing**:
	- File: `herdsman/src/controller/model/device.ts/interview()`
	- First `interviewInternal()` for normal device
	- If failed when `interviewInternal()`, try `interviewQuirks()` for shorter process using to interview Tuya devices
- Main function to execute interviewing:
	- File: `herdsman/src/controller/model/device.ts/interviewInternal()`
	- Processes:
		- Node descriptor: `await nodeDescriptorQuery()`
		- Match descriptor: `matchDescriptors`
		- Active endpoint: `activeEndpoints`
		- Simple descriptor: `simpleDescriptor`
- After interviewing, event "DeviceInterview" will be emitted
	- Function: `this.selfAndDeviceEmit(device, Events.Events.deviceInterview, event);`
- Zigbee2MQTT will handle "DeviceInterview" event emitted by `herdsman`
	- Function: `z2m/lib/zigbee.ts/this.herdsman.on('deviceInterview'`
	- **Device definition is created** in function `z2m/lib/zigbee.ts/this.logDeviceInterview(d);`
		- In function `if (data.device.definition)`
			- In function `z2m/lib/model/device.ts/get definition()`
				- In function `this._definition = zigbeeHerdsmanConverters.findByDevice(this.zh);`
					- In function `converters/index.js/function findByDevice(device)`
	- Using `eventBus` to emit  "DeviceInterview" event

## Device configure:
- Trigger: `z2m/lib/zigbee.ts/this.herdsman.on('deviceInterview'/this.eventBus.emitDeviceInterview(d);`
- Flow: In function `z2m/lib/extension/configure.ts/start()/this.eventBus.onDeviceInterview(this, (data) => this.configure(data.device, 'zigbee_event'));`
	- In function `configure()`
		- In function `await device.definition.configure(`
			- Then to configure of device definition in `converters`

## Device control:
- Write/read commands
	- Trigger: By sending MQTT control messages
	- Flow: In function `z2m/lib/extension/publish.ts/onMQTTMessage(`
		- Write command: `if (parsedTopic.type === 'set' && converter.convertSet)`
		- Read command: `else if (parsedTopic.type === 'get' && converter.convertGet)`
- Report commands
	- Trigger: By receiving MQTT report message
	- Flow: `z2m/lib/zigbee.ts/this.herdsman.on('message')` -> emit DeviceMessage event `this.eventBus.emitDeviceMessage()`
		- In function `z2m/lib/extension/receive.ts/this.eventBus.onDeviceMessage(this, this.onDeviceMessage);`
			- In function `z2m/lib/extension/receive.ts/onDeviceMessage()`
				- Handle report `const converted = await converter.convert()`



# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 

