# How to name a branch

## Structure of a branch name:
```
{Branch_type}/{Owner_email}-{Function}
```

 - E.g. `feature/thangnt30-list-file-detail-task`

## Type of branches
- Feature
	- E.g. `feature/thangnt30-list-file-detail-task`
- Fix
	- E.g. `fix/thangnt30-list-file-detail-task`
- Hotfix
	- E.g. `hotfix/thangnt30-list-file-detail-task`

# How to name a commit

## Structure of a commit name
```
[{Jira id}][{Feature}] {Task details}
```

 - E.g. `[NBOX-431][Documentary] due date sign flow`

## Detailed
- `{Jira id}` is project name + task id in Jira 
	- This field is required
	- Create corresponding task in Jira if have not done it
- `{Feature}` is:
	- Feature which the task belong to
		- E.g. `User info`
	- Or type of general task
		- E.g. `Documentary`
- `{Task details}` is all details of tasks solved by the commit
	- If a commit solved multiple tasks then separates the tasks using `&`
		- E.g. `[NBOX-431][Webview] Fix redirect & loading webview`

#
---
- Status: #done
- Tags: #git
- References:
	- [Source](http://wiki.nbox.viettel.vn/en/nbox-kt)
- Related:
