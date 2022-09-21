# 
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
	    // Add a config here if you want to auto open terminal when start debugging
        {
            "command": "npm start",
            "name": "Run npm start",
            "request": "launch",
            "type": "node-terminal"
        },
        {
            "command": "npm run herdsman",
            "name": "Run npm run herdsman",
            "request": "launch",
            "type": "node-terminal"
        },
        {
            "type": "pwa-node",
            "request": "launch",
            "name": "Launch Program",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}\\index.js",
            "outFiles": [
                "${workspaceFolder}/**/*.js"
            ]
        }
    ]
}
```


# 

---
- Status: #done

- Tags: #vscode 

- References:
	- 

- Related:
	- 
