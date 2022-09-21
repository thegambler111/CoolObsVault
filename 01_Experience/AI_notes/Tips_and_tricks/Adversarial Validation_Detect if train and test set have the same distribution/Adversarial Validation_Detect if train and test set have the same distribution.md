# Detect if train and test set have the same distribution
- => Use **Adversarial Validation** to train a model to try to separate training samples from test samples

## Process
- Mix together your training and test data
- Drop the target column
- Create a new binary target column
- Set the target to 1 for every training sample
- Set it to 0 for every test sample.
- Split this data
- Train a new model


## Evaluate
- The goal of this new model is to try and tell training samples apart from test samples.
- You can evaluate this model using a ROC curve.
	- The model can't distinguish the splits if the AUC is close to 0.5. That's a good thing!
	- But if the AUC is closer to 1.0, there's something wrong: your model has no trouble identifying training samples from test samples. 
		- => Something is giving that information away!
		- To identify the drift, we can list every feature and its importance in predicting whether a sample belongs to the training or test splits.
		- Then we can go feature after feature and find out what's causing the drift.



# 

---
- Status: #done

- Tags: #tips_and_tricks #machine_learning #drift_in_ml

- References:
	- [Source](https://twitter.com/svpino/status/1554436881734983680)
	- [Adversarial Validation](https://www.youtube.com/watch?v=c5ClgEhAhK0)
	- [Code example](https://www.kaggle.com/code/carlmcbrideellis/what-is-adversarial-validation/notebook)

- Related:
	- 
