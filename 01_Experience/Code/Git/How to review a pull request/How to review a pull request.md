# How to review a pull request

## Device functionalities
- Function in vendor's app
	- Function on Tuya website for Tuya devices
- Function currently support in Z2M
- => Result: List of functions of profile

## Device profile
- Check if Z2M has similar profile
	- Check same ManufacturerName
	- Check same ModelID
		- Check if the profile with same ModelID has all functions of new device -> Add fingerprint
		- Check if the profile with same ModelID can be used as base to create new profile
	- => Result: Base profile
- From base profile
	- Verify existing functions
	- List out what is needed to develop new functions
		- exposes
		- toZigbee
		- fromZigbee
		- configuration:
			- Bind
			- Reporting
			- Initialize
	- => Result: List of need to add functions

## Code structure
- Code syntax
	- Follow predefined eslint -> Download eslint extension in VSCode
- Code logic
	- Check if function works correctly
- Code optimization
	- Check if code is optimized
		- Which line is not needed
		- Which lines can be combined
		- Which logic can become clearer, easier to understand
	- Check if functions can be replace by existing functions

#
---
- Status: #done
- Tags: #git
- References:
- Related:
