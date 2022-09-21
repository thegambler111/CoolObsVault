# 
- Function can access variables from all outer scope (outer function or global)

```js
let multiplier = 1.1;

function taxCalculator(tax) {
    function calculateTax(amount) {
        return amount * tax * multiplier;
        // `amount` from local arg
        // `tax` from arg of outer function
        // `multiplier` from global
    }
}

const calculateVat = taxCalculator(0.23);
const calculateIncomeTax = taxCalculator(0.3);

multiplier = 1.2;
calculateVat(100); // Here `multiplier` will be update and take latest value
```


# 

---
- Status: #done 

- Tags: #js

- References:
	- 

- Related:
	- 
