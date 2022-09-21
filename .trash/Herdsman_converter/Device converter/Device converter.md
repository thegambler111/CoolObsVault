# 
```js
{
	fingerprint: [{modelID: 'TS011F', manufacturerName: '_TZ3000_cfnprab5'}],
	zigbeeModel: 'TS011F',
	model: 'SM-0306E-2W',
	vendor: 'UseeLink',
	description: '4 gang switch, with USB',
	fromZigbee: [fz.on_off, fz.ignore_basic_report],
	toZigbee: [tz.on_off, tz.tuya_switch_power_outage_memory],
	extend: extend.switch(),
	meta: {multiEndpoint: true},
	options: [exposes.options.invert_cover()
            .withDescription('Inverts the cover position, true: open=100,close=0, false: open=0,close=100 (default false).'),
        ],
	exposes: [
		e.switch().withEndpoint('l1'),
		e.switch().withEndpoint('l2'),
		e.switch().withEndpoint('l3'),
		e.switch().withEndpoint('l4'),
		e.switch().withEndpoint('l5'),
		exposes.enum('power_outage_memory', ea.ALL, ['off', 'on', 'restore'])
			.withDescription('Recover state after power outage'),
		exposes.enum('indicator_mode', ea.ALL, ['off', 'status', 'position', 'on'])
			.withDescription('Plug LED indicator mode'),
		e.child_lock(),
	],
	configure: async (device, coordinatorEndpoint, logger) => {
		for (const ID of [1, 2, 3, 4, 5]) {
			await reporting.bind(device.getEndpoint(ID), coordinatorEndpoint, ['genOnOff']);
			await device.getEndpoint(ID).read('genOnOff', ['onOff']);
		}
		const endpoint = device.getEndpoint(1);
		await reporting.tuyaIndicatorMode(endpoint);
		await reporting.tuyaChildLock(endpoint);
		await reporting.tuyaPowerOutageMemory(endpoint);
		await endpoint.read('genOnOff', ['onOff', 'tuyaChildLock', 'tuyaBacklightMode', 'moesStartUpOnOff']);
	},
	endpoint: (device) => {
		return {'l1': 1, 'l2': 2, 'l3': 3, 'l4': 4, 'l5': 5};
	},
	onEvent: async (type, data, device, options) => {
		// Set manual read for devices which do not support reporting
		// Store in globalStore
	}
},
```

- All of this information will be stored in `device.definition`
	- In `toZigbee/convertSet`, it will be stored at `meta.mapped`
- `fromZigbee` is called at `z2m/lib/extensions/receive.ts/onDeviceMessage`
- `toZigbee` is called at `z2m/lib/extensions/publish.ts/onMQTTMessage`

- `fingerprint`: Pair of modelID and manufatrerName: Device identifier
- `zigbeeModel`: Second device identifier
- `fromZigbee`: [[01_Experience/IoT/Zigbee2MQTT/Herdsman_converter/fromZigbee/fromZigbee|fromZigbee]]
- `toZigbee`: [[01_Experience/IoT/Zigbee2MQTT/Herdsman_converter/toZigbee/toZigbee|toZigbee]]
- `exposes`: Show in `expose` tab of device on frontend, mostly for controlling and viewing attributes
- `configure`: What to do when configuring device in interview
	- You can change `configure` from `=>` assign to `function() =` assign and use `this` to modify other field like `options` (this.options) or `exposes` (this.exposes)
		- However, when you reset the Gateway, all changes this way will be reverted >.<
	- Incomplete list of configuration actions
		- Binding endpoints
		- Setting up reports
		- Read attribute values
- `endpoint`: Define endpoints if device has multiple endpoints
- `meta`: Define value to be returned by `converters/lib/utils.getMetaValue()`
- `options`: Control device_options
	- Expose in front-end in tab `Settings (specific)`
	- Trigger function `z2m/extensions/bridge.ts/changeEntityOptions()`
	- These device_options are stored in devices section of `data/configuration.yaml`
		- For example: `invert_cover` is a device_options, defined in `options` above
```
devices:
  '0x84fd27fffe8aad5c':
    friendly_name: '0x84fd27fffe8aad5c'
    invert_cover: false
```

- `onEvent`: Set manual read for devices which do not support reporting
	- Trigger in `z2m/lib/extensions/onEvent.ts/callOnEvent()` when:
		- onDeviceMessage
		- onDeviceJoined
		- onDeviceInterview
		- onDeviceAnnounce
		- onDeviceNetworkAddressChanged
		- onEntityOptionsChanged


# 

---
- Status: #done

- Tags: #z2m

- References:
	- 

- Related:
	- 
