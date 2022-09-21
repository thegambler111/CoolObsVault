# Summary

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Summary.png]]

# Supervised learning

## Linear regression
- Using a linear function to calculate output from input data
- Output belongs to a continuous space

- Linear regression function: $$\hat{y} = \theta_0 + \theta_1x_1 + \theta_2x_2+ ... + \theta_nx_n$$
	- $\hat{y}$ is the predicted value
	- n is the number of features
	- $x_i$ is the $i^{th}$ feature value
	- $\theta_i$ is the model parameter of the $i^{th}$ feature value


- MSE (Mean squared error) cost function: is used to find the error rate of our prediction
- MSE $\in [0,1]$
- The smaller MSE, the better the function

## Gradient Descent
- Gradient descent can be used to find the set of model parameters $\theta$ that can give reasonably small MSE
- Motivation: 
	- Finding global minima/maxima if the function is convex
	- Used for optimizing many models in machine learning

- Idea:
	- Start somewhere
	- Take step based on gradient vector of the current position till getting the the lowest point

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Gradient descent.png]]

## Underfitting and overfitting
- Underfitting:
	- Your model perform poorly on both training and testing dataset
- Overfitting:
	- Your model perform very well on training dataset but poorly on testing dataset

## Regularized Linear
- Definition: Regularized linear is the method to reduce overfitting. A simple way to regularize a polynomial model is to reduce the number of polynomial degrees. Regularization is typically achieved by constraining the weights of the model.
- Ridge Regression, Lasso Regression, and Elastic Net, which implement three different ways to constrain the weights


## Logistic regression
- Logistic Regression is used to estimate the probability that an instance belongs to a particular class
- ?

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Logistic regression.png]]

### Linear vs logistic
- Linear Regression is used to handle regression problems whereas Logistic regression is used to handle the classification problems.
- Linear regression provides a continuous output but Logistic regression provides discreet output.


## Support vector machines
- Finding the best hyperplane to separates classes in feature space
- Hyperplane is a multi dimensional planes

## K-Nearest neighbor
- New data X without label
- Find k labeled data nearest to X
- In k labeled data, identify the class Y contains the majority of data
- Then data X belongs to the above class Y

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/K-Nearest neighbor.png]]


## Decision tree
- A decision tree is a machine learning algorithm that partitions the data into subsets
- GINI: $$GINI(S) = 1-\sum_{i=1}^{c} p_i^2$$
- Using GINI to calculate information gain:
	- ????

## Random forest
- Read bagging ensemble


# Unsupervised learning
## K-Means Clustering
- Clustering is the partitioning of a data set into subsets (clusters), so that the data in each subset (ideally) share some common trait
- The k-means Clustering is separate n objects into k partitions
- The grouping is done by minimizing the sum of squares of distances between data and the corresponding cluster centroid

- Silhouette score: Checking the valid of the result
	- SC -> 1: good
	- SC -> -1: bad
	- ? Generally, SC < 0 is bad


# Ensemble learning
- Using results from multiple models to get the final results

## Bagging ensemble method: Random forest
- Random forest consists of multiple independent decision trees
- Each tree has
	- A random sub-sample number of instances of training data
	- A random sub-sample number of features of training features
- We use the average among all the predictions produced by these decision tree as the final prediction
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Bagging.png]]

## Random forest in practice
- In Viettel, max_depth of a decision tree is <= 32
- When training from overfit -> good fit, hyperparameters changes:
	- n_estimators: larger -> fitter
	- max_depth: larger -> fitter
	- min_samples_split: smaller -> fitter
	- min_sample_leaf: smaller -> fitter
	- max_features: larger -> fitter
	- min_impurity_decrease: smaller -> fitter

# Boosting
- Boosting is using many "weak" classifiers to produce a final "strong" classifier
- Start with a weak learner
- Each new weak learner in the sequence tries to correct the misclassification/error made by the previous weak learners
- Final results is the combination results of all weak learners
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Boosting.png]]
## Gradient Boosting
- Using gradient descent to minimize the loss function

## Bagging vs Boosting
- Bagging uses vote to determine the final results
	- All learner is independent of each others
- Boosting to use the wrong output (?) of previous weak learners to teach the new learner
	- All learners are in a sequence

## Stacking
- You have multiple models
- You train a new model to get the final result
	- Using the outputs of all existing models as input of the final model
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Stacking.png]]

---
# Deep learning
# Machine Learning vs Deep Learning
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Machine Learning vs Deep Learning.png]]

# Representation Learning (aka Feature Learning)
- From the input, find the meaningful part of it

# Deep Learning is Representation Learning

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Representation Learning.png]]

# Deep learning vs traditional machine learning
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Deep learning vs traditional machine learning.png]]

- Deep learning is better because of feature attraction is handle by machine
	- Not in all task that deep learning is better than traditional machine learning
		- For example: tabular data

# Artificial Neural Network (ANN)
## Neuron
- Dendrites get inputs
- Nucleus processes data
- Axon verify outputs (whether they are enough to trigger synapses)
- ? Synapses handle outputs


- ![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/Neuron.png]]

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/From Neuron.png]]

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/To ANN.png]]

## Layers

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/3_Machine learning fundamental/ANN layers.png]]

## Activation function
- Activation function has (about) the same function as Axon

# Deep Neural Network (DNN)
- DNN is ANN but with more hidden layers (deeper)

## Lost function
- Loss function is a measure of how far the prediction is from ground truth (correct answer)
- Loss function -> 0 is better
	- => We need to find set of weights and biases with the smallest loss function
- For regression:
	- Mean Squared Error (MSE)
- For classification:
	- Cross Entropy (CE)


## Gradient descent
- Instead of finding the correct weights and biases from the scratch
- We first initialize the weight and biases
- Then we modify those to get to the local minimum of loss function (convergent)

## Backpropagation
- We use backpropagation to find the local minimum of loss function
- Steps:
	- Forward pass to compute network output and "error"
	- Backward pass to compute gradients (distance till local minimum)
	- A fraction (learning rate) of the weight’s gradient is subtracted from the weight to get closer to local minimum

## Learning rate
- Too small learning rate slows down the convergent 
- Too large learning rate may prevent model from convergent

## Activation Functions
- Activation function is used to introduce non-linearity to the neural network, helping model a response variable varying nonlinearly with input variables
	- => Ability to learn complex functions

## Feedforward Neural Networks
- Model always executes in 1 direction

## Convolutional Neural Networks
- Convolutions are calculated by using convolutional kernels (filters) to slide through and multiply image patches by convolutional kernel.
	- => Used in CNN to extract relationship among pixels
	- => Take advantage of spatial invariance

## Recurrent Neural Network

- Recurrent architecture helps take into account the order in the sequence and dependence among sequence elements.


## Transfer learning
- Fine-tune a pre-trained model. 
- Utilize the trained backbone (usually with frozen weights) for other downstream tasks.
- => Leverage existing powerful backbones, reduce time & training resources.


## Autoencoders
- Components
	- Encoder: transforms high-dimensional input into lower dimensional format.
	- Encoded state (latent state): contains compressed representation of input data.
	- Decoder: converts encoded state to original input.

## RNN – Long Short-Term Memory (LSTM) Networks

- Core components in a LSTM module:
	 - Cell state: Store the information of all previous data
	 - Forget gate
	 - Input gate
	 - Output gate

## RNN – Encoder-Decoder Architecture

## Generative Adversarial Network









# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
