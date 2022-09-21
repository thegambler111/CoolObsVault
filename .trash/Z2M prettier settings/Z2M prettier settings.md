# Change in settings.json
- Download extensions:
	- Eslint
	- Prettier
	- Prettier Eslint

- Open settings.json
	- Ctrl+Shift+P:
	- Search "Preferences: Open Settings (JSON)"

```json
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

# Reference
- [[01_Experience/Code/VSCode/VSCode settings and extensions/VSCode settings and extensions]]


# 

---
- Status: #done

- Tags: #z2m

- References:
	- 

- Related:
	- 
