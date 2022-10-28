# 1. Create device issue

## 1.1. Open empty issue
1. Go to ["Issues" tab of Zigbee-herdsman-converters](https://github.com/ViettelIoTLaboratory/zigbee-herdsman-converters/issues)
2. Click "New issue" button on top right
3. Choose "Open a blank issue"
4. Choose issue information:
	- Labels
	- Project
	- Milestone
5. Fill in the issue's content
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to create new device issue for phase 2/Issue.png]]

## 1.2. Issue content:
```markdown
# Discussion name: Device number Device code (15.2 DMS): Description
# 1. Device information:
- Link to drive

# 2. Requests
## 2.1. Errors
- List of errors and details

## 2.2. Missing functions
- List of missing functions and details


# 3. Priority
- Priority: Low, Normal, High
```

# 2. Check on the project dashboard
- After adding new issue, you should check whether it is on the project dashboard
- [The project dashboard](https://github.com/orgs/ViettelIoTLaboratory/projects/1/views/14)
- Your newly created issue should be the last one under column "Request" in tab "Phase 2 - 2022"
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to create new device issue for phase 2/Project dashboard.png]]

## 2.1. Project dashboard columns:
- No device:
	- When the device in issue is not in HNI lab
- Request:
	- The issue is newly created and no body has worked on it yet
- Re-open:
	- The issue is coded but the code is rejected when verifying or approving
- In progress:
	- Someone is working on the issue
- Resolved:
	- The issue is coded waiting to be verified
- Closed:
	- The issue is verified, waiting for device team to confirm
- Approved:
	- Device team confirmed new functions

# 3. How to approve new functions
- After checking the new functions, you need to update the state of the issue:
	- If the code is not working or not what you expected:
		- Comment on the issue
		- Move the issue to "Re-open" tab in project dashboard
		- Notify in WhatsApp's group chat
	- If the code is working as you expected:
		- Close the issue
		- Move the issue to "Approved" tab in project dashboard
		- Update the "progress" excel file

# 4. Excel profile form for devices in Phase 2
- https://docs.google.com/spreadsheets/d/1E1TRiQkhVdGuEI7GilPVuSLv6DTn2mGo


# 
---
- Status: #done
- Tags: #z2m
- References:
	- [Source](https://github.com/orgs/ViettelIoTLaboratory/discussions/208)
- Related:
