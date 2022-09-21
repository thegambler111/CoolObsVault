# Is ReLU continuous and differentiable?
## ReLU definition:
- If x <= 0, the function will return 0. Otherwise, the function will return x.
$$f(x) = max(0, x)$$
## Continuous?
- If you draw this function, you'll notice that there are no discontinuities in the function
- => **ReLU is continuous**

![[01_Experience/AI_notes/Basic_knowledge/ReLU/ReLU graph.png]]

## Differentiable?

- For a function to be differentiable:
	- It must be continuous ✅
	- Its derivative should also exist for every individual point ❓

- We can compute the derivative of a function using this formula
$$\frac{dy}{dx}=\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

- Looking at the chart again, for ReLU to be differentiable, its derivative should exist at $x = 0$
	- That's where the function changes abruptly. 

![[01_Experience/AI_notes/Basic_knowledge/ReLU/ReLU graph.png]]

- For the derivate exists at $x = 0$, the left-hand and right-hand limits at $x = 0$ must exist and are equal


- In the derivative function, replace $f(x)$ with the actual function
$$\frac{dy}{dx}=\lim_{h \to 0} \frac{\max(0,x+h) - \max(0,x)}{h}$$


![](https://api.typefully.com/media-p/d4a9efff-86d6-4485-87e2-f3e12a666edb/)

### Left-hand limit
- At $x = 0$ and $h < 0$:

$$\frac{dy}{dx}=\lim_{h \to 0^{-}} \frac{\max(0, h) - \max(0,0)}{h}$$

$$\frac{dy}{dx}=\lim_{h \to 0^{-}} \frac{0 - 0}{h} = 0$$

- => At $x = 0$ and $h < 0$, the derivative = 0.

### Right-hand limit
- At $x = 0$ and $h > 0$:

$$\frac{dy}{dx}=\lim_{h \to 0^{+}} \frac{\max(0, h) - \max(0,0)}{h}$$

$$\frac{dy}{dx}=\lim_{h \to 0^{+}} \frac{h - 0}{h} = 1$$

- => At $x = 0$ and $h > 0$, the derivative = 0.

---

- Therefore, at $x = 0$
	- The left-hand limit is 0
	- The right-hand limit is 1
- => Both limits exist but are not equal
- => The derivative of ReLU doesn't exist at $x = 0$
- => **ReLU is not differentiable**

# ReLU is not differentiable but can still be used as an activation function when using Gradient Descent?

- In deep learning, it's rare for x to be precisely zero
	- => When $x \approx 0$, we set the derivative to 0 (or any arbitrary value) and move on with our lives



# 

---
- Status: #done

- Tags: #machine_learning #basic_ai_knowledge #svpino

- References:
	- [Question](https://twitter.com/svpino/status/1495835736100073474)
	- [Explanation](https://twitter.com/svpino/status/1496469904735621122)

- Related:
	- 
