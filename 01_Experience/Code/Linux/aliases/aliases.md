# alias multiple commands

- A function is a new command that has internal logic. It isn't simply a rename of another command. It does internal operations.
- i.e.
```bash
d() {
    if exists colordiff; then
        colordiff -ur "$@"
    elif exists diff; then
        diff -ur "$@"
    elif exists comm; then
        comm -3 "$1" "$2"
    fi | less
}
```

# 

---
- Status: #done

- Tags: 

- References:
	- [Source](https://stackoverflow.com/questions/756756/multiple-commands-in-an-alias-for-bash/757149#757149)

- Related:
	- 
