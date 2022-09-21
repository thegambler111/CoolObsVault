# Sync with remote server using extension "SFTP"
- Search and install "SFTP" extension by Natizyskunk
- Open SFTP config
- Use example below:
```json
{
    "name": "My Server",
    "host": "192.168.68.4", // Change
    "protocol": "sftp",
    "port": 22,
    "username": "labiot", // Change
    "remotePath": "/opt/zigbee2mqtt", // Change
    "privateKeyPath": "C:\\Users\\HP\\.ssh\\id_rsa",  // If you have set ssh key, use this, otherwise use password field in the guide
    "uploadOnSave": true,
    "useTempFile": false,
    "openSsh": true,
    "ignore": [".vscode", ".github", "node_modules", ".git"] // Change
}

```


# 

---
- Status: #done

- Tags: #vscode 

- References:
	- [Source](https://stackoverflow.com/questions/66569829/does-visual-studio-code-support-code-sync-with-remote-server)
	- [Github](https://github.com/Natizyskunk/vscode-sftp)

- Related:
	- 
