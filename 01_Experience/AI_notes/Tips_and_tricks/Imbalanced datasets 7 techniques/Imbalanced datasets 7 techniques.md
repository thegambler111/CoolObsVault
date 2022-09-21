# TLDR
1. Pick the appropriate performance metric
2. Collect more data
3. Generate synthetic data
4. Resample the dataset
5. Use different weights
6. Try different algorithms
7. Approach the problem correctly.

# What's an imbalanced dataset ?
- An imbalanced dataset has a significant difference in the number of samples for each class.


# What is the problem ?
- Imagine your dataset has 950 cat pictures and only 50 dog pictures.
- A model that classifies every picture as a cat will be 95% accurate!

# How to solve it ?
## Accuracy is not a good metric for imbalanced problems.
- Instead, look at any of the following metrics:
	- A combination of Precision and Recall
	- F-Score
	- Confusion Matrix
	- ROC Curves

## Collect more data
- This is the simplest solution

## Augment the dataset with synthetic data.

## Resample your dataset
- Both over and undersampling introduce biases into your dataset by arbitrarily changing the data distribution
- For example:
	- Oversample the pictures of dogs.
		- Use every dog pictures 4 times (50x4=200)
	- Undersample the pictures of cats.
		- Use every other cat picture (950/2=475)

## Weight each class differently.

## Different algorithms handle imbalances differently.
- Decision Trees are excellent at handling imbalanced classes
- Neural networks, not so much

## Make sure you approach the problem correctly.
- Many people have tried to solve anomaly detection problems using multi-class classification.



# 

---
- Status: #done

- Tags: #tips_and_tricks #machine_learning 

- References:
	- [Source](https://twitter.com/svpino/status/1546826721839566848)

- Related:
	- 
