# Stochastic Gradient Descent (SGD)
- SGD uses a single sample of data on every [[01_Experience/AI_notes/Basic_knowledge/Iteration#Iteration|iteration]].
- Advantages of Stochastic Gradient Descent:
	- Faster learning on some problems.
	- The algorithm is simple to understand.
	- Avoids getting stuck in local minima.
	- Provides immediate feedback.

- Disadvantages of Stochastic Gradient Descent:
	- Computationally intensive.
	- May not settle in the global minimum.
	- The performance will be very noisy.


# Batch Gradient Descent
- The algorithm uses all of the data on every [[01_Experience/AI_notes/Basic_knowledge/Iteration#Iteration|iteration]].
- Advantages of Stochastic Gradient Descent:
	- Computationally efficient.
	- Stable performance (less noise).

- Disadvantages of Stochastic Gradient Descent:
	- Requires a lot of memory.
	- Slower learning process.
	- May get stuck in local minima.


# Mini-Batch Gradient Descent
- The algorithm uses some of the data (> 1 and < all) on every [[01_Experience/AI_notes/Basic_knowledge/Iteration#Iteration|iteration]].
- Advantages of Stochastic Gradient Descent:
	- Avoids getting stuck in local minima.
	- More computationally efficient than SGD.
	- Doesn't need as much memory as BGD.

- Disadvantages of Stochastic Gradient Descent:
	- New hyperparameter [[01_Experience/AI_notes/Basic_knowledge/Batch size#Batch size|batch_size]], which is one of the most influential parameters in the outcome of a neural network, to worry about.


# Conclusion
- Mini-Batch Gradient Descent is the way to go.
- Empirical evidence suggests that smaller batches perform (< 100) better than bigger ones (> 100)
- batch_size = 32 is a good starting point.


# 

---
Status: #done 

Tags: #machine_learning  #basic_knowledge #batch_size

References:

Related:
