# Topic
- MQTT topic are made of UTF-8 strings
- Consist of 1 or more topic levels
- Topic levels are separated by forward slash "/"

## Topic rules
- Topic names are Case-sensitive
- A topic should consists of at least 1 character
- The topic name should use only UTF-8 strings

# Topic filtering
- Topic filtering is achieved by topic hierarchy

# Wildcard
- Wildcards (Wildcard character) are symbols used as placeholders to replace or represent one or more characters
- Wildcards can only be use to subscribe to topic not publish
- There are 4 types of wildcards:
	- /
		- Create topic hierarchy
	- $
		- Access default system level topics created by broker ("$SYS" topic)
	- -
		- Single level wildcard
		- Replace 1 topic level
	- \#
		- Multi level wildcard
		- Replace all topic of all lower layers where the hash is used

## Example
- List of topics

```
1. firstFloor/lab/sensorA/hum
2. firstFloor/lab/sensorA/temp
3. firstFloor/lab/sensorB/temp
4. firstFloor/workspace/sensorA/hum
5. firstFloor/workspace/sensorA/temp
```

- `firstFloor/lab/+/temp` = Topic 2 + 3
- `firstFloor/lab/#` = Topic 1 + 2 + 3
- `firstFloor/#` = Topic 1 + 2 + 3 + 4 + 5
- `firstFloor/+/sensorA/hum` = Topic 1 + 4
- `firstFloor/+/sensorA/#` = Topic 1 + 2 + 4 + 5

## System wildcard ($SYS)
- Some information published in these wildcards:
	- Total number of bytes received
	- Total number of bytes sent
	- Number of currently connected clients
	- Total number of message received
	- Total number of dropped messages due to queuing limits

# Topic best practice
- Don't use space character in topic names
- Don't start a topic name with "/"
	- This will create a topic level with zero character
- Don't use long topic names
	- Long topic name will increase packet size
- Include client identifier into the topic
- Have Upgrade possibility in mind when creating topic hierarchy

#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
