# Setup

- [Download](https://cli.github.com/)
- Login using Github account: `gh auth login`
	- What account do you want to log into?
		- Choose `GitHub.com`
	- What is your preferred protocol for Git operations?
		- Choose `HTTPS`
	- Authenticate Git with your GitHub credentials?
		- Type `Y`
	- How would you like to authenticate GitHub CLI?
		- Choose `Login with a web browser`
	- Copy your code
		- The code look something like this: 25DA-2CC2
	- Press `Enter` to open Github on Web
		- Paste your code to the tab that is just opened then click `Continue`
	- Click `Authorize github`
	- Done

# Show Oraganization's repo list

```bash
**gh repo list organization_name
```


# Delete default gh repo

- Open `.git/config file`
- Remove line` gh-resolved = base`
- Save the file and close


# Export issue of a repo
- Open Windows PowerShell
	- Do not use Command line because it will not store Vietnamese
	- [Utf 8 in commandl ine](https://stackoverflow.com/a/65641304)
- Go to the folder of git repo
	- i.e. zigbee-herdsman-converters
- Type:
```bash
gh issue list --state all -m mile_stone_name_or_number -R repo_name > file_name.csv
```
- Example for Zigbee-herdsman-converters
```bash
gh issue list --state all -m 2 -R ViettelIoTLaboratory/zigbee-herdsman-converters > file_name.csv
```

- [Source 1](https://cli.github.com/manual/gh_issue_list)
- [Source 2](https://stackoverflow.com/questions/41369365/how-can-i-export-github-issues-to-excel)








# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
