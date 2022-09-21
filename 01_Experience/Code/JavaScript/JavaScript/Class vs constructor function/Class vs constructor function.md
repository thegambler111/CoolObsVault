# Class vs constructor function
- Defining a class is somewhat similar to defining a constructor function
| Constructor functions                     | Classes                               |
| ----------------------------------------- | ------------------------------------- |
| Blueprint for object                      | Blueprint for object                  |
| Properties and Methods                    | Properties and Methods                |
| Can be called with 'new'                  | Must be called with 'new'             |
| All properties and methods are enumerable | Methods are non-enumerable by default | 
| Not in strict mode by default             | Always in strict mode                 |

- In the example below, class Person $\approx$ function Person

```js
class Person {
    name = 'Max';

    constructor() {
        super();
        this.age = 30;
    }

    greet() {
        console.log(
            'Hi, I am ' + this.name + ' and I am ' + this.age + ' years old.'
        );
    }
}

function Person() {
    this.age = 30;
    this.name = 'Max';
    this.greet = function () {
        console.log(
            'Hi, I am ' + this.name + ' and I am ' + this.age + ' years old.'
        );
    };
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
