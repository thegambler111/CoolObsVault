# 
- You can use optional `?` arguments to change to required arguments when overloading
```ts
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: number, b: string): string;
function add(a: string, b: number): string;
function add(a: Combinable, b: Combinable) {
    if (typeof a === 'string' || typeof b === 'string') {
        return a.toString() + b.toString();
    }
    return a + b;
}

const a = add('a', 2);
const b = add(1, 'b');
const c = add(1, 2);
```

# 

---
- Status: #done

- Tags: #js

- References:
	- 

- Related:
	- 
