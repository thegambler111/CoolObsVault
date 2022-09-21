# Fibonacci numbers
- Let's start with the simplest example for recursion: Fibonacci numbers.
	- Each Fibonacci number is the sum of the previous one and the one before.
	- The recursion starts with 0 and 1.
$${
\begin{align}
F_0 &= 0\\
F_1 &= 1\\
F_n &= F_{n-1} + F_{n-2}
\end{align}
}$$
- Python implementation:
```python
def fibonacci(n):
	if n === 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
```

- The execution is extremely slow:
![[01_Experience/Math/Using matrix multiplication to do recursion with speed of light/python implementation runtime.png]]

# Matrix multiplication
$$
\begin{bmatrix}
	a & b\\
\end{bmatrix}
\begin{bmatrix}
	x\\
	y\\
\end{bmatrix}
= ax + by
$$

# From matrix multiplication to Fibonacci recursion

- We can express the Fibonacci recursion in terms of vectors:
$$
\begin{align}
\begin{bmatrix}
	F_{n} & F_{n-1}\\
\end{bmatrix}
\begin{bmatrix}
	1\\
	1\\
\end{bmatrix}
&= F_{n} + F_{n-1} \\
&= F_{n+1}
\end{align}
$$

- By adding a second column to the right side, we can copy the n-th Fibonacci number over. Thus, we have a recursive relation.
$$
\begin{align}
\begin{bmatrix}
	F_{n} & F_{n-1}\\
\end{bmatrix}
\begin{bmatrix}
	1 & 1\\
	1 & 0\\
\end{bmatrix}
&=
\begin{bmatrix}
	F_{n} + F_{n-1} & F_{n}\\
\end{bmatrix} \\
&= 
\begin{bmatrix}
	F_{n+1} & F_{n}\\
\end{bmatrix} \\
\end{align}
$$
- Applying our matrix recursion n times, we obtain an explicit formula to calculate the Fibonacci numbers.
$$
\begin{align}
\begin{bmatrix}
	F_{1} & F_{0}\\
\end{bmatrix}
\begin{bmatrix}
	1 & 1\\
	1 & 0\\
\end{bmatrix}^n
&= 
\begin{bmatrix}
	F_{n+1} & F_{n}\\
\end{bmatrix} \\
\end{align}
$$
- By noticing that the Fibonacci numbers start with 0, 1, 1, we can stack two shifted vectors on top of itself and obtain the n+1-th, n-th, n-1-th Fibonacci numbers purely by raising the right matrix to the n-th power.
$$
\begin{align}
\begin{bmatrix}
	F_{2} & F_{1}\\
	F_{1} & F_{0}\\
\end{bmatrix}
\begin{bmatrix}
	1 & 1\\
	1 & 0\\
\end{bmatrix}^{n-1}
&= 
\begin{bmatrix}
	1 & 1\\
	1 & 0\\
\end{bmatrix}^{n}\\
&= 
\begin{bmatrix}
	F_{n+1} & F_{n}\\
	F_{n} & F_{n-1}\\
\end{bmatrix}
\end{align}
$$

- It is much faster than the vanilla version
![[01_Experience/Math/Using matrix multiplication to do recursion with speed of light/Matrix multiplication implementation runtime.png]]









# 

---
- Status: #done

- Tags: #maths

- References:
	- [Twitter source](https://twitter.com/TivadarDanka/status/1499695654825717763)

- Related:
	- [[01_Experience/Math/How many path of length K between A and B/How many path of length K between A and B]]
