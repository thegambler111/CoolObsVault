# Class interface
- A class can inherit (`extends`) only 1 class but can `implements` multiple interfaces

```ts
interface Named {
    name: string;
    outputName?: string;
}

interface Greetable extends Named {
    greet(phrase: string): void;
}

interface Aged {
    age: number;
}

class Person implements Greetable, Aged {
    name: string;
    age: number;

    constructor(n: string, a: number) {
        this.name = n;
        this.age = a;
    }

    greet(phrase: string) {
        console.log(phrase + ' ' + this.name);
    }
}
```



# Function interface

```ts
interface AddFn {
    (a: number, b: number): number;
}

let add: AddFn;

add = (n1: number, n2: number) => {
    return n1 + n2;
};
```

# Optional properties and methods

- By adding `?` after properties name, you make the properties optional
- You can also create optional methods by adding `?` after methods name

```ts
interface Named {
    name?: string;
    outputName?: string;
}

interface Greetable extends Named {
    greet(phrase: string): void;
}

interface Aged {
    age: number;
}

class Person implements Greetable, Aged {
    name?: string;
    age: number;

    constructor(n?: string) {
        if (n) {
            this.name = n;
        }
        this.age = 30;
    }

    greet(phrase: string) {
        if (this.name) {
            console.log(phrase + ' ' + this.name);
        } else {
            console.log('Hi!');
        }
    }
}

let user3 = new Person();
```





# 

---
- Status: #done

- Tags: #js

- References:
	- 

- Related:
	- 
