# Event duplication
- When adding an event **without any arguments**, it should replace the previous identical event
- When adding an event **using bind() function** (and maybe event inside event ???), the event is likely to be **duplicate** (previous identical event with same or different arguments) will **not** be replaced)
- Solution:
	- Replace the node with deep copy of it (this will delete all events)
		- `node1.replaceWith(node1.cloneNode(true));`
	- OR store old event and delete it before adding new event


# Only 1 handler for that event
- Using the default attribute instead of `addEventListener`
	- For example: using `onclick` attribute instead of `addEventListener` function

```js
const btn = document.querySelector('button');

const btnClickHandler = () => {
    alert('Button was clicked!');
};

const btnClickHandler2 = () => {
    alert('Button was clicked 2!');
};

btn.onclick = btnClickHandler;
btn.onclick = btnClickHandler2;
// This will overwrite btnClickHandler => only btnClickHandler2 run
```

# Remove eventListener created with bind()
- `bind()` create and return a new function object => Remove event that use `bind()` (`btnClickHandler.bind(this)` in the example below will not work)
```js
const btnClickHandler1 = () => {...}

btn.addEventListener('click', btnClickHandler.bind(this));
btn.removeEventListener('click', btnClickHandler.bind(this));
// This will not work cause 2 btnClickHandler.bind(this) are 2 different objects
```

- To remove an event that use `bind()`, you need to store it in a variable:

```js
const btnClickHandler1 = () => {...}
const bindedClickHandler1 = btnClickHandler.bind(this)

btn.addEventListener('click', bindedClickHandler1);
btn.removeEventListener('click', bindedClickHandler1);
// This will work cause bindedClickHandler1 are the same object
```

# Useful functions
- `event.stopDefault()` prevents all default behavior of the bowser for that event of that action (i.e. stop go to the link when clicking a link)
- `event.stopPropagation()` prevents triggering handler of ancestor (outer) elements (i.e. stop event trigger for body when clicking a button inside that body)
- `event.currentTarget` is the element which the event is defined for
	- `event.currentTarget` inside `bodyClickHandler222` is `body`
	- `event.currentTarget` inside `btnClickHandler1` is `btn`
- `event.target` is the lowest element which the event trigger from
	- When clicking `btn`, without `event.stopPropagation()`, both `bodyClickHandler222` and `btnClickHandler1` will be trigger
		- `event.target` inside `btnClickHandler1` is `btn`
		- `event.target` inside `bodyClickHandler222` is also `btn`

```js

const bodyClickHandler222 = () => {...}
body.addEventListener('click', bodyClickHandler222);

// The 'btn' is inside 'body'

const btnClickHandler1 = (envent) => {
	event.stopDefault();
	event.stopPropagation(); // This will prevent triggering 'body' click event
}

btn.addEventListener('click', btnClickHandler1);

```

# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
