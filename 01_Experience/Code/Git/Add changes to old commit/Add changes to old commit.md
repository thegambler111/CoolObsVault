# 
- where `OLDCOMMIT` is something like `091b73a`

```
git add <my fixed files>
git commit --fixup=OLDCOMMIT
git rebase --interactive --autosquash OLDCOMMIT^
```


# 

---
- Status: #done

- Tags: #git 

- References:
	- [Source](https://stackoverflow.com/a/27721031)

- Related:
	- 
