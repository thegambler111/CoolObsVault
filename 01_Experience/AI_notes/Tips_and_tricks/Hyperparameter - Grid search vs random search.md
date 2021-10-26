# Grid search
-  A list of candidate values for each hyperparameter is defined and evaluated.
-  Select the combination yielding the best performance, preferably evaluated in a validation set.
-  Example:
	- 2 Hyperparameters $\alpha$ and $\beta$.
	- Based on some hypothetical knowledge,  $\alpha$ could be \[1, 2, 3\] and $\beta$ could be \[20, 60, 80\].
	- => Set up a grid of their values:


|     | 1      | 2      | 3      |
| --- | ------ | ------ | ------ |
| 20  | (1,20) | (2,20) | (3,20) |
| 60  | (1,60) | (2,60) | (3,60) |
| 80  | (1,80) | (2,80) | (3,80) |
- 
	- Each combination is evaluated and the one yielding the best performance, for example (3,60), is selected.
	- On the other hand, the global minimum could be located at (2.57, 58)
- This task becomes time-consuming when there are many hyperparameters and the search space is huge, not to mention that a list of candidates must be provided a priori.
> A prior is some proves to show that these candidates are likely to be archive what we want.


# Random search

- Random search is an alternative to grid search by relying on randomness.
- [Random search for hyper-parameter optimization](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf)
- Random search is easily understood and implemented.
- There is no need to provide a priori for the candidate set.
- It is already implemented in [hyperopt library](https://github.com/hyperopt/hyperopt).
- In random search, three components must be specified:
	- Function to measure how good the candidate set are.
	- Search space.
	- Number of trials.


**=> There are other more advanced approaches for hyperparameter optimization, such as Bayesian optimization.**




# 

---
Status: #writing

Tags: #hyperparameter #hyperparameter_optimization #machine_learning #tips_and_tricks

References:
- [# Random Search vs Grid Search for hyperparameter optimization](https://towardsdatascience.com/random-search-vs-grid-search-for-hyperparameter-optimization-345e1422899d)
- [Random search for hyper-parameter optimization](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf)

Related: [[01_Experience/AI_in_production/Lifecycle/Model_training/A Recipe for Training Neural Networks#Tune]]
