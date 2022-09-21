# 1. How to use Github Project dashboard

## 1.1. Overview
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to use Github Project dashboard/Github project dashboard.png]]

- [Link to project dashboard in the image](https://github.com/orgs/ViettelIoTLaboratory/projects/1/views/3)
- On top is the project name: Phase 1: New device support
- Under project name is view tabs. There are 2 types of views:
	- Table: Like excel
	- Board: Like the image above
- Content of all views is the projects issues
- Click the triangle under view tab to open search box

## 1.2. Board view
- The image above will take effect in Phase 1 (first 100 device types) and used by Gateway team
- There are 5 columns which are 5 states of an issue:
	- *Request*: When the issue is created by device team
	- *Re-open*: When an issue is resolved but then rejected by either gateway team lead or device team
	- *In progress*: When a Gateway team member is taking care of an issue
	- *Resolved*: When the issue is solved, waiting for the review of team lead
	- *Closed*: When team lead approved the new code and updated the code to test environment (2 test gateways at HNI and HCM)
	- *Device team approved*: When developed feature satisfy device team

## 1.3. Create graph
- On top right, there is a button to create graph
- Self-explore :D

## 1.4. Default workflows
- Click *Three dots button* on top right then choose *Workflows*
- Modify these workflows to change default flow of the issues
- [Create custom workflow using Github actions](https://docs.github.com/en/actions/quickstart)


# 2. How to create new Github issue
- Open new issue:
	- Manual:
		- Go to `Issue` tab in `zigbee-herdsman-converters`: [Issue tab](https://github.com/ViettelIoTLaboratory/zigbee-herdsman-converters/issues)
		- Click button *New Issue* on top right
		- Click *Open a blank issue.*
	- [Direct link](https://github.com/ViettelIoTLaboratory/zigbee-herdsman-converters/issues/new)
- Fill in *Title* and *Content*
- On right column:
	- Assignees: Leave blank
	- Labels: *New device support request*
	- Projects: *Phase 1: New device support*
	- Milestone: *Phase 1 - 2022*
- Press *Submit new issue*



# 3. When to change state of a task

- When a gateway team member take a task:
	- Open the task, change assignee to your name
	- Move the task from *Request* or *Re-open* to *In progress* column
- When a gateway team member finished a task:
	- Create a pull request and add the link to comment of the task
	- Move the task to *Solved* column
- Gateway team lead checked and verified the code:
	- If there are any problems, move the task to *Re-open* column
	- If not, move the task to *Closed*
		- Update task on [excel file](https://docs.google.com/spreadsheets/d/1oWEILMFegl2e3MyBsZe2oohcmRNCRdro/edit)
- Device team checked and verified the code:
	- If there are any problems, move the task to *Re-open* column
	- If not, move the task to *Device team approved*





#

---
- Status: #done

- Tags: #github

- References:
	- 

- Related:
	- 
