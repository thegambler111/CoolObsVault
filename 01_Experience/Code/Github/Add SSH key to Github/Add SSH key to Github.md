# Why?
- To use Github without logging in
- Interact with private repos

# Generate ssh key for your machine
- Generate ssh key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

- After executing above command, you will be prompted to "Enter a file in which to save the key" like this:
	- If you don't want to change the file location, just press enter
	- **Remember this location to add to ssh-agent**
	- NOTE: This will replace old ssh key if the locations are the same

```shell
> Enter a file in which to save the key (/home/YOU/.ssh/ALGORITHM):[Press enter]
```

- Then, you will be prompt to enter a secure passphrase
	- Press enter to leave the secure passphrase empty

```shell
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

# Add your ssh key to ssh-agent
- Start the ssh-agent in the background

```shell
eval "$(ssh-agent -s)"
```

- Example result:

```shell
> Agent pid 59566
```

- Add your SSH private key to the ssh-agent (default in Linux: `~/.ssh/id_ed25519`)

```shell
ssh-add "location_of_your_key_file"
```

# Add ssh key to you Github
- Open your key file and copy the key
	- You can print the key to terminal and copy from there using this command

```shell
cat "location_of_your_key_file"
```

- In the upper-right corner of any Github page, click your profile photo, then click Settings.
- In the "Access" section of the sidebar, click SSH and GPG keys.
- Click New SSH key or Add SSH key.
- Enter key name in "Title" field
- Paste your key into "Key" field
- Click Add SSH key.

#
---
- Status: #done
- Tags: #github
- References:
	- [Generate ssh key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
	- [Add ssh key to Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)
- Related:
