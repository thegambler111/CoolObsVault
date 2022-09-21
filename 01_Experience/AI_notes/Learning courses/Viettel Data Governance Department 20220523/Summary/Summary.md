# Machine learning fundamental
## Summary
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Summary.png]]

## Supervise learning
### Linear vs logistic regression
- If you want to calculate a specific number (e.g. amount of money this customer spend on mobile this month) use linear regression
- If you want to decide whether an instance belongs to a particular class (e.g. will this customer use the new app or not).

### K-Nearest neighbor
- Based on some (k) of the most similar instances to decide the class of the new instance

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/K-Nearest neighbor.png]]

### Decision tree
- Split the instances into multiple subsets in a tree like structure
- Each split uses a different condition


## Unsupervised learning
### K-Means Clustering
- This technique is used for dataset with no label
- Grouping the instances into k subsets

## Ensemble learning
- This technique is used to combine results from multiple models into a better result
- Using results from multiple models (learners) to get the final results

### Bagging
- All learners (same model) are independent of each others

#### Random forest
- Random forest is a collection of independent decision trees

### Boosting
- Learners (same model) are trained in sequence
	- Using the result of the last learner to modify the dataset for new learner

### Stacking
- Training a new model to combine results from all learners
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Stacking.png]]

## Deep learning
- Deep learning is used when traditional machine learning cannot deliver good enough results

### Deep learning vs traditional machine learning
- In traditional machine learning, all features are hand-crafted (created by human)
- In deep learning, features are discovered by machine

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Machine Learning vs Deep Learning.png]]

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Deep learning vs traditional machine learning.png]]

### Artificial Neural Network (ANN)
- ANN is built based on human brain neuron

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/From Neuron.png]]

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/To ANN.png]]

- It include 1 input layer, 1-2 hidden layer and 1 output layer
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/ANN layers.png]]

### Deep Neural Network (DNN)
- DNN is ANN but with more hidden layers (deeper)

- DNN training components:
	- Loss function:
		- Loss function is a measure of how far the prediction is from ground truth (correct answer)
	- Gradient descent and Backpropagation:
		- Gradient descent and Backpropagation are used to find the local minimum of loss function
	- Learning rate:
		- Learning rate decide the convergent speed
			- Too small -> Too slow
			- Too big -> Cannot converge
	- Activation Functions
		- Activation Functions introduce non-linearity (new knowledge) to the network

#### Convolutional Neural Networks
- Convolutional Neural Networks is mainly used for image tasks
- Convolutional Neural Networks uses convolutional kernels (filters)
	- The kernels separates data into small parts to learn separately
	- After each hidden layers, small parts merge together into bigger parts to learn feature of bigger size

#### Recurrent Neural Network
- Recurrent architecture is used in language tasks like text or voice
- Recurrent architecture learn the order of sequence and dependency among the data.
- Some recurrent architectures:
	- Autoencoders
	- Long Short-Term Memory (LSTM) Networks
	- Encoder-Decoder Architecture

## Generative Adversarial Network GAN
- GAN model is used to create artificial data from source data like images

## Transfer learning
- Using model trained on a similar dataset to train with our dataset
	- Reduce training time
	- Get better results


# Time-series analysis
## Definition
- Definition:
	- Time-series is used to handle time-sequence data
	- Time-series is an ordered sequence of values that are usually equally spaced over time
- Components:
	- Trend:
		- Overall, persistent long-term upward or downward movement
		- Trend can be linear or non-linear
	- Cyclical component:
		- Repeating swings or movements over more than one year
		- The cycles **do not have a fixed frequency**
		- It is often measured peak to peak or trough to trough.
	- Seasonal component:
		- Regular periodic fluctuation, usually within a 12 month period
		- It **has a fixed and known frequency**
	- Irregular component:
		- They are unpredictable fluctuations and can be thought of as random errors
		- Their causes are random variations of nature, accidents, unusual events, noise

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/1_Time-series Analysis/Components.png]]


## Moving averages
- We use average of data in a time window to smooth current data or predict new data
	- Moving Averages can be used to remove seasonal components and identify trend and/or cyclical components
	- It is mainly use as baseline for other techniques

## Exponential Smoothing
- Using **weighted averages** of past observations to forecast
- 3 types of Exponential Smoothing
	-  Simple Exponential Smoothing:
		- For series with no trend or seasonality
	- Holt’s Exponential Smoothing
		- For series with trend and no seasonality
	- Holt-Winter's Exponential Smoothing
		- For series with trend and seasonality
- Usually, only Holt-Winter's Exponential Smoothing is used as the other 2 are not good enough

## Regression-based Models
- Regression can be used to find **global trend** of the entire series in the forecasting period

## Auto-regression Models
- This model is used to find big fluctuation happened every certain time period


# Recommendation system
## Definition
- Recommendation system is a system that gives suggestions / recommendations to users. 
- Types of data:
	- Demographic
		- Data about user’s characteristics
	- Historical
		- Behavior of user in history
	- Content
		- Data about items
	- Context
		- Context where users consume items, such as time, location, weather, …

## Content-based Recommendation System
- Content-based system recommend to customer the items similar to previous items rated highly by them

## Collaborative Filtering
- Based on the rated item of a user:
	- Find items similar to this user's highly rated items 
	- Find other users similar to this user

# Explainable (interpretable) AI
- Interpretability is the degree to which a human can
	- Understand the cause of a decision.
	- Consistently predict the model's result.

## Methods for machine learning interpretability
- 
	- Intrinsic interpretability: models that are considered interpretable due to their simple structure
	- Post hoc interpretability refers to the application of interpretation methods after model training
- 
	- Model-specific interpretation tools are limited to specific model classes
	- Model-agnostic tools can be used on any machine learning model and are applied after the model has been trained (post hoc).
- 
	- Local interpretation method explain an individual prediction.
	- Global interpretation method explain the entire model behavior.

## List of methods
- Model-specific methods:
	- Linear regression
	- Logistic regression
	- Decision tree
- Model-agnostic methods:
	- Partial Dependence Plot (PDP)
	- Individual Conditional Expectation (ICE)
	- Accumulated Local Effects (ALE)
	- Permutation feature importance
	- Global surrogate
	- LIME
	- SHAP
- Example-based explanation:
	- Counterfactual explanation
	- Adversarial example
	- Influential instances
- Neural network interpretation:
	- Learned features
	- Pixel attribution
	- Detecting concepts

# MLOps
- MLOps is used to ease the process of develop and deploy a machine learning project

## MLOps Key Features
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/MLOps key features.png]]

### Scoping
- Define target and constraints of the project

### Data
- Determine whether the data is available, accurate, reliable and how the data will be preprocessed
- How to use the data legally and ethically
- Create feature store for Feature Engineering:
	- Derivatives: Infer new information from existing information
	- Enrichment: Add new external information
	- Encoding: Present the same information differently
	- Combination: Link features together
- Auto Feature Selection

### Model development
- Find suitable models
- Find the best modeling parameters 
- Find a balance between between cost and performance
- Choose validation strategy and evaluation metrics

### Deployment:
- Deploy the system to production
- Monitor and maintain system.
	- Deal with Concept drift and Data Drift 
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/Data Drift and Concept Drift.png]]

## MLOps Maturity
- MLOps level 0: Manual Process
	- Everything is manual
- MLOps level 1: CT (Continuous training)/ML pipeline automation
	- Only training is automatic
- MLOps level 2: CI/CD pipeline automation
	- Everything is automatic



# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
