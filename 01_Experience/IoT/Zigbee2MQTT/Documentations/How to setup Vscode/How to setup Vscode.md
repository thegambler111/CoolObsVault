# Setup prettier

## Change in settings.json
- Download extensions:
	- Eslint
	- Prettier
	- Prettier Eslint
- Open settings.json
	- Ctrl+Shift+P:
	- Search "Preferences: Open Settings (JSON)"

```json
    "files.autoSave": "onFocusChange",
    "files.eol": "\n",
    "prettier.tabWidth": 4,
    "editor.autoClosingBrackets": "always",
    "editor.autoClosingDelete": "always",
    "editor.formatOnSave": true,
    "prettier.singleQuote": true,
    "prettier.printWidth": 120,
    "prettier.trailingComma": "all",
    "prettier.bracketSpacing": false,
    "[json]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "eslint.validate": ["javascript", "typescript"],
    "eslint.alwaysShowStatus": true,
    "eslint.lintTask.enable": true,
    "[typescript]": {
        "editor.defaultFormatter": "rvest.vs-code-prettier-eslint"
    },
    "[javascript]": {
        "editor.defaultFormatter": "rvest.vs-code-prettier-eslint"
    },
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": true
    },
```

## Reference
- [[01_Experience/Code/VSCode/VSCode settings and extensions/VSCode settings and extensions]]

# Link modules
- In any folder, before running any `npm link` command, run `npm ci` to download external libraries if you have not run it before
![[01_Experience/Code/JavaScript/TypeScript/npm link_Debug Typescript module in node_modules/npm link_Debug Typescript module in node_modules#Using npm link for Zigbee2mqtt]]
- After linking, run `npm run build` in `zigbee-herdsman`, `zigbee2mqtt-frontend` then in `zigbee2mqtt`


# Use Vscode as git message editor
![[01_Experience/Code/Git/Set Vscode as default git message editor/Set Vscode as default git message editor#Set Vscode as default git message editor]]

#
---
- Status: #done
- Tags: #z2m
- References:
- Related:
