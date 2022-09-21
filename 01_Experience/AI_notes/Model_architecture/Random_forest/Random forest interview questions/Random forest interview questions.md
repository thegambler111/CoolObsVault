# Random forest interview questions

## Q: What ensemble principle is used in Random Forests?

A: Random Forest works on the principle of the bagging ensemble technique.

Bagging stands for Bootstrap Aggregation.
In Bagging, random data samples in a training set are used with replacement.


## Q: Do Random Forests require pruning?

A: Random Forests usually do not require pruning as they don't overfit like a single DT as trees are bootstrapped and multiple random trees use random features so the individual trees are strong predictors without being correlated.


## Q: What is Out-of-Bag score? When is it used?

A: In this method, we take observation samples and show them only to all those trees that have not been trained on them and evaluate the result.

In the cases where we don’t have a large dataset and want to consume it all for training then OOB can be useful. 

Otherwise, it’s better to have an unseen validation set since OOB works only with a subset of DTs.


## Q: What are some hyperparameters in Random Forests?

A: Some common hyperparameters for random forests are:
• max_depth
• n_estimators
• max_leaf_nodes
• max_features
• min_sample_split
• min_samples_leaf
• criterion

## Q: What's the difference between Gini Index and Entropy? What's the one advantage Gini Index has over Entropy?

A: Both are very similar as they both measure impurity. But Gini Index has values inside the interval [0, 0.5] whereas the interval of the Entropy is [0, 1].
Gini Index has the advantage of quicker computation over Entropy since Entropy makes use of logarithms which are computationally expensive.


## Q: What are weak learners in random forests?

A: Weak learners are the simple models that do slightly better than random guessing.

In random forests, decision trees are used as weak learners.

## Q: What's "random" in Random Forests? And how does it help?

A: It refers to the random subset of data and features that are used with replacement to train weak learners.

This helps because the weak learners trained in the process are less correlated with each other.

## Q: What's the one disadvantage Random Forests have over Decision Trees?

A: Unlike decision trees, random forests are not interpretable.

We can interpret simple trees by the rules that are formed, but it's not doable for random forests since there are multiple trees.


## Q: Is Random Forest sensitive to outliers or not?

A: Random forests are insensitive to outliers. It is because the models or the weak learners fitted locally for each subspace. One weak learner doesn't affect the entire model.

Also just like a median is unaffected by outliers, tree based models do splitting of nodes so bucketing is quite unaffected by outliers.
 




# 

---
- Status: #done

- Tags: #random_forest

- References:
	- [Source](https://twitter.com/capeandcode/status/1564938568107040768)

- Related:
	- 
