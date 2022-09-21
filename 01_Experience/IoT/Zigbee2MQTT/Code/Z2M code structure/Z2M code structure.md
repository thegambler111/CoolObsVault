# Important files

- `/index.js`.start() : main file
- `/dist/controller.js`.start(): Controller: Initiate all necessary components
- `/dist/zigbee.js`.start(): Initiate and control Zigbee connection
	- `this.herdman`: Handling Zigbee message
- `/lib/mqtt.ts` : Connect, subscribe, publish,... with MQTT server
	- onMessage(): Log massages from your server to MQTT server
- `/lib/extension/frontend.ts` : Frontend
- `/lib/evenBus.ts`: Handle all events
- `/lib/extension/receive.ts`: Define callbacks for receive messages


#
- `/index.js`.start() : main file
- `/dist/controller.js`.start(): Controller: Initiate all necessary components
- `/dist/eventBus.js`:
	- Define and trigger any events
	- Based on Node library "Event"

# Sequence of event.emitter
- The `EventEmitter` calls all listeners synchronously in the order in which they were registered.
- [Link](https://nodejs.org/api/events.html#asynchronous-vs-synchronous)




# When run "npm start"
- `/index.js`: Main file
	- [checkDist()](https://github.com/haint126/zigbee2mqtt/blob/49d33396518dfba0bac4f88569b56974e24386e7/index.js#L76): Check code version and rebuild code
	- [settings.validate()](https://github.com/haint126/zigbee2mqtt/blob/49d33396518dfba0bac4f88569b56974e24386e7/index.js#L86): Validate settings
	- [controller.start()](https://github.com/haint126/zigbee2mqtt/blob/49d33396518dfba0bac4f88569b56974e24386e7/index.js#L101) -> `/lib/controller.ts`: Start Controller
- `/lib/controller.ts`: Main controller
	- [constructor()](https://github.com/haint126/zigbee2mqtt/blob/49d33396518dfba0bac4f88569b56974e24386e7/lib/controller.ts#L52):
		- this.eventBus -> `/lib/eventBus.ts`
		- this.zigbee -> `/lib/zigbee.ts`
		- this.mqtt -> `/lib/mqtt.ts`
		- this.state -> `/lib/state.ts`
		- this.restartCallback: from arguments
		- this.exitCallback: from arguments
		- this.extensionArgs: Args for defining extensions
		- this.extensions: List of extensions: Each extension handle a job of the system -> `/lib/extension/*`
	- [start()](https://github.com/haint126/zigbee2mqtt/blob/49d33396518dfba0bac4f88569b56974e24386e7/lib/controller.ts#L90):
		- this.state.start() -> `/lib/state.ts`
		- this.zigbee.start(): Start herdsman controller -> `/lib/zigbee.ts`
		- this.zigbee.devices(false): Log all connected devices
		- this.zigbee.permitJoin(settings.get().permit_join): Set permit_join
		- this.mqtt.connect(): Start MQTT connection -> `/lib/mqtt.ts`
		- **this.callExtensions(): Start all extensions**
		- this.publishEntityState(): Send all cached states.
		- this.eventBus.onLastSeenChanged(): Set onLastSeenChanged


- `/lib/eventBus.ts`: Event emitter
	- constructor():
		- this.callbacksByExtension:
			- List of all events and callbacks
			- Format: key: {event, callback}
			- `Key` is the object that initiate the event-callback
	- this.on():
		- Save event callback to `this.callbacksByExtension`
		- Add callback to event using `this.emitter.on()`
	- this.removeListeners(`key`: ListenerKey):
		- Remove all event listeners (saved in  `this.callbacksByExtension[key]`) from `this.emitter`
		- ????? But not remove `key` form`this.callbacksByExtension` 

- `/lib/zigbee.ts`: Zigbee handler
	- constructor()
		- this.herdsman: herdsman controller -> `\zigbee-herdsman\src\controller\controller.ts`
	    - this.eventBus: 
	    - this.groupLookup: ???
	    - this.deviceLookup: ???
	- this.start():
		- herdsmanSettings: settings of herdsman
		- startResult: Status of starting herdsman controller -> `\zigbee-herdsman\src\controller\controller.ts`
		- this.herdsman.on(...): Define herdsman events
		- for (const device of this.devices(false))): Remove devices in blocklist or not in passlist
		- transmitPower: Set herdsman transmit power
	- this.devices(): Get list of devices include or not include Coordinators
		- this.herdsman.getDevices() -> `\zigbee-herdsman\src\controller\controller.ts`
	- this.permitJoin():
		- this.herdsman.permitJoin() -> `\zigbee-herdsman\src\controller\controller.ts`
	- 



- `/lib/mqtt.ts`: MQTT handler -> mqtt library
	- constructor():
		- this.publishedTopics
		- this.connectionTimer
		- this.client
		- this.eventBus
	- this.connect():
		- mqttSettings = settings.get().mqtt: Get setting
		- mqtt.connect(mqttSettings.server, options): Connect to MQTT server
		- this.onConnect -> this.onConnect()
		- this.client.on() -> Using mqtt library `on()` function: [More info](https://www.npmjs.com/package/mqtt)
			- this.client.on('connect', ): Emitted on successful (re)connection (i.e. connack rc=0).
			- this.client.on('error', ): Emitted when the client cannot connect (i.e. connack rc != 0) or when a parsing error occurs.
			- this.client.on('message',): Emitted when the client receives a publish packet
	- this.onConnect():
		- this.connectionTimer = setInterval: Set timer to try connecting to MQTT server => *logger.error every 10s*
		- this.publishStateOnline()
	- **this.publish(): Publish MQTT messages**
		- this.eventBus.emitMQTTMessagePublished():
		- if (!this.isConnected()):
		- this.client.publish():


- `/lib/state.ts`: Saving states of all connected devices
	- constructor():
		- this.state: States of all connected devices
		- this.file: Location of state file (data/state.json)
		- this.timer: Save state interval (default = 5 mins)
		- this.eventBus
	- this.start(): Set run interval to save states
	- this.load(): Read state.json file







- `/lib/util/logger.ts`: Logger
	- cleanup(): Remove old log folders
	- settings.get().advanced.log_rotation: Rotate log files


# Device interview
- ZH Trigger: `/src/controller/controller.ts`
	- `onDeviceJoined()`


- Trigger: `/lib/zigbee.ts`:
	- `this.herdsman.on('deviceJoined')`
	- `this.herdsman.on('lastSeenChanged')`
	- `this.herdsman.on('deviceInterview')`
		- `/lib/extension/bidge.ts`
		- `/lib/extension/onEvent.ts`
	- `this.herdsman.on('deviceAnnounce')`
	- `this.herdsman.on('message')`: Device announce its attributes ?
	- `this.herdsman.on('lastSeenChanged')`
	- `this.herdsman.on('deviceInterview')`
		- `/lib/extension/bidge.ts`
		- `/lib/extension/configure.ts`
		- `/lib/extension/onEvent.ts`

- Trigger: `/lib/zigbee.ts` :`this.herdsman.on('deviceInterview', )`
	- `const device = this.resolveDevice(data.device.ieeeAddr)`
		- `this.resolveDevice()`: Find `Device` or create a new `Device`
			- `this.deviceLookup[ieeeAddr]`: Records of `Device` in `Zigbee` class
			- `device = this.herdsman.getDeviceByIeeeAddr(ieeeAddr)`
			- `device && (this.deviceLookup[ieeeAddr] = new Device(device))` => If `device` exists, then create a new `Device`
			- `device.zh.isDeleted`: Check if `device._deleted`
			- `device.ensureInSettings()`: Add device.ieeeAddr to configuration.yaml
	- `this.eventBus.emitDeviceInterview` -> `this.eventBus.onDeviceInterview`
		- `/lib/extension/bidge.ts`:
			- `this.publishDevices()`:  Publish to mqtt list of devices ?????
				- `const devices`: List of devices
				- `this.zigbee.devices()`: ?????
				- `this.getScenes(endpoint)`: ?????
			- `publishEvent`: Public to mqtt event interview
		- `/lib/extension/onEvent.ts`: Execute `device.definition.onEvent()` ?????
			- `this.callOnEvent()`
				- `zhc.onEvent(type, data, device.zh);`
					- `device.definition.onEvent`
		- `/lib/extension/configure.ts`: Config device ?????
			- `this.configure()`
				- `if (!force)`
				- `device.definition.configure()`
		- `/lib/extension/homeassistant.ts`:
			- `this.onZigbeeEvent`
				- `this.discover()`
		- `/lib/extension/legacy/bridgeLegacy.ts`: Legacy: Public to mqtt log
			- `this.onZigbeeEvent_`
				- `this.mqtt.publish('bridge/log', )`:  Public to mqtt
		- `/lib/extension/legacy/softReset.ts`: Legacy: reset timer
			- `this.resetTimer()`








# EventBus
- onAdapterDisconnected
- onPermitJoinChanged
- onPublishAvailability
- onEntityRenamed
- onDeviceRemoved
- onLastSeenChanged
- onDeviceNetworkAddressChanged
- onDeviceAnnounce
- onDeviceInterview
- onDeviceJoined
- onEntityOptionsChanged
- onDeviceLeave
- onDeviceMessage
- onMQTTMessage
- onMQTTMessagePublished
- onPublishEntityState
- onGroupMembersChanged
- onDevicesChanged
- onScenesChanged
- onReconfigure
- onStateChange


# Zigbee actions

- onDeviceInterview
- onDeviceAnnounce
- onDeviceJoined
- onDeviceMessage
- onDeviceLeave
- onDeviceRemoved








# 

---
- Status: #writing

- Tags: #z2m 

- References:
	- [Source](https://github.com/Koenkk/zigbee2mqtt)

- Related:
	- 
