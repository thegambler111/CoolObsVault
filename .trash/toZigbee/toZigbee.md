# 
## Trigger when
- This trigger when:
	- `ConverSet`: When receiving `set` MQTT message (like when changing attribute in frontend)
	- `ConverGet`: When receiving `get` MQTT message (like when clicking reload button of an attribute in frontend)

## Components
```js
ts011f_plug_child_mode: {
	key: ['child_lock'],
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

- `key`: = attribute name in `expose`

- `convertSet`:
	- `value`: Attribute value from MQTT message
		- If it is text, it should always be in lowercase
	- `lookup`: How to translate value to data in Zigbee message
		- This needs to be the opposite of `fromZigbee` ([[01_Experience/IoT/Zigbee2MQTT/Herdsman_converter/fromZigbee/fromZigbee|fromZigbee]])
		- This needs to be similar to `expose` values in `converters/device/tuya.js`
	- `utils.validateValue`: Validate if value in lookup (can be translated)
	- `await entity.write`: send `write_attribute` message
		- The first argument is cluster name from `herdsman/cluster.ts`
		- The second argument is payload:
			- `key`: Attribute ID, from `herdsman/cluster.ts` or from `simple_descriptor` message
			- `value`: must be translated
			- `type`: Can be seen from `simple_descriptor` message
	- `return`: Changing state (attributes) of device store in Z2M and send a MQTT message when change happens
		- This will change the frontend, same with when receiving `attribute_report` Zigbee message
		- `state`: ?
		- `key` ('child_lock' in the example): = attribute name in `expose`
		- `value`: should be similar to `expose` values in `converters/device/tuya.js`

- `convertGet`:
	- `await entity.read`: send `read_attribute` message
		- `key`: Attribute ID, from `herdsman/cluster.ts` or from `simple_descriptor` message
		- The second argument is list of attribute names you want to read, see `herdsman/cluster.ts` for the correct name
	- For cluster 'manuSpecificTuya', do not set `convertGet`
		- Cause there is no 'attribute_report' message for that cluster (?)


# 

---
- Status: #done

- Tags: #z2m

- References:
	- 

- Related:
	- 
