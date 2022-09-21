# To enable decorator in TS
- To use decorator, you must set `"experimentalDecorators": true` in tsconfig.json
- Decorator is a function that usually start with a capital character
- Decorator run when you define your class, not when you initiate an instance
- **Decorator is used to run some behind the scene code when defining a class or a function, accessor, property, argument**

- TS use returns of decorators for class, function and accessor, not returns of decorators for property, argument
- Class decorator can change the `constructor` of class

```ts

function WithTemplate(template: string, hookId: string) {
  console.log('TEMPLATE FACTORY');
  return function<T extends { new (...args: any[]): { name: string } }>(
    originalConstructor: T
  ) {
    return class extends originalConstructor {
      constructor(..._: any[]) {
        super();
        console.log('Rendering template');
        const hookEl = document.getElementById(hookId);
        if (hookEl) {
          hookEl.innerHTML = template;
          hookEl.querySelector('h1')!.textContent = this.name;
        }
      }
    };
  };
}

@WithTemplate('<h1>My Person Object</h1>', 'app')
class Person {
  name = 'Max';

  constructor() {
    console.log('Creating person object...');
  }
}

const pers = new Person(); 
// Whenever an instance of the class is created, the new constructor inside decorator WithTemplate is used

console.log(pers);
```


- Function and accessor decorator can change function through the `PropertyDescriptor` (configurable,  enumerable, value, writable)
```ts
function Autobind(_: any, _2: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  const adjDescriptor: PropertyDescriptor = {
    configurable: true,
    enumerable: false,
    get() {
      const boundFn = originalMethod.bind(this); // Add bind(this)
      return boundFn; // Return modified method
    }
  };
  return adjDescriptor;
}

class Printer {
  message = 'This works!';

  @Autobind // This decorator change PropertyDescriptor of func showMessage
  showMessage() {
    console.log(this.message);
  }
}

const p = new Printer();
p.showMessage();

const button = document.querySelector('button')!;
button.addEventListener('click', p.showMessage);
```




# 

---
- Status: #done

- Tags: #js

- References:
	- 

- Related:
	- 
