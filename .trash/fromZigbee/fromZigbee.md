# 
## Trigger when
- This trigger when receiving Zigbee message (usually attribute report messages)

## Components
### Type 1: Normal
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

- `cluster`: Cluster of attribute
- `type`: command type (Need verify: should be command defined in cluster)
- `convert`: How to translate message data
	- `property`: the attribute which is reported, see `herdsman/cluster.ts` for the correct name
	- `lookup`: How to translate the data
		- This needs to be the opposite of `toZigbee` ([[01_Experience/IoT/Zigbee2MQTT/Herdsman_converter/toZigbee/toZigbee|toZigbee]])
		- This needs to be similar to `expose` values in `converters/device/tuya.js`
	- `return`: 
		- `key`: = attribute name in `expose`
		- `value`: must be translated to `expose` value

### Type2: Tuya specific
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


- `cluster`: Cluster of attribute
- `type`: command type (Need verify: should be command defined in cluster)
- `convert`: How to translate message data
	- `dp`: Data point, the attribute which is reported, see `herdsman/cluster.ts` for the correct name
		- If attribute is not supported, get data point of attribute from message data with [[01_Experience/IoT/Zigbee2MQTT/Herdsman_converter/EF00 message data/EF00 message data|EF00 message data analyze example]]
	- `return`: 
		- `key`: = name in `expose`
		- `value`: must be translated to `expose` value



# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 
