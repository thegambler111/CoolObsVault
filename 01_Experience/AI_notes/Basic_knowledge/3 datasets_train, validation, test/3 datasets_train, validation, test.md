# 3 datasets: train, validation, test
- We usually split the data into three different sets:
	- Train set
	- Validation set
	- Test set

## Train set:
- You'll use this to train your model
- You'll also use this data for every analysis, transformation, and decision.

## Validation set:
- You'll use this data to compute your model's performance and decide how to improve it.
- The validation set gives you feedback to improve your model.
- Inevitably, your model will start overfitting to the validation set after some time.
	- => Your validation set won't give you helpful feedback anymore
	- Solution:
		- After several iterations, throw your validation set into your train set and get new data to create a new validation set.
		- If you don't have more data, you must rely heavily on k-fold cross-validation.

## Test set:
- The goal of your test set is to provide a final, unbiased estimation of your model's performance.
- A good test set will give you a performance similar to what you expect when processing production data.
- Until the very end, you never look at your test data.
- You never use it to do any analysis or transformations. Never make decisions that affect your model using the test data.
- => **Use your test data once. After that, merge it into your train set and find new test data.**


# Prevent data leaking from transforming dataset before splitting
1. Split your data first. Only then do any transformations.
1. Data leakage is cheating. Your model will look better than it is.
1. If you peek into your test set, is not a good test set anymore.




# 

---
- Status: #done

- Tags: #basic_ai_knowledge

- References:
	- [Source](https://twitter.com/svpino/status/1542840462838378496)

- Related:
	- 
