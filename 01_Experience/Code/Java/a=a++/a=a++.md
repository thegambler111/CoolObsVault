# What happens when `a=a++`
```java
int a = 0;
a = a++;
```

- First function `a++` executes:
	- `a` value is increase by 1 -> value of `a` is changed to `1`
	- Then return the value of initial `a` which is `0`
- Then function `a=` executes:
	- Before being assigned, value of `a` is `1`
	- `a` is assigned to returned value of function `a++` which is `0`
- So the final value of `a` is `0`

#
---
- Status: #done
- Tags: #java
- References:
	- [Source](https://stackoverflow.com/a/5098354)
- Related:
