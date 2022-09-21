# 
- Symbol creates an unique symbol that has very limited way to access
- Symbol is used to limit the ability to change some values

```js
const uid = Symbol(); // Create a brand new Symbol
console.log(uid); // Symbol()

const user = {
    [uid]: 'p1', // key = Symbol()
    name: 'Max',
    age: 30
};
// age: 30
// name: "Max"
// Symbol(): "p3"

user[uid] = 'p2'; // Correct way to change uid
user.uid = 'p3'; // Cannot change uid because there is no 'uid' key in user


console.log(user[Symbol()]); // undefined
console.log(Symbol() === Symbol()); // false

```



# 

---
- Status: #done

- Tags: #js

- References:
	- 

- Related:
	- 
