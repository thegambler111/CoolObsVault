# CPU overload
- Using 'Monit' to restart service
- Using PM2 to auto scale

# Error when setting up the Gateway
![[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M setup Orange Pi Zero/Z2M setup Orange Pi Zero#Error handling]]


# Error when changing converters/tuya.js
```
UnhandledPromiseRejectionWarning: TypeError: Cannot read property 'options' of undefined
at addDefinition (/opt/zigbee-herdsman-converters/index.js:91:23)

OR

/opt/zigbee-herdsman-converters/index.js:91                                                                     if (converter.options) {                                                                                              
              ^                                                                                 TypeError: Cannot read property 'options' of undefined 

```

## Solution
- Check `fromZigbee` and `toZigbee` part of the newly changed device
	- Maybe wrong function name


# MQTT message with payload contain "action": ""

## Reason
- This error happens when there is an attribute with name "action" and home-assistant is enable
	- Some how, message from home-assistant will return "action" with empty value

## Solution
- Change attribute name to something other than "action"

# Error: Data request failed with error: 'MAC channel access failure'

## Reason
- Sonoff USB is too close to the Gateway

## Solution
- Use an USB cable and move the Sonoff USB at least 30 cm away from Gateway


# Error "Cannot find module ..." when setting up the server for the first time:
## Reason
- Trouble with installed package

## Solution
- Use `npm ls` to check installed packages and their status
- Remove `node_modules` folder of trouble project and `npm ci` to reinstall


# Devices in a Z2M Gateway do not appear in HA or appear for a short period then disappear

## Reason
- 2 Gateway have the same mqtt base_topic

## Solution
- Give each gateway a unique mqtt base_topic

# Gateway cannot connect to MQTT broker from 1 place but can connect in another place
## Reason
- MicroSD card I/O is slow or the card's quality is low

## Solution
- Replace MicroSD card
























# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 
