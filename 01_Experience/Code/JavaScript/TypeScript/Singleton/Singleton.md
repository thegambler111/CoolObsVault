# 
- Singleton can be created using `private` and `static`

```ts
class DummyClass {
    private static instance: AccountingDepartment;

    private constructor() {}

    static getInstance() {
        if (DummyClass.instance) {
            return this.instance;
        } else {
            this.instance = new DummyClass();
            return this.instance;
        }
    }
}

const dummy1 = DummyClass.getInstance():
const dummy2 = DummyClass.getInstance():
console.log(dummy1 === dummy2); // true

```




# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
