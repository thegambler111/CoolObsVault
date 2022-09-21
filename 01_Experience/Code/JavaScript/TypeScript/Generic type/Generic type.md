# 
- Generic type is flexible yet strongly typed (type safety)
- What exactly generic type refers to (whether `string` or `numeber` or something) is determined when variable is defined or function is called or class object is initiate

```ts
function merge<T extends object, U extends object>(objA: T, objB: U) {
    return Object.assign(objA, objB);
}

const mergedObj = merge({ name: 'Max', hobbies: ['Sports'] }, { age: 30 });
// what type `T` and `U` refer to is detemined here when calling the function
console.log(mergedObj);

interface Lengthy {
    length: number;
}
```

```ts
interface Lengthy {
    length: number;
}

function countAndDescribe<T extends Lengthy>(element: T): [T, string] {
// T can be any kind of type as long as it has property `length` as a number
    let descriptionText = 'Got no value.';
    if (element.length === 1) {
        descriptionText = 'Got 1 element.';
    } else if (element.length > 1) {
        descriptionText = 'Got ' + element.length + ' elements.';
    }
    return [element, descriptionText];
}

console.log(countAndDescribe(['Sports', 'Cooking']));
```

- You can use `extends` to limit the type which generic type refers to

```ts
class DataStorage<T extends string | number | boolean> {
// T can only be either string or number or boolean
// => all items in 1 instance of DataStorage can belong to only 1 type, either string or number or boolean
    private data: T[] = [];

    addItem(item: T) {
        this.data.push(item);
    }

    removeItem(item: T) {
        if (this.data.indexOf(item) === -1) {
            return;
        }
        this.data.splice(this.data.indexOf(item), 1); // -1
    }

    getItems() {
        return [...this.data];
    }
}

const textStorage = new DataStorage<string>(); // `T` is defined here as `string`
textStorage.addItem('Max');
textStorage.addItem('Manu');
textStorage.removeItem('Max');
console.log(textStorage.getItems());

const numberStorage = new DataStorage<number>(); // `T` is defined here as `number`
```

- You can use `keyof` to tell that some type is key of a generic type
```ts
function extractAndConvert<T extends object, U extends keyof T>(obj: T, key: U) {
// Object type `T` has a key `U`
    return 'Value: ' + obj[key];
}

extractAndConvert({ name: 'Max' }, 'name');
```









# 

---
- Status: #done

- Tags: #js

- References:
	- 

- Related:
	- 
