```toc
style: number
min_depth: 1
max_depth: 2
title: Table of contents
```

# Reminder
- **Rule of thumb: Only add stuffs to Viettel files. You may only comment not delete or add anything to other files. Leave your name (i.e. haint126) when commenting in non-Viettel file.**
- If you want to add something to non-Viettel files, ask team lead first
- Viettel files will have name containing "viettel", or starting with "vt"


# Check device functionalities
- **This is the most important step**
- Read device teams reports
- Read device's "User manual"
- Pair device with vendor gateway and check on vendor's app
	- [For Tuya devices, follow these instructions to view devices in Tuya Cloud](https://www.zigbee2mqtt.io/advanced/support-new-devices/03_find_tuya_data_points.html#find-tuya-data-points) 
		- In Tuya Cloud, check "Device Debugging" part to view all supported functions
		- NOTE:
			- Some functions may be missing on Tuya app and can only be seen in Tuya Cloud
				- For these functions, check if the devices truly support them, then talk with device team about implementing them or not
			- Some functions may appear on Tuya app but cannot be control
- Pair device with Viettel gateway and check device definition
	- If device is not supported -> Skip this step
- Additional ways:
	- Try call all defined ZCL attributes and methods of all cluster to check if those attributes and methods are supported or not
	- Read code of other similar devices (same modelID)
- When device is not supported, or there are any missing functionalities, make changes to device definition

# Change or create new device definition
- **Always create new definition in `converters/devices/viettel.js`**
- **If there is existing definition and you want to change it, move that specific device definition to `converters/devices/viettel.js`**
	- If there is only fingerprints of your device, copy device definition to `converters/devices/viettel.js` and comment the original
	- If there are multiple fingerprints, comment the original device's fingerprint, then create new device definition in `converters/devices/viettel.js`
	- If device has no fingerprint and only `zigbeeModel`, copy `zigbeeModel` definition to `converters/devices/viettel.js` then add fingerprint
	- If there is no fingerprint, and no `zigbeeModel`, find definition of similar device then copy it to `converters/devices/viettel.js`

## Device definition
- In `z2m`, device definition will be stored in `device.definition`
- In `converters/converters/toZigbee.js/convertSet()`, you can retrieve device definition in `meta.mapped`
- All definitions are loaded when `zigbee-herdsman-converters` library is loaded
	- In `converters/index.js/addDefinition()`
- Example:
```js
fingerprint: [{modelID: 'TS0001', manufacturerName: '_TZ3000_qyf0xkkv'}],
zigbeeModel: 'TS0001',
model: 'TS0001',
vendor: 'TuYa',
description: '1 gang switch',
extend: extend.switch(),
meta: {multiEndpoint: true},
options: [exposes.options.invert_cover()],
whiteLabel: [{vendor: 'Lonsonho', model: 'X701'},
	{vendor: 'Bandi', model: 'BDS03G1'}],
exposes: [e.switch().withEndpoint('l1')],
fromZigbee: [fz.on_off, fz.ignore_basic_report],
toZigbee: [tz.on_off],
endpoint: (device) => {
	return {'l1': 1, 'l2': 2};
},
onEvent: async (type, data, device, options) => {
	// Set manual read for devices which do not support reporting
	// Store in globalStore
}
configure: async (device, coordinatorEndpoint, logger) => {
	await reporting.bind(device.getEndpoint(1), coordinatorEndpoint, ['genOnOff']);
	await reporting.bind(device.getEndpoint(1), coordinatorEndpoint, ['genBasic']);
	await vtReporting.tuyaThaiBinhStatusReport(device.getEndpoint(1));
},
ota: ota.zigbeeOTA,
```

### fingerprint
- Specific device identifier
	- i.e. `{modelID: 'TS0001', manufacturerName: '_TZ3000_qyf0xkkv'}
- It includes modelID and manufacturerName
- modelID: ZCL Cluster Basic, attribute ModelIdentifier (0x0005)
- manufacturerName: ZCL Cluster Basic, attribute ManufacturerName (0x0004)

### zigbeeModel
- Group device identifier
	- i.e. `'TS0001'`

### model
- Vendor model number, look on the device for a model number

### vendor
- Vendor of the device (only used for documentation and startup logging)

### description
- Description of the device, copy from vendor site. (only used for documentation and startup logging)

### extend
- Contains definition to inherit from.
- Add all fields in extend definition that are not in current definition will be added
- For more insight, read `converters/index.js/addDefinition()`

### meta
- Additional data of the device, used when these data is not stored on ZCL attributes and should not be controlled by user
- Define values to be returned by `converters/lib/utils.js/getMetaValue()`
- Usually is used in `converters/converters/toZigbee.js`, stored in function at `meta.mapped.meta`

### options
- **You should NEVER use `options` because it can not be controlled through MQTT message, thus cannot be controlled by end user**
- Additional data of the device, used when these data is not stored on ZCL attributes and can be controlled by user
- Can be controlled in frontend in tab `Settings (specific)`
- Usually is used in `converters/converters/toZigbee.js`, stored in function at `meta.options`
- When changed in frontend, it will trigger function `z2m/extensions/bridge.ts/changeEntityOptions()`
- These options are stored in devices section of `data/configuration.yaml`
	- For example: `invert_cover`, defined in `options` above, will be stored like this
```
devices:
  '0x84fd27fffe8aad5c':
    friendly_name: '0x84fd27fffe8aad5c'
    invert_cover: false
```

### whiteLabel
- No idea, please search for it and share your finding

### exposes
- Device information, defined either on an attributes or read from a report
- Show in `expose` tab of device on frontend, mostly for controlling and viewing attributes
- Basic and pre-defined exposes can be found in `converters/lib/exposes.js`
	- You can change some part of pre-defined exposes by using base function
- Exposes have 2 main values:
	- `name` is used to identify the expose
	- `access`:
		- STATE: Information can be viewed by user
		- SET: Information can be changed by user
		- GET: Information can be manually read from device
		- STATE_SET: STATE + SET
		- STATE_GET: STATE + GET
		- ALL: STATE + SET + GET
- Exposes are controlled by functions in `fromZigbee` and `toZigbee`

### fromZigbee
- When receiving Zigbee message, z2m search all fromZigbee functions, find the correct ones to process the message

#### Type 1: Report attribute and read attribute response of ZCL cluster
- Example:
```js
ts011f_plug_child_mode: {
	cluster: 'genOnOff',
	type: ['attributeReport', 'readResponse'],
	convert: (model, msg, publish, options, meta) => {
		const property = 'tuyaChildLock'; // Look at herdsman/cluster.ts attribute name
		if (msg.data.hasOwnProperty(property)) {
			const value = msg.data[property];
			const lookup = {0: 'unlock', 1: 'lock'};
			if (lookup.hasOwnProperty(value)) {
				return {'child_lock': lookup[value]};
			}
		}
	},
},
```

- `cluster`: Zigbee cluster of the message
- `type`: Command type: global or cluster specific
- `convert`: How to process message data
	- `property`: the attribute which is reported or read, see `herdsman/cluster.ts` for the correct name
	- `lookup`: How to translate the data
		- This needs to be the same as lookup in `toZigbee` but with key-value swapped
		- The keys need to be similar to `expose` values in `converters/devices/tuya.js`
	- `return`: 
		- `key`: attribute name in `expose`
		- `value`: must be translated to `expose` values

#### Type2: Tuya specific
- Example:
```js
viettel_tuya_electric_meter: {
	cluster: 'manuSpecificTuya',
	type: ['commandDataResponse', 'commandDataReport', 'commandActiveStatusReport'],
	convert: (model, msg, publish, options, meta) => {
		const dpValue = tuya.firstDpValue(msg, meta, 'viettel_tuya_electric_meter');
		const dp = dpValue.dp;
		const value = tuya.getDataValue(dpValue);
		switch (dp) {
		case tuya.dataPoints.state: // DPID that we added to common
			return {'state': value ? 'ON' : 'OFF'};
		case tuya.dataPoints.dinrailPowerMeterTotalEnergy:
			return {'energy': value/100};
		case tuya.dataPoints.dinrailPowerMeterCurrent:
			return {'current': value/1000};
		case tuya.dataPoints.dinrailPowerMeterPower:
			return {'power': value/10};
		case tuya.dataPoints.dinrailPowerMeterVoltage:
			return {'voltage': value/10};
		case tuya.dataPoints.vtElectricMeterChildLock:
			return {'child_lock': tuya.vtElectricMeter.childLock[value]};
		case tuya.dataPoints.vtElectricMeterIndicatorMode:
			return {'indicator_mode': tuya.vtElectricMeter.indicatorMode[value]};
		case tuya.dataPoints.vtElectricMeterPowerOutageMemory:
			return {'power_outage_memory': tuya.vtElectricMeter.powerOutageMemory[value]};
		default:
			meta.logger.warn(`fromZigbee:viettel_tuya_electric_meter: NOT RECOGNIZED DP #${
				dp} with data ${JSON.stringify(dpValue)}`);
			break;
		}
		return null;
	},
},
```

- `cluster`: Zigbee cluster of the message
- `type`: Command type: global or cluster specific
- `convert`: How to process message data
	- `dp`: Data point, the attribute which is reported, see `herdsman/src/zcl/definition/cluster.ts` for the correct name
		- If attribute is not supported, get data point of attribute from message data with [[#Tuya 0xEF00]]
	- `return`: 
		- `key`: attribute name in `expose`
		- `value`: must be translated to `expose` values

### toZigbee

- `ConverSet`: When you want to change the state of the device, you can change it in gateway frontend or directly send `set` MQTT message
- `ConverGet`: When you want to manually read the state of the device, you can click reload button it in gateway frontend or directly send `get` MQTT message

#### Type 1: Read attribute and write attribute of ZCL cluster
```js
ts011f_plug_child_mode: {
	key: ['child_lock'],
	options: [exposes.options.invert_cover()],
	convertSet: async (entity, key, value, meta) => {
		value = value.toLowerCase();
		const lookup = {'unlock': 0x00, 'lock': 0x01};
		utils.validateValue(value, Object.keys(lookup));
		await entity.write('genOnOff', {0x8000: {value: lookup[value], type: 0x10}});
		return {state: {'child_lock': value}};
	},
	convertGet: async (entity, key, meta) => {
		await entity.read('genOnOff', ['tuyaChildLock']);
	},
},
```

- `key`: Attribute name which is defined in `expose`
- `options`: (Need to read more) Same as option in device definition
- `convertSet`:
	- `value`: Attribute value from MQTT message
		- If it is text, we need to transform it to lowercase
	- `lookup`: How to translate value to payload of Zigbee message
		-  This needs to be the same as lookup in `fromZigbee` but with key-value swapped
		- This needs to be similar to `expose` values in `converters/devices/tuya.js`
	- `utils.validateValue`: Validate if value is in `lookup`
	- `await entity.write`: send `write_attribute` command
		- The first argument is cluster name from `herdsman/cluster.ts`
		- The second argument is command payload:
			- `key`: Attribute ID or Attribute name from `herdsman/cluster.ts` or from `simple_descriptor` message
			- `value`: must be translated into number
			- `type`: Can be seen from `simple_descriptor` message or get from`herdsman/cluster.ts` 
	- `return`: Changed state (attributes) of device
		- New state will be store in Z2M
		- If there is any change to the state, Z2M send a MQTT message to report new device state which will change the frontend
		- `state`: Indicate the state of the device
		- `key` ('child_lock' in the example): = attribute name in `expose`
		- `value`: should be similar to `expose` values in `converters/devices/tuya.js`

- `convertGet`:
	- `await entity.read`: send `read_attribute` Zigbee command
		- `key`: Attribute ID, from `herdsman/cluster.ts` or from `simple_descriptor` message
		- The second argument is list of attribute names you want to read, see `herdsman/cluster.ts` for the correct name
	- For cluster 'manuSpecificTuya', do not set `convertGet`
		- (Need to verify) There is no 'attribute_report' command for that cluster 

#### Type 2: Tuya specific
- Example:
```js
vt_tuya_dimmer_switch_dme: {
	key: ['light_mode'],
	convertSet: async (entity, key, value, meta) => {
		if (typeof value === 'string' || value instanceof String) {
			value = value.toLowerCase();
		}
		const result = {};
		let lookup;
		switch (key) {
		case 'light_mode':
			lookup = {'on': 0, 'indicator': 1, 'off': 2};
			utils.validateValue(value, Object.keys(lookup));
			await tuya.sendDataPointEnum(entity, vt.dataPoints.vtTuyaDimmerLightMode, lookup[value]);
			result[key] = value;
			break;
		}
		return {state: result};
	},
},
```
- For Tuya cluster, the only different is command to change attribute:
	- Use set of functions `sendDataPoint___` in `converters/lib/tuya.js`:
		- `sendDataPointBool` for Boolean datatype
		- `sendDataPointValue` for value datatype
		- `sendDataPointEnum` for enum datatype
		- ...
	- The first argument is endpoint
	- the second argument is dataPoint
	- The last argument is data value


### endpoint
- (Need to verify) Specify name for each endpoint

### onEvent
- One function is to set manual read for devices which do not support reporting
	- Trigger in `z2m/lib/extensions/onEvent.ts/callOnEvent()` when:
		- onDeviceMessage
		- onDeviceJoined
		- onDeviceInterview
		- onDeviceAnnounce
		- onDeviceNetworkAddressChanged
		- onEntityOptionsChanged
- Need to read more!!!

### configure
- Setup the devices after interview
- (Need to read more) Incomplete list of configuration actions:
	- Bind device endpoints to gateway endpoint:
		- Whenever device state changes, it will send reports to bound devices
		- Use `await reporting.bind()
	- Set up reports:
		- If device does not send report by default, we set it up
		- Use predefined report or `await endpoint.configureReporting()
	- Read attribute values:
		- When device first join in, gateway will not know any of device information. If device does not report all information, we need to read it manually
		- Use `await endpoint.read` or cluster specific command
- Additional knowledge, do not use in real project:
	- You can change `configure` from `=>` assign to `function() =` assign and use `this` to modify other field of device definition like `options` (this.options) or `exposes` (this.exposes)
	- However, when you reset the Gateway, all those changes will be reverted

### ota
- Need to read more!!!
- Enable device firmware update through gateway

## How to add new reporting
- Create payload: payload = (`attribute` , `minimumReportInterval`, `maximumReportInterval`, `reportableChange`)
	- `attribute`: Attribute name
	- `minimumReportInterval`:
		- (Need to verify) Minimum time in second to send a report
		- Even when device state constantly changes, new report is only sent after minimumReportInterval senconds
	- `maximumReportInterval`:
		- (Need to verify) Maximum time in second to send a report
		- Even when device state does not change, new report is sent after maximumReportInterval senconds
	- `reportableChange`:
		- (Need to verify) How much the attribute changes compare to the last report to count as device state changes
		- (ZCl 2.5.7) Depend on datatype in ZCL 2.6.2:
			- For attributes with 'analog' data type, the field has the same data type as the attribute
			- For attributes of 'discrete' data type, this field is omitted
		- Example: If reportableChange = 2 for attribute temperature, device only send report when the temperature increase or decrease more than 2 (in attribute value) than the last report
- Send configure reporting command: `await endpoint.configureReporting(cluster, payload)
	- `cluster`: Cluster name
	- `payload`: payload above

## How to add new functionalities
- Check for device functionalities
- For each functionality, find:
	- Cluster
	- Attribute name (may not needed if control purely by command)
	- Command to read and write (change) attribute
	- Command payload
	- How to translate command payload from number to real life information
	- How to setup reporting (may not needed if device auto report)
- Add to `expose` in device definition:
	- Expose name
	- Expose values
	- Expose access
	- Expose description
- Add to `toZigbee`
	- `convertSet`
		- If there are multiple keys (each key is an expose name and attribute), handle each key separately
		- If value is in form of `string`, change it to lowerCase:
			- Check if value is string: `if (typeof value === 'string' || value instanceof String)`
			- Change string to lowerCase: `value = value.toLowerCase();`
		- Create a lookup to translate from information to payload number:
			- `const lookup = {'decrease_hue': 0, 'increase_hue': 1};`
		- Validate if value is correct
			- `utils.validateValue(value, Object.keys(lookup));
		- Return new changed attribute:
			- `return {state: {color_loop_direction: value}};`
	- `convertGet`
		- Add read command
			- `await entity.read(clusterName, ["listOfAttributesToRead"]);` 
- Add to `fromZigbee`
	- Check if function is processed: `if (hasAlreadyProcessedMessage(msg)) return;`
	- Check if payload contained the attribute you want to process:
		- `if (msg.data.hasOwnProperty("attributeName"))`
	- Get attribute value:
		- `const value = msg.data["attributeName"];`
	- Define lookup to translate payload to information:
		- `const lookup = {0: 'open', 1: 'stop', 2: 'close'};`
	- Return result:
		- `return {exposeName: lookup[value]};
- Add to `configuration`
	- Add binding if the cluster is not bound yet
		- `await reporting.bind(endpoint, coordinatorEndpoint, ["listOfClusterNames"])
	- Check if the attribute is automatically reported by device:
		- Change the attribute, check if there is any Zigbee report message of the attribute
		- If there is no report message, add one
			- Read above for how to add a report
	- Check if when device is pair, the attribute is auto reported
		- If it is not reported, read it manually:
			- `await endpoint.read('clusterName', ['listOfAttributes']);
- If there is any additional information that is not store in ZCL attributes:
	- If this information is constant and should not be control by user, store them in `meta`
	- If this information should be control by user:
		- Create an `expose` and `toZigbee` function with only `convertSet` for it
			- Do not call write command in `convertSet`
			- These will enable attribute to be controlled by user
			- For example: Function `vttz.vt_bulb_enable_transition_time_for_onoff`
		- Read it in `configuration` by adding its default value in `return`  in `fromZigbee` of related attribute
			- This will enable attribute to be read when configure device
			- For example: In function `vtfz.vt_bulb_on_off`:
				- `!meta.state.hasOwnProperty('onoff_transition')`: Check if additional attribute `onoff_transition` is initiated yet
				- `result.onoff_transition = 'false';` will return initiated value of attribute


# Verify device definition

## Check if all attributes are read after interview
- After interview, check MQTT messages (using MQTT explorer)
- All device attributes should be presented in MQTT message
- If any attributes are missing, you need to read in manually in `configurate`

## Check if all attributes are changed correctly
- For each attribute, do as follow:
	- Change attribute in Gateway frontend, check with sniffer
		- Check if the payload in sent command is correct
		- Check if device response is OK
		- Check if device physically change correctly
		- Check if there is report of attribute changed
		- Check if frontend changed
		- Check if there is MQTT report message
	- Change attribute using MQTT message, check with sniffer:
		- Check those steps above
		- Check if attribute value in string can be in both upper and lower case
			- Example: Send 2 MQTT messages with different cases:
				- {"state": "oFF"}
				- {"state": "OfF"}


# Tricks
## Setup reporting
- In `converters/devices/viettel.js/configure:` , first use `reporting.bind` to receive default reporting from device
- If there are missing reports, use pre-defined `reporting` in `converters/lib/vtReporting.js` or `converters/lib/reporting.js`
	- If their is no correct pre-defined one, create it


## Setup auto read for device that not support reporting
- Using `onEvent` in `converters/devices/viettel.js`


# How Z2M works

## How Z2M find the correct device definition
- Device definition is collected in `z2m/lib/model/device.ts/get definition()`
	- Specifically `converters/index.ts/findByDevice`
- `modelID` is looked up first
	- If there is only 1 matching `modelID`, and the definition contain `zigbeeModel`, return it immediately
	- `modelID` = `fingerprint.modelID` OR `zigbeeModel`
- If there are multiple results from `modelID`, then `fingerprint` is looked up next
	- Return the first matching `fingerprint` (matching of all fields)
- If there is no matching `fingerprint`, then `zigbeeModel` is looked up
	- Return the first matching `zigbeeModel`



## Vendor specific cluster
### Tuya 0xEF00
- You can find how herdsman decode the data here `herdsman/zcl/buffaloZcl.ts/readListTuyaDataPointValues()`
- Example 1: 00 0f 1c 04 00 01 02
	- First 2 bytes (00 0f) are sequence number
	- Next byte (1c) is data point for attribute identification (i.e. 1c = 28 = indicator_mode)
		- Attribute identification can be find at `converters/lib/tuya.js/dataPoints` or `converters/lib/viettel.js/dataPoints`
	- Next byte (04) is data type (i.e. 04 = int8/enum, 01 = boolean)
	- Next 2 bytes (00 01) are data length
	- The rest of the bytes (02) are data value

- Example 2: 01 00 02 02 00 04 00 00 01 a8
	- Sequence number: 0x0100
	- Data point: 0x02
	- Data type: 0x02 (Number)
	- Data length: 0x0004 -> Data is 4 bytes
	- Data: 0x000001a8  = 424

#### Reference:
- [Official Tuya command document](https://developer.tuya.com/en/docs/iot-device-dev/tuya-zigbee-universal-docking-access-standard?id=K9ik6zvofpzql#subtitle-6-Private%20cluster)
- [Tuya Serial Communication Protocol](https://developer.tuya.com/en/docs/iot/tuya-zigbee-module-uart-communication-protocol?id=K9ear5khsqoty)
- [Tuya Zigbee Generic Interfaces](https://developer.tuya.com/en/docs/iot-device-dev/tuya-zigbee-universal-docking-access-standard?id=K9ik6zvofpzql)
- [View Tuya device on Tuya Cloud](https://www.zigbee2mqtt.io/advanced/support-new-devices/03_find_tuya_data_points.html#find-tuya-data-points)










# 

---
- Status: #done

- Tags: #z2m

- References:
	- 

- Related:
	- 
