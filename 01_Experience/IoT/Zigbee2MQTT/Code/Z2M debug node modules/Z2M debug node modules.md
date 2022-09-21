# Debug on console
- Use [module debug](https://www.npmjs.com/package/debug)
- To show debug on console use:
```bash
DEBUG={module_name}* node start
```
- Example:
	- `DEBUG=mqttjs* node start`
	- `DEBUG=zigbee-herdsman* node start`

# Store debug on a file
- [Source](https://stackoverflow.com/questions/29448156/write-the-contents-of-node-debug-log-to-file/66583847#66583847)
- To store debug to a file:
```bash
DEBUG={module_name}* node start 2> debug.txt
```
- Example:
	- `DEBUG=mqttjs* node start 2> debug.txt`
	- `DEBUG=zigbee-herdsman* node start 2> debug.txt`


- In Windows, use 'set' before assign variable

# 

---
- Status: #done

- Tags: #z2m #ts #js

- References:
	- 

- Related:
	- 
