# Behavior
- When device is OFF: all commands SHALL be ignored
- When color loop is ACTIVE: it SHALL only be stopped by a deactivate color loop request
	- Incoming color changing commands MAY be ignored
- When receiving command: ColorMode will change first (if needed).
	- Then new color attributes will be converted from old color attributes
	- If new color cannot be converted correctly because of more restricted color range. Device behavior will be manufacturer dependent




# 

---
- Status: #done

- Tags: #zcl #zigbee 

- References:
	- ZCL book

- Related:
	- 
