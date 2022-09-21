# 
- Fields are attributes defined outside `constructor`, while properties are attributes defined inside `constructor`
- Field $\approx$ properties
```js
class Person {
    name = 'Max'; // This is a field

    constructor() {
        super();
        this.age = 30; // This is a properties
    }

	// This is also a field
	walk = function () {
        console.log('I am walking');
    }

	// This is a function
    greet() {
        console.log(
            'Hi, I am ' + this.name + ' and I am ' + this.age + ' years old.'
        );
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
