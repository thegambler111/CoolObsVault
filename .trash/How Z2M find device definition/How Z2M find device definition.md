# Device definition (read from converters)
- Device definition is collected in `z2m/lib/model/device.ts/get definition()`
	- -> `converters/index.ts/findByDevice`
- `modelID` is looked up first
	- If there is only 1 matching `modelID`, return it immediately
	- `modelID` = `fingerprint.modelID` OR `zigbeeModel`
- If there are multiple results from `modelID`, then `fingerprint` is looked up next
	- Return the first matching `fingerprint` (matching of all fields)
- If there is no matching `fingerprint`, then `zigbeeModel` is looked up
	- Return the first matching `zigbeeModel`



# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 
