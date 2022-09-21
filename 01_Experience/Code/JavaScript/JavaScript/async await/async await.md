# 
- Adding `async` before a function wrap that function inside a big invisible `Promise`
- `async` function is not handled by JavaScript but by browser
- Anything inside an `async` function is executed in sequence => Cannot run tasks simultaneously
- Everything inside `async` function is wrapped by invisible `then`
- `await` add invisible `then` block and return `resolve`
- You can use try catch to handle `reject` like normal code

```js
\\ Promise version
function trackUserHandler() {
    let positionData;
    getPosition()
        .then((posData) => {
            positionData = posData;
            return setTimer(2000);
        })
        .catch((err) => {
            console.log(err);
        })
        .then((data) => {
            console.log(data, positionData);
        });
}
```


```js
\\ async await version
async function trackUser() {
    let posData;
    let timerData;
    try {
        posData = await getPosition();
        timerData = await setTimer(2000);
    } catch (err) {
        console.log(err);
    }
    console.log(posData, timerData);
}
```


# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- [[01_Experience/Code/JavaScript/JavaScript/Promise/Promise]]
