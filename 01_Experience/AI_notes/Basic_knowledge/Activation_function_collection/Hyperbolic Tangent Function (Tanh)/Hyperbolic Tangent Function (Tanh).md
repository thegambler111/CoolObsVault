# Description

- The tanh function is also a sigmoid "S"-shaped function.
$$\tanh({z}) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$
- The range of the tanh function is between -1 and 1.

# Plot
![[01_Experience/AI_notes/Basic_knowledge/Activation_function_collection/Hyperbolic Tangent Function (Tanh)/Tanh plot.png]]

-   The tanh function saturates as the inputs become larger (either positive or negative).
-   For large positive and negative values, the function gets asymptotically close to 1 and -1, respectively.
-   When the function saturates, its gradient becomes very close to zero, which slows down learning.

# Derivative
$$\tanh'({z}) = 1 - (\tanh({z}))^{2}$$
![[01_Experience/AI_notes/Basic_knowledge/Activation_function_collection/Hyperbolic Tangent Function (Tanh)/Tanh derivative.png]]

- Notice that the derivative of the tanh function gets very close to zero for large positive and negative inputs.


# Pros
1. The tanh function **introduces non-linearity** into the network which allows it to solve more complex problems than linear activation functions.
2. It is **continuous**, **differentiable**, and have **non-zero derivatives** everywhere.
3. Because its output value ranges from -1 to 1, that makes each layer's output more or less centered around 0 at the beginning of training, which **speed up convergence**.


# Cons
1. **Limited Sensitivity**
	- The tanh function saturates across most of its domain. It is only sensitive to inputs around its **midpoint 0**.

2. **Vanishing Gradients** in Deep Neural Networks
	- Because the tanh function can get easily saturated with large inputs, its gradient gets very close to zero.
	- This causes the gradients to get smaller and smaller as backpropagation progresses down to the lower layers of the network.
	- Eventually, the lower layers' weights receive very small updates and never converge to their optimal values.

- Note: the **vanishing gradient** problem is **less severe** with the tanh function because it has a mean of 0 (instead of 0.5 like the logistic function).



# 

---
- Status: #done 

- Tags: #basic_ai_knowledge #activation_functions 

- References:
	- [Source](https://share.streamlit.io/ammaryh92/activation_functions/main/app.py)

- Related:
	- 
