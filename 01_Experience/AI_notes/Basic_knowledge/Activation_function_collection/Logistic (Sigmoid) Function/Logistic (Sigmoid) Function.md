# Description

- It is a sigmoid function with a characteristic "S"-shaped curve.
$$sigmoid(z) = \frac{1}{1+ \exp(-z)}$$
- The output of the logistic (sigmoid) function is always between 0 and 1.

# Plot

![[01_Experience/AI_notes/Basic_knowledge/Activation_function_collection/Logistic (Sigmoid) Function/Sigmoid plot.png]]

- The logistic function saturates as the inputs become larger (either positive or negative).
- For large positive and negative values, the function gets asymptotically close to 1 and 0, respectively.
- When the function saturates, its gradient becomes very close to zero, which slows down learning.


# Derivative

$$sigmoid'(z) = sigmoid(z)(1 - sigmoid(z))$$

![[01_Experience/AI_notes/Basic_knowledge/Activation_function_collection/Logistic (Sigmoid) Function/Sigmoid derivative.png]]
- Notice that the derivative of the logistic function gets very close to zero for large positive and negative inputs.


# Pros
1. The logistic function **introduces non-linearity** into the network which allows it to solve more complex problems than linear activation functions.
2. It is **continuous and differentiable everywhere**.
3. Because its output is between 0 and 1, it is very common to use in the output layer in **binary classification** problems.


# Cons
1.  **Limited Sensitivity**
	- The logistic function saturates across most of its domain.
	- It is only sensitive to inputs around its **midpoint 0.5**.
2.  **Vanishing Gradients** in Deep Neural Networks
	- Because the logistic function can get easily saturated with large inputs, its gradient gets very close to zero. This causes the gradients to get smaller and smaller as backpropagation progresses down to the lower layers of the network.
	- Eventually, the lower layers' weights receive very small updates and never converge to their optimal values.



# 

---
- Status: #done 

- Tags: #basic_ai_knowledge #activation_functions 

- References:
	- [Source](https://share.streamlit.io/ammaryh92/activation_functions/main/app.py)

- Related:
	- 
