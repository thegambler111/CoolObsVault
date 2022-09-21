# 
```js
const userName = 'Max';

const altName = '';

console.log(!!userName); // use 2 operator '!' transform falsy to false and truthy to true => true

console.log(userName === 'Max'); // generates and prints a boolean => true

console.log(userName); // wasn't touched, still is a string => 'Max'


console.log(userName || null); // userName is truthy and therefore returned by || => 'Max'

console.log(altName || 'Max'); // altName is falsy (empty string), hence 'Max' is returned => 'Max'

console.log(altName || ''); // both altName and '' are falsy but if the first operand is falsy, the second one is always returned => ''

console.log(altName || null || 'Anna'); // altName and null are falsy, 'Anna' is returned => 'Anna'


console.log(userName && 'Anna'); // userName is truthy, hence second (!) value is returned => 'Anna'

console.log(altName && 'Anna'); // altName is falsy, hence first value is returned => ''

console.log(userName && ''); // userName is truthy, hence second value is returned => '


const enteredValue = ''; // let's assume this is set based on some input provided by the user, therefore it might be an empty string

const userNamex = enteredValue || 'PLACEHOLDER'; // will assign 'PLACEHOLDER' if enteredValue is an empty string

```


# 

---
- Status: #done 

- Tags: #js

- References:
	- [Source](https://www.udemy.com/course/javascript-the-complete-guide-2020-beginner-advanced)

- Related:
	- 
