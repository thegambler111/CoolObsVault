# "Visual Studio Code is unable to watch for file changes in this large workspace" (error ENOSPC)
- [Source](https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc)
- When you see this notification, it indicates that the VS Code file watcher is running out of handles because the workspace is large and contains many files
- 2 ways to handle

## Remove potential large folder
- Before adjusting platform limits, make sure that potentially large folders, such as Python `.venv`, are added to the `files.watcherExclude` setting
- The default for `files.watcherExclude` excludes `node_modules` and some folders under `.git`
- Example:

```json
"files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/*/**": true
  }
```

## Increase VSCode limit
- Check the current file watcher limit

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

- Increase limit by editing `/etc/sysctl.conf` (except on Arch Linux) and adding this line to the end of the file:

```Shell
fs.inotify.max_user_watches=524288
```

- The new value can then be loaded in by running 

```shell
sudo sysctl -p
```

#
---
- Status: #done
- Tags: #vscode
- References:
- Related:
