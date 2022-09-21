# 
- `bind()` create and return a new function object
	- `printResult.bind(...) !== printResult`

```js
const printResult = (message, result) => {
    console.log(`${message} ${result}`);
};

const getSum = (printResultCallback, ...numbers) => {
    let sum = 0;
    for (const num of numbers) {
        sum += num;
    }
    printResultCallback(sum);
};

getSum(printResult.bind(this, 'The sum is'), 1, 2, 3, 4, 5); // The args from bind is always start at the begining of the function args. In this case, 'the sum is' = messageText
// => The sum is 15
```


# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
