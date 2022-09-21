# Promise
- `Promise` is used to avoid nested callback
- Everything inside `Promise` will be pushed to event loop and handled by browser
- All function after `Promise` will be executed by JavaScript => Not be blocked by `Promise`
```js
const promise = new Promise((resolve, reject) => {
	callback1(
		(resolveData) =>{
			resolve(resolveData);
		},
		(rejectData) =>{ // Usually rejectData = errorMessage
			reject(rejectData);
		},
		options
	);
```
- `then()` happens in sequence, any events in previous `then()` must be finished before the next `then()`

```js
const button = document.querySelector('button');

const getPosition = (opts) => {
    console.log('step0');
    const promise = new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            (success) => {
                console.log('step6');
                resolve(success);
            },
            (error) => {
                console.log('step6.5');
                reject(error);
            },
            opts
        );
    });
    console.log('step1');
    return promise;
};

const setTimer = (duration) => {
    console.log('step2/step8');
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('step5/step10');
            resolve('Done!');
        }, duration);
    });
    console.log('step3/step9');
    return promise;
};

function trackUserHandler() {
    let positionData;
    getPosition()
        .then(
            (posData) => {
                console.log('step7');
                positionData = posData;
                return setTimer(2000);
            },
            (err) => {
                console.log('step7.5');
                console.log(err);
                return setTimer(2000);
            }
        )
        .catch((err) => {
            console.log('step7.6');
            console.log(err);
        })
        .then((data) => {
            console.log('step11');
            console.log(data, positionData);
        });
    setTimer(1000).then(() => {
        console.log('Timer done!');
    });
    console.log('step4');
    console.log('Getting position...');
}

button.addEventListener('click', trackUserHandler);
```



# Handle error in then
- `then()` has 2 args
	- The first arg is for resolve (success)
	- The second arg is for reject (error)
```js
sampleFunc()
	.then(
		(resolveData1) => {}, // If resolve (success)
		(error1) => {}, // If reject (error)
	)

```


# catch()
- `catch()` will handle `reject` of all `then`() above it
- `catch()` will not handle any `reject` of any `then`() below it
- `catch()` will also handle any `throw Error`
- If 1 `then` get `rejected` which is directly above 1 `catch()`, all `then()` after the rejected `then()` and above the `catch()` is skipped
```js
sampleFunc()
	.then((resolveData1) => {} // If `reject` happens here
	)
	.then((resolveData2) => {} // This is skipped
	)
	.then((resolveData3) => {} // This is also skipped
	)
	.catch((error) => {} // This will execute to catch error from then1
	)
	.then((resolveData4) => {} // This will run after `catch`
	);
```

- If error happens in a `then()` which already handle `reject`, the `catch()` will not execute
```js
sampleFunc()
	.then(
		(resolveData1) => {},
		(error1) => {} // If `reject1` happens here
	)
	.then((resolveData2) => {} // If `reject2` happens here
	)
	.then((resolveData3) => {} 
	)
	.catch((error) => {} // This will catch reject2, not reject1 because reject1 is already handled
	)
	.then((resolveData4) => {} // This will run after `catch`
	);
```


# Promise.race()
- All functions are execute but only take the resolve of the fastest function
- If 1 function is `reject`, all functions still execute
	- If no function is done, a `reject` will be sent
	- If at least 1 function is done, a `resolve` of said function is sent, no `reject` will be sent

```js
Promise.race([function1(), function2()]).then((data) => { // Both functions are execute
    console.log(data); // data = resolve of fatster function
});
```


# Promise.all()
- All functions are execute
- Only return `result` when all functions are done
- `result` is list of `resolve` with the same sequence as the input functions no matter which ends sooner
- If 1 function is `reject`, all other function still execute
	- No `resolve` will be sent => No `result`
	- A `reject` will be sent

```js
Promise.race([function1(), function2(), function3()]).then((result) => {
    console.log(result); // result === [resolve1, resolve2, resolve3]
});
```

# Promise.allSettled()
- All function are execute no matter `resolve` or `reject`
- Return list of details of `resolve` and `reject` with the same sequence as the input functions

```js
Promise.allSettled([function1(), function2(), function3()]).then(
    (result) => {
        console.log(result);
    }
);
```



# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- [[01_Experience/Code/JavaScript/JavaScript/async await/async await]]
