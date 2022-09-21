# `this`
- `this` refers to which trigger the function (the thing in front of your function execution), unless `this` is defined when function is called

```js
const person = {
	name: "Hai",
	getUpperName() {
		return this.name.toUpperCase();
	}
}
person.getUpperName(); // this = person

let { getUpperName } = person
getUpperName(); // this = global context ('Window' object in web browser)
// => Error
```

- When a function is bind to an `eventListener`,  `this` inside that function is referred to the DOM element that trigger the event (like a button)
- For function created using `=>`, `this` inside the function is the same as `this` outside the function (where you can write code???)
```js
this // outside function `this` (where you can write code???)
// this out here will be `window`
const person = {
	name: "Hai",
	getUpperName: () => {
		return this.name.toUpperCase(); // `this` here is the same as outside function `this`
	}
}
person.getUpperName(); // => Error

let { getUpperName } = person
getUpperName(); // => Error
```


# Define `this`
- Using `bind()`

```js
const person = {
	name: "Hai",
	getUpperName() {
		return this.name.toUpperCase();
	}
}

let { getUpperName } = person
getUpperName = getUpperName.bind(person); // In all call after here, `this` = person
getUpperName(); // this = person
```

- Using `call()` or `apply()` (somewhat similar)
```js
const person = {
	name: "Hai",
	getUpperName() {
		return this.name.toUpperCase();
	}
}

let { getUpperName } = person
getUpperName.call(person); // In this specific call, `this` = person
```


# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
