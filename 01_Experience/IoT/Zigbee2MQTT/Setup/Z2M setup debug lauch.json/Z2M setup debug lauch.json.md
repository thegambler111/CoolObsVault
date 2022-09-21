# 
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "npm start",
            "request": "launch",
            // Go to zigbee2mqtt fodler
            "cwd": "${workspaceFolder}\\zigbee2mqtt",
            // Choose scripts defined in package.json to run
            "runtimeArgs": [
                "run-script",
                "start"
            ],
            // Show log to VScode console
            "console": "integratedTerminal",
            "runtimeExecutable": "npm",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "type": "node"
        },
        {
            "name": "npm debug",
            "request": "launch",
            "cwd": "${workspaceFolder}\\zigbee2mqtt",
            "runtimeArgs": [
                "run-script",
                "debug"
            ],
            "console": "integratedTerminal",
            "runtimeExecutable": "npm",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "type": "node"
        },
    ]
}
```


# 

---
- Status: #done

- Tags: #vscode #nodejs

- References:
	- [Source](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_launch-configuration-attributes)

- Related:
	- 
