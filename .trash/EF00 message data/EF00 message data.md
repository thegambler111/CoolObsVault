# Data
- From `herdsman/zcl/buffaloZcl.ts/`
- 00 0f 1c 04 00 01 02

	- First 2 bytes (00 0f) are sequence number
	- Next byte (1c) is data point for attribute identification (i.e. 1c = 28 = indicator_mode)
	- Next byte (04) is data type (i.e. 04 = int8/enum, 01 = boolean)
	- Next 2 bytes (00 01) are data length
	- The rest of the bytes (02) are data value

- 01 00 02 02 00 04 00 00 01 a8
	- Sequence number: 0x0100
	- Data point: 0x02
	- Data type: 0x02 (Number)
	- Data length: 0x0004 -> Data is 4 bytes
	- Data: 0x000001a8  = 424


- Read more:
	- [Official Tuya command document](https://developer.tuya.com/en/docs/iot-device-dev/tuya-zigbee-universal-docking-access-standard?id=K9ik6zvofpzql#subtitle-6-Private%20cluster)
	- [Tuya Serial Communication Protocol](https://developer.tuya.com/en/docs/iot/tuya-zigbee-module-uart-communication-protocol?id=K9ear5khsqoty)
	- [Tuya Zigbee Generic Interfaces](https://developer.tuya.com/en/docs/iot-device-dev/tuya-zigbee-universal-docking-access-standard?id=K9ik6zvofpzql)


# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
