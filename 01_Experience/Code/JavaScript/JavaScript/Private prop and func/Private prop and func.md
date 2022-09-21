# Private properties and functions
- To declare a private properties (attributes) and function, use `#` before it name
- Private properties (attributes) must be declare outside constructor

```js
class Sample {
    #name; // Private props must be initialized outside constructor
    constructor(name) {
        this.#name = name;
    }

    getName() {
        this.#printName();
    }
    #printName() {
        console.log(this.#name);
    }
}

const sample = new Sample('John');
sample.getName(); // => John
sample.#name = 'Jane'; // => Error
sample.#printName(); // => Error
```




# Private setter with public getter in TypeScript
- Normally, setter and getter must be both public or private
- [However, there is a work around](https://stackoverflow.com/questions/27825350/private-setter-typescript/45909300#45909300)



# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
