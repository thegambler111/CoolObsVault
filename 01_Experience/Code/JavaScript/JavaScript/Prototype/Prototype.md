# Prototype
- Prototype `P` of an Object `O` acts as "fallback object" of Object `O`
	- When calling a function or property from `O`, if `O` does not have that function or property, JavaScript will try to find said function or property in prototype of `O` (which is `P`)
		- If `P` does not have that function or property, JavaScript will try to find in prototype of `P` and so on until the last prototype (which is `Object.prototype`)

```js
class AgedPerson{
...
}

class Person extends AgedPerson {
...
}

const p = new Person();
p.__proto__ == Person.prototype // => true
Person.__proto__ == AgedPerson // => true
```

- Any function (not function defined using field) of the object will be inside of its prototype
	- Therefore, function will be created only once for the class, not for each instance of that class
	- On the other hand, function defined using field will be created for each instance of that class
```js
class Person {
	printName(){ // This will be inside prototype
	...
	}

    walk = function () { // This will not be inside prototype
    ...
    }
...
}

const p = new Person(); // function printName() will be inside p.__proto__
```


- Prototype of 2 object from the same class are the same
```js
class Person {
...
}

const p = new Person();
const p2 = new Person();
p.__proto__ == p2.__proto__ // => true
```



# Super
![[01_Experience/Code/JavaScript/JavaScript/super/super#Prototype super]]


# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
