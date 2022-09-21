# splice

```js
hobbies = ['Coding', 'Sports', 'Cooking', 'Reading'];
console.log(hobbies);
const removedItems = hobbies.splice(1, 2, 'Money', 'Gaming', 'Sleeping'); // start ay index 1, remove 2 elements, add 3 elements 'Money', 'Gaming', 'Sleeping' from index 1, move the rest of the elements to the right of the added elements
// => ['Coding', 'Money', 'Gaming', 'Sleeping', 'Reading']
console.log(hobbies);
```

# indexOf
```js 
testResults = [1, 5.3, 1.5, 10.99, 1.5, -5, 10];
testResults.indexOf(1.5); // return index of element in array, return -1 if not found
```

# find
```js
const personData = [{ name: 'Max' }, { name: 'Manuel' }];
const manuel = personData.find((person, idx, persons) => {
  return person.name === 'Manuel';
}); // => { name: 'Manuel' }
```


# findIndex
```js
const personData = [{ name: 'Max' }, { name: 'Manuel' }];
const maxIndex = personData.findIndex((person, idx, persons) => {
  return person.name === 'Max';
}); // => 0
```

# forEach
```js
const prices = [10.99, 5.99, 3.99, 6.59];
const tax = 0.19;
const taxAdjustedPrices = [];
prices.forEach((price, idx, prices) => {
    const priceObj = { index: idx, taxAdjPrice: price * (1 + tax) };
    taxAdjustedPrices.push(priceObj);
}); // Do not need to return inside forEach
// => taxAdjustedPrices = [{ index: 0, taxAdjPrice: 12.18 }, { index: 1, taxAdjPrice: 6.99 }, { index: 2, taxAdjPrice: 4.19 }, { index: 3, taxAdjPrice: 7.39 }]
```

# map
```js
const prices = [10.99, 5.99, 3.99, 6.59];
const tax = 0.19;
const taxAdjustedPrices = [];
taxAdjustedPrices = prices.map((price, idx, prices) => {
    const priceObj = { index: idx, taxAdjPrice: price * (1 + tax) };
    return priceObj; // Need return inside map
});
// => taxAdjustedPrices = [{ index: 0, taxAdjPrice: 12.18 }, { index: 1, taxAdjPrice: 6.99 }, { index: 2, taxAdjPrice: 4.19 }, { index: 3, taxAdjPrice: 7.39 }]
```

# sort
```js
const prices = [10.99, 5.99, 3.99, 6.59];
const sortedPrices = prices.sort((a, b) => {
    if (a > b) {
        return 1;
    } else if (a === b) {
        return 0;
    } else {
        return -1;
    }
});// => [3.99, 5.99, 6.59, 10.99]
```

# filter
```js
const prices = [10.99, 5.99, 3.99, 6.59];
const filteredArray = prices.filter((p, idx, prices) => {
    return p > 6;
}); // => [10.99, 6.59]
```


# reduce
```js
const prices = [10.99, 5.99, 3.99, 6.59];
const sum = prices.reduce((prevValue, curValue, curIndex, prices) => {
  return prevValue + curValue; // return the value of next prevValue
}, 0); // 0 is the initial value of prevValue
// => 31.98
```

# Array de-structuring
```js
const nameData = ['Max', 'Schwarz', 'Mr', 30];
const [firstName1, lastName1] = nameData; // => firstName1 = 'Max', lastName1 = 'Schwarz'
const [firstName, lastName, ...otherInfo] = nameData; // => firstName = 'Max', lastName = 'Schwarz', otherInfo = ['Mr', 30]
```



# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
