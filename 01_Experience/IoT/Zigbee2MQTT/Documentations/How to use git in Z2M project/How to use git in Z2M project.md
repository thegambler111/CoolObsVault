# How to make a commit
- Change your code
- **Check all changes before committing**
- Commit:
	- Add changes to your commit:
		- Add changed files to your commit:
			- `git add changed_file_name_1 changed_file_name_2 changed_file_name_n`
		- OR add all changed files to your commit:
			- `git add .`
	- Create a commit:
		- `git commit -m "your_commit_message"`

## How to make a commit message

### When add new device definition
- Commit message will be in this form:
	- ":add: device_number device_short_name device_name"
		- "device_number" and "device_short_name" from device team
		- "device_name" can be from device team or from you
	- i.e. ":add: 3.5 SAE Aqara US plug"
		- device_number = "3.5"
		- device_short_name = "SAE"
		- device_name = "Aqara US plug"

### When modify a device definition
- Commit message will be in this form:
	- ":mod: device_number device_short_name device_name"

### Other
- Please ask your repository manager
	- Don't ask Mr.Cong :D



# What to do before pushing a change
- Fetch from lab repository (should be "origin", if not "origin",  change "origin" with correct remote):
	- `git fetch origin`
- Create a backup branch:
	- `git branch your_backup_branch_name`
- For `converters`, rebase with branch "phase1" in lab repository ("origin"):
	- `git rebase origin/phase1`
	- **If there are any conflicts, ask for help :)**
	- For `z2m` and `herdsman`, ask for branch to rebase 
- Push your commit to your branch on lab repository
	- `git push origin your_branch_name`
- If you know how to create a merge request, please create one :)
	- Merge request should contains only 1 commit (to reduce conflicts)
	- Merge request must be compatible with (mergeable to) destination branch
	- Remember to change destination of your merge request:
		- From: Your_branch
		- To: "phase1"

 🎼🎵🎙

# How to update your code to latest version (only if you do not create new code -> device team)
- NOTE: Usually, you only need to update `zigbee-herdsman-converters`

- In each folder:
	- Fetch new code (replace origin if lab repository is different repository):
		- `git fetch origin`
		- If nothing shows up in command line -> No new changes -> No need to update
	- Remove all changes (WARNING: this will remove anything that has not been committed):
		- `git reset --hard HEAD`
	- Checkout to default branch:
		- In `zigbee-herdsman-converters`:
			- `git checkout master`
		- In `zigbee-herdsman` or `zigbee2mqtt`:
			- `git checkout develop`
	- Delete branch code:
		- In `zigbee-herdsman`:
			- `git branch -D haint126`
		- In `zigbee-herdsman-converters`:
			- `git branch -D phase1`
		- In `zigbee2mqtt`:
			- `git branch -D develop`
	- Get new code:
		- In `zigbee-herdsman`:
			- `git switch -c haint126 origin/haint126`
		- In `zigbee-herdsman-converters`:
			- `git switch -c phase1 origin/phase1`
		- In `zigbee2mqtt`:
			- `git switch -c develop origin/develop`
	- If you get new code in `zigbee-herdsman` or `zigbee2mqtt`, you will need to rebuild:
		- `npm run build`
		- You do not need to build in folder `zigbee-herdsman-converters`
	- Done


# References
- [Official Git Documentation](https://git-scm.com/doc)




# 

---
- Status: #done

- Tags: #z2m #git 

- References:
	- 

- Related:
	- 
