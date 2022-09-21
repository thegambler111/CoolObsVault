# 
![[01_Experience/Code/JavaScript/JavaScript/Primitive vs Reference Values/slide.png]]

# Primitive values
- Including: Strings, Numbers, Booleans, null, undefined, Symbol
- Assign a variable will assign it with a real value
- Coping a variable (= assign to different variable) will copy the value
- Changing from copied variable will not affect initial variable and vice versa

```js
let name1 = 'Max';
let name2 = name1;

name1 === name2; // true
name1 = 'Anna';

name2; // 'Max'
```


# Reference Values
- Including: Objects (Array is an object, function is also an object)
- Assign a variable will assign it with a pointer (address)
- Coping a variable (= assign to different variable) will copy the pointer
- Changing value of copied variable will also change the value of initial variable and vice versa

```js
let person1 = { age: 30 };
let person2 = person1;
let person3 = { ...person1 };
let person4 = { age: 30 };
const person5 = { age: 30 };

person1.age = 32;
person2.age; // 32
person3.age; // 30

person1 === person4; // false (different pointer)

person5.age = 32; // No error because person5 is a reference and this line only change the value of the age property of the object which variable person5 is referencing
person5 = { age: 32 }; //Error !!! Because this line assign new object to person5 which change the pointer

let hobbies1 = ['Sports'];
let hobbies2 = hobbies1;
let hobbies3 = [...hobbies1];
const hobbies5 = ['Sports'];

hobbies1.push('Cooking');
hobbies2; // ['Sports', 'Cooking']
hobbies3; // ['Sports']

hobbies5.push('Cooking'); // No error because hobbies4 is a reference and push function only change the refered value
hobbies5 = ['Sports', 'Cooking']; //Error !!! Because this line assign new array to hobbies5 which change the pointer
```

# 

---
- Status: #done 

- Tags: #js

- References:
	- [Source](https://www.udemy.com/course/javascript-the-complete-guide-2020-beginner-advanced)

- Related:
	- 
