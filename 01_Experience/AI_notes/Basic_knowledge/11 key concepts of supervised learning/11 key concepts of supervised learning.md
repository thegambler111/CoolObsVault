# Target (also referred to as "y")
- The target is the piece of information that we are predicting. 

- For example:
	- The animal that's shown in a picture
	- The price of a house
	- Whether a message is spam or not


# Features (also referred to as "x", or "variables")
- These are the input variables to our problem. We use these features to predict the target.

- For example:
	- Pixels of a picture
	- Number of bedrooms of a house
	- Square footage of a house


# Samples (also known as "examples" or "instances")
- A sample is a particular instance of data
- It could be "labeled" (when it specifies the target) or "unlabeled" (when it doesn't.)


# Labeled sample
- Labeled samples are used to train and validate a model. 
- These are usually represented as (x, y), where:
	- "x" is a vector containing all the features
	- "y" is the corresponding target.


# Unlabeled sample
- Unlabeled samples contain features, but they don't contain the target: (x, ?)
- The whole goal of supervised learning is to build a model that predicts the target of unlabeled samples.


# Model
- A model defines the relationship between features and the target.
- You can think of a model as a set of rules that, given certain features, determine the corresponding target.

- For example: Given the bedrooms, bathrooms, and square footage, we get the price.


# Training
- Training is a process that builds a model. 
- We take labeled samples during training, and let the model gradually learn the relationships between features and the target.

# Validation
- Validation is the process that lets us know whether a model is any good.
- Usually, we run a set of (unseen) labeled samples through a model to ensure that it can predict the targets.

# Inference
- Inference is the process of applying a trained model to unlabeled samples to obtain the corresponding targets.
- In other words, "inference" is the process of making predictions using a model.


# Regression
- A regression model predicts continuous values, for example:
	- The value of a house
	- The price of a stock
	- Tomorrow's temperature


# Classification

- A classification model predicts discrete values, for example:
	- The picture is showing a dog or a cat
	- The message is spam or not
	- The forecast is sunny or overcast


# 

---
- Status: #done 

- Tags: #basic_ai_knowledge 

- References:
	- [Source](https://twitter.com/svpino/status/1501905723000692738)

- Related:
	- 
