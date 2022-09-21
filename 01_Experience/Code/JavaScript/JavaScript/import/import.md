# 
- You can only import what you export using `export` keyword



# default
- You can use `default` keyword to tell which function or class is default exported
- Name of default class or function will not be recognized well importing
- When importing, you need to specify a name for default export

```js
// Component.js
export function doSomething() {};

export default class someClass{}; // The name `someClass` is ignore because of `default`
```

```js
import { someClass, doSomething } from './Component.js';
// => Error: someClass is not defined
// The name `someClass` is ignore because of `default`
```

```js
import Cmp, { doSomething } from './Component.js';
// `Cmp` represent default export from './Component.js' which is `someClass`
```

# Import as a bundle
- You can import everything exported from a file using alias

```js
// Component.js
export function doSomething() {};

export class someClass{}; // The name `someClass` is ignore because of `default`
```

```js
import * as Cmp from './Component.js';

Cmp.doSomething();
new Cmp.someClass();
```

# Dynamic import
- You can also import module inside function

```js
// Component.js
export function doSomething() {};

export default class someClass{}; // The name `someClass` is ignore because of `default`
```

```js
function doOtherThing(){
	import('./Component.js').then(module => {
      const someC = new module.someClass();
      module.doSomething();
    });
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
