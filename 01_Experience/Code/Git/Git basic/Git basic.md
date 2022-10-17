# TL;DR
- Download code from the internet: `git clone`
- Create new remote: `git remote add`
- Create new branch: `git branch`
- Change branch: `git checkout` or `git switch`
- Create a commit: `git add` then `git commit`
- Check commit history: `git log`
- Remove commit: `git reset`
- Update remote repo: `git push`
- Update remote reference: `git fetch`
- Combine 2 branches: `git merge` or `git rebase`
``
# What is Git
- Git is a free and open source distributed version control system
	- It is used to store the development history of any projects
	- You can easily change the state of your project to previous version

# Git components

## Git repository
- A git repository is a place where you store your project's codes
- There are 2 types of repositories
	- Local repository:
		- Project codes on your machine
	- Remote repository:
		- Project codes on external server (Github, Git lab,...)

## Git branch
- Each git branch is a different version of your projects
- Git branches are effectively a pointer to a snapshot of your changes

## Git commit
- Git commit is changes between 2 adjacent snapshots of your project
- All git commits create your project's timeline

# Git flow

## Local repository and remote repository
![[01_Experience/Code/Git/Git basic/git_flow_2.jpg]]
![[01_Experience/Code/Git/Git basic/git_flow_1.jpeg]]

- Working tree is the current state of your files
- Index/staging area is the place where you add file to prepare for a commit
- Local branch is the state of your local repository
- Remote-tracking reference is the copy of remote repository on your local machine
- Remote branch is the state of your remote repository

## Git clone
- Git clone is used to copy codes from remote repository to your local machine to create a local repository
- In Github, there are 3 types of address for remote repository
	- HTTPS
	- SSH
	- GitHub CLI
- Git clone command:

```bash
git clone your_remote_repo_address
```

## Git status
- Git status is used to check the current state of your current working tree
- Git status command:
	- The result contains 3 parts:
		- Your current branch
		- Your local branch state compared to tracking remote branch state
		- Your code state compared to the last commit

```bash
git status
```

## Git remote
- Git branch is used to control your remote repositories

### Git branch commands
- To show all remotes:

```bash
git remote show
```

- To add new remote:

```bash
git remote add new_remote_name new_remote_repo_address
```

- To delete remote:

```bash
git remote remove remote_name
```

- To rename remote:

```bash
git remote rename old_remote_name new_remote_name
```

## Git branch
- Git branch is used to control your repository branch

### Git branch commands
- To show all your branches:

```bash
git branch
```

- To delete a branch:
	- `-d` will not allow you to delete your branch if it has not been merge to its tracking remote branch
	- `-D` = `-d` + `-f`

```bash
git branch -d your_branch_namne
OR
git branch -D your_branch_namne
```

- To create a new branch:

```bash
git branch your_new_branch_name
```

## Git checkout
- Git checkout is used to move between branches

### Git checkout commands
- To move to a specific branch
	- If you checkout a branch not on local but there is a branch with the same name exist on remote, git will create a new branch with the commit history of that remote branch

```bash
git checkout your_branch_name
```

- To create a new branch and move to it:
	- Your new branch will have the same commits history as the branch when you checkout

```bash
git checkout -b your_new_branch_name
```

## Git switch
- Git switch is also used to move between branches

### Git switch commands
- To move to a specific branch:
	- This will not create a new branch in any situation

```bash
git switch your_branch_name
```

- To create a new branch and tell it to track a specific remote branch:

```bash
git switch -c your_new_branch_name your_tracking_remote_branch
```

## Git add
- Git add is used to move your changes from working area to staging area, preparing to commit

### Git add commands
- To add changed files:

```bash
git add file1 file2 file3
```

- To add all changed files:

```bash
git add .
```

- NOTE: To remove staged/added files:

```bash
git restore --stage file1 file2
```

## Git commit
- Git add is used to move your changes from staging area to local branch

### Git commit commands
- To commit all staged changes:

```bash
git commit -m "your_commit_messagee"
```

- To add all staged changes to the last commit:

```bash
git commit --amend -m "your_commit_messagee"
```

- To add all staged changes to the last commit without changing commit message:

```bash
git commit --amend --no-edit
```

## Git log
- Git add is used to view your commit history

### Git commit commands
- To view your commit history:
	- Showed information of each commit:
		- Commit code
		- Author
		- Commit time
		- Commit message

```bash
git log
```

- To view the short version of commit history:
	- Showed information of each commit:
		- Short commit code
		- Commit message

```bash
git log --oneine
```

- To view the short version of commit history with graph showing relation of commits:

```bash
git log --oneine --graph
```

## Git reset
- Git reset is used to undo some commits

### Git reset commands
- To remove commits but keep changes:

```bash
git reset last_kept_commit_code
```

- To remove commits and changes:

```bash
git reset -h last_kept_commit_code
```

## Git push
- Git push is used to move your changes from local repository to remote repository

```bash
git push remote_repo_name local_branch_name:remote_branch_name
```

## Git fetch
- Git fetch is used to update your remote-tracking reference to remote repository

```bash
git fetch remote_repo_name
```

## Git merge
- Git merge is used to combine commits another branch to your current branch

```bash
git merge another_branch_name
```

## Git rebase
- Git rebase is used to:
	- Copy commit history of another branch
	- Check if there are any new commits in the current branch compared to the other branch
	- Add all new commits after the other branch commits

```bash
git rebase another_branch_name
```

# Additional material
- [Learn Git series - Youtube](https://www.youtube.com/playlist?list=PLe6EXFvnTV7-_41SpakZoTIYCgX4aMTdU)
- [Git introduction](https://viblo.asia/p/gioi-thieu-ve-git-aWj53448K6m)

#
---
- Status: #done
- Tags: #git
- References:
- Related:
