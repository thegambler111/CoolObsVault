# Activation functions
- Activation functions are used to introduce **non linearities** in the neural network. 
	- A network that doesn't have activation function is like a linear classifier/regressor.
- Real world problems are rarely linear. 
	- We have to inject non-linearities into the network so it can solve those non linear problems.
	- It's actually like allowing the network to bend itself to fit the problem.

# Tips and tricks

- Always use ReLU in the hidden layers. It's fast and works great
	- Try its versions like Leaky ReLU when you want extra boost in the accuracy or other metrics
- Avoid using sigmoid and tanh in the first layers of the network or generally in all hidden layers
	- They can cause the gradients to vanish quickly
	- They are also computationally expensive (due to the presence of exponent in their formula)
- What activation function should be in the last layer
	- Use sigmoid for binary classification and multi-label classification problems 
	- Use softmax for multi-class classification problems
	- Use ReLU or none if you are merely doing regression
- Always use ReLU at first, try others later

![[01_Experience/AI_notes/Basic_knowledge/Activation functions/Activation functions.png]]

# 

---
- Status: #done 

- Tags: #machine_learning #basic_ai_knowledge #activation_functions

- References:
	- [Source](https://twitter.com/Jeande_d/status/1460963761284517896)

- Related:
	- 
