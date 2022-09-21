# Aliases in Windows
## Add alias folder to Windows
1.  Create a folder called `C:\Aliases`
2.  Add `C:\Aliases` to your path (so any files in it will be found every time)
3.  Create `a.bat` file in `C:\Aliases` for each of the aliases you want

- [Source aliases](https://stackoverflow.com/questions/20530996/aliases-in-windows-command-prompt/39459404#39459404)

- Suggested `.bat` content:
```bash
@echo off
echo.
command %*
```
### Using `%` to get inputs
- Use `%*` to accept all inputs
- Use `%1` to accept the first input
- Example: a.bat file
```bash
scp -r labiot@192.168.68.%1:/opt/zigbee2mqtt/%2 .\Desktop\%3
```
- Running command `a 4 "" test` = `scp -r labiot@192.168.68.4:/opt/zigbee2mqtt/ .\Desktop\test`
	- => copy folder `/opt/zigbee2mqtt/` to `.\Desktop\test`


### Using `call` to call multiple command in the same `.bat` file
- [Source call](https://stackoverflow.com/questions/34922908/how-to-run-multiple-commands-in-a-batch-file/34923034#34923034)
- Example: if you have `a.bat`, `b.bat` and `c.bat`, your `callall.bat` file

```bash
call a
call b
call c
```



## ssh-copy-id in Windows

```bash
type %USERPROFILE%\.ssh\id_rsa.pub | ssh %1 "test -d .ssh || mkdir .ssh && cat >> .ssh/authorized_keys"
```


# 

---
- Status: #done

- Tags: #windows

- References:
	- [Source aliases](https://stackoverflow.com/questions/20530996/aliases-in-windows-command-prompt/39459404#39459404)
	- [Source 1 ssh-copy-id](https://serverfault.com/questions/224810/is-there-an-equivalent-to-ssh-copy-id-for-windows/224851#224851)
	- [Source 2 ssh-copy-id](https://www.chrisjhart.com/Windows-10-ssh-copy-id/)
	- [Source call](https://stackoverflow.com/questions/34922908/how-to-run-multiple-commands-in-a-batch-file/34923034#34923034)

- Related:
	- 
