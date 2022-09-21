# Field define
- Any field defined in an Object will act after `super()`
```js
class AgedPerson{
...
}

class Person extends AgedPerson {
	name = 'John'; // This will get execute after super() in constructor
	constructor() {
        super();
        this.age = 30;
        ...
    }
}
```



# Prototype super()
- `super()` creates an object based on extended class and then sets it as prototype of the object built based on this class

```js
class AgedPerson{
...
}

class Person extends AgedPerson {
	constructor() {
        super();
        ...
    }
}
```






# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
