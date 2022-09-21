# Base device behavior 
- Beacon request
- Beacon
	- Beacon:
		- Device depth: 0 = Coord, 
		- Extended PanID:
	- Superframe:
		- Pan coordinator: true -> This is Coor
		- Association permit: true -> permit join
- Priority: High LQI (maybe depends on low device depth)
- Association request
	- Device type: FFD/RFD
	- Receive on when idle: Receive messages on when idle
	- Extended source: Device MAC: First 3 bytes is company indicator
	- Source addr capability true: Except network ID
- Association response: `herdsman/controller/controller.ts/onDeviceJoined()`
	- Extended source: C MAC
	- Short addr: Device network ID
- Transport key: Collect network key

- Device announcement:
	- Destination: 0xfffd: Send to all Coordinator + Router
	- Capability information ~ Association request

- Read attributes: coor -> Device
	- Appli support:
		- Destination endpoint
		- Cluster: Basic
		- Cluster profile: Home Automation
		- Source endpoint:
	- Direction: Client to servers (read Zigbee docs)
	- Disable default response: True (does not except default response)
	- Command: always from client -> server
- Read attribute response: Return device info to coor
	- Manufacture name
	- Model identifier
	- Direction: Server -> client (read Zigbee docs)

- Read attributes:
- Read attribute response:

- MAC descriptor request: (for security devices) (tuya always ask after read attribute?)
	- Input cluster list: Ask if device has this cluster
- MAC descriptor response:
	- Status: Success
	- Endpoint count: 0 -> No endpoint has asked cluster
`herdsman/controller/model/controller.ts/onDeviceJoined()`
- Node descriptor request: (Device can also ask GW this)
- Node descriptor response:
	- Node descriptor:
		- Type: Coord/router/device
	- Capability:
	- Manufactory code:
	- Max buffer size: Buffer size of MAC layer (number of bytes)
	- Manufacturer code: 0x1002 (Silicon lab)
	- Server flags: (Developer can use to compare GW of different vendors)
		- Network manager: Can or cannot modify Zigbee channel, connection
		- Stack compliance revision
> Node descriptor: Get manufacturer ID
- Match descriptor:
> Match descriptor: Ask if device has Intruder alarm system zone Input Cluster 

- Active endpoint request: Ask for num of endpoints
- Active endpoint response:
	- Active endpoint list:
> Active endpoint request: Ask for num of endpoints

- Simple descriptor request: Ask for cluster in each endpoint
	- Endpoint: 1 (Number of endpoint)
- Simple descriptor response:
	- Endpoint:
	- Profile
	- Input cluster count:
	- Input cluster list:
	- Output cluster count
	- Output cluster list:
> Simple descriptor: Get endpoint details

- Write attributes: Apply default attributes (depend on devices)
- Write attribute response:







Khi Router die, end device sẽ gửi Beacon request
Sau khi nhận Beacon, nếu Extended PanID giống với mạng cũ thì thiết bị sẽ tiến hành Rejoin (kể cả khi association permit False)

Gateway Tuya: chỉ end device hỏi:
Gateway VT: cả end device và coord đều có thể hỏi








```js
endpoint._configuredReportings // Store all attribute change reports

```

- Adding `await reporting` in tuya.js herdsman-converters will add to `endpoint._configuredReportings`

TODO: See which herdsman event emits when an attribute (power_outage_memory, state) changes for reporting to mqtt server





>
0x8002: Relay status:
0x8001: Indicator mode
0x8000: Child lock

- In 'toZigbee.js':
	- In 'convertSet': Happens when click attribute values in `expose`
		- `await entity.write` send Zigbee command to device
		- `return` add changed attributes to MQTT message and trigger a report
	- In 'convertGet': Happens when click Reload button 🔄


- TODO:
	- Clean function
	- Set state return 2 MQTT messages
		- In z2m/extensions/publish.ts: => `toZigbee.ts` => Trigger after successfully `await entity.write`
			- Line 246 `converter.convertSet`. Then line 290 `this.publishEntityState`
		- In z2m/extensions/receive.ts: > `fromZigbee.ts` => Trigger when receive 'Attribute report'
			- `fromZigbee`
				- `property` = herdsman/cluster.ts attribute_name instead of attribute_id
					- "tuyaBacklightMode" instead of 0x8001
	- When will 'Attribute Report' is set
		- When pair or can change anytime
	- Missing 'Attribute Report' for 'child_lock' => Will pair again with `await reporting` in `tuya.js` change things?
	- Trigger a report when receiving zigbee attribute report instead of when changing in frontend
	- Pairing require multiple times
	- Report attribute immediately after reconnect GW or after pairing (Maybe `bind` like switch)

# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 
