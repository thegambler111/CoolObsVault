#

## CTRL + C on terminal

![](https://i.ibb.co/Hzvy0f2/Ctrl-C-2.png)

### Step 1: SIGTERM signal will trigger the stop process

### Step 2: Stop all extensions of zigbee2mqtt

- Removing listener from listerner array of all events registered on each extension: Bridge, publish, receive, deviceGroupMembership, configure, networkMap, groups, bind, onEvent, OTAUpdate, report, externalExtension.

### Remove listener for event:
- Controller: 
	- adapterDisconnect
	- lastSeenChanged
- State:
	- deviceLeave
- MQTT:
	- publishAvailability

### Step 4: Stop state

- Remove listener of events registered in State (deviceLeave)
- Clear interval of periodically saving state
- Saving state to file

### Step 5: Disconnect MQTT

- Publish “offline” to MQTT topic ‘bridge/state’
- Remove listener for events registered of MQTT: publishAvailability

### Step 6:

- Save database
- Remove all listener of adapter events: deviceJoined, zclData, rawData, disconnected, deviceAnnounce, deviceLeave.
- Disable device join
- Clear interval of periodically backing up and saving database
- Writing coordinator backup to file

### Step 7: Emit event and do nothing

- Call adapter.stop() to emit ‘close’ event. However this event only continue emitting Events.disconnected if it’s triggered by UNPLUGGING USB. In this CTRL + C case, the process stop here.

---

## UNPLUG THE USB

_Adapter Event: adapterDisconnected_
![](https://i.ibb.co/ssbqdhM/UNPLUG.png)

### Step 1: Emit and listen to events

### Step 2: Stop controller

- Do the same as [Step 2](#step-2-stop-all-extension-of-zigbee2mqtt) -> [Step 6](#step-6) of [CTRL + C process](#ctrl--c-on-terminal)

---

## New Device Join

_Adapter Event: deviceJoined_

![]()

### Step 1: Emit and listen to events

### Step 2: Stop controller

- Publish Device
- Publish Event
-

#

---

- Status: #done

- Tags:

- References:
	- [Source]()

- Related:
