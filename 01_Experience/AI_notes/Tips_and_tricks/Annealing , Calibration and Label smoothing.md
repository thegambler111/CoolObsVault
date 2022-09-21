# TLDR

- An event with higher entropy means that event is represented by more information
- Principle of maximum entropy: the best probability distribution is the one with maximum entropy
- Empirical rule or 68-95-99.7 rule of normal statistical distribution: ![[Images/AI_note_images/Label_smoothing_empirical_rule.png]]
- Simulated Annealing in machine learning helps overcoming local minimal by increase learning rate when at a minimal
- Calibration: A classification model is **calibrated** if its predicted probabilities of outcomes reflect their accuracy.
- Label Smoothing is a regularization technique that introduces noise for the labels by reducing the largest logit
	- The whole label $y$ of training set is correct with probability $1-\alpha$ and incorrect otherwise
	- $${y\_ls = (1 - \alpha) * y\_one\_hot + \alpha / K}$$



# Entropy

- In Physics, entropy is defined as the measure of chaos or disorder in a system
	- Higher entropy = higher chaos
- In information theory, entropy is defined as the expected number of bits of information contained in an event
	- Higher entropy = more information to represent a event
	- Ex: Tossing coin: The information required to identify the result is 1 question => Entropy = 1



# Principle of maximum entropy

> If we have a few number probability distribution that could encode the prior data, then the best probability distribution is the one with maximum entropy


# Empirical Rule

- Empirical means based on, concerned with, or verifiable by observation or experience rather than theory or pure logic
- **Empirical Rule** or **68-95-99.7** is only applicable to **Normal Statistical Distribution** which is **symmetric** and **unimodal** distribution
- Formula: $${\mu \, \pm \, m\sigma}$$
	- Where:
		- $\mu$ = mean/average
		- $\sigma$ = standard deviation
		- $m$ =  multiplier
	- $m = 1$ => Get 68% of data
	- $m = 2$ => Get 95% of data
	- $m = 3$ => Get 99.7% of data

![[Images/AI_note_images/Label_smoothing_empirical_rule.png]]


# Annealing

- Physical annealing is the process of heating up a material until it reaches an **annealing temperature** and then it will be **cooled down** slowly in order to change the material to a desired structure
- Simulated Annealing:
	- is used for optimizing parameters in a model
	- help overcoming local minimal
	- Checkout "CosineAnnealing" in Pytorch optimizer

![[Images/AI_note_images/Label_smoothing_annealing.png]]

- Advantages
	-   Easy to implement and use
	-   Provides optimal solutions to a wide range of problems
- Disadvantages
	-   Can take a long time to run if the annealing schedule is very long
	-   There are a lot of tuneable parameters in this algorithm

# Consine Annealing warm restart


- torch.optim.lr_scheduler.CosineAnnealingWarmRestarts()
- Using this instead of stepLR to over come local minimal.

![[Images/AI_note_images/Label_smoothing_cosine_annealing_warm_restart.png]]



# Label Smoothing

## Calibration

- A classification model is **calibrated** if its predicted probabilities of outcomes reflect their accuracy.
- Example: 100 image predictions:
	- If all is predicted with 0.9 confidence score then 90 images should be classified correctly
	- If all is predicted with 0.6 confidence score then 60 images should be classified correctly
- Model calibration is important for:
	-   model interpretability and reliability (closely calibrated model is more reliable)
	-   deciding decision thresholds for downstream applications
	-   integrating our model into an ensemble or a machine learning pipeline

## Overconfidence

- Model is overconfidence if its confidence score is significantly higher than the real accuracy


## How to plot calibration

1.  Create a set with three values: predicted label, predicted confidence score, and real label.
2.  Sort this set in ascending order of the predicted confidence score
3.  Now divide the data set in bins of some fixed size . If the data set is large then keep bin size large and vice versa.
4.  Now calculate actual accuracy and the average of confidence score in each bin.
5.  Plot a graph with actual accuracy on y-axis,  average confidence score on x-axis, and a perfected calibration line x=y.
6.  If the accuracy-confidence line is above perfected calibration line then the model is underconfident and vice versa.

![[Images/AI_note_images/Label_smoothing_calibration_chart.png]]


## Label smoothing

- Label Smoothing is a regularization technique that introduces noise for the labels. This accounts for the fact that datasets may have mistakes in them, so maximizing the likelihood of $log\,p(y|x)$ directly can be harmful. Assume for a small constant $\alpha$, the training set label $y$ is correct with probability $1-\alpha$ and incorrect otherwise. Label Smoothing regularizes a model based on a softmax with $k$ output values.
- In short, label smoothing is a regularization technique as it restrains the largest logit from becoming much bigger than the rest.
- Label smoothing does improve calibration according to [this paper](https://arxiv.org/abs/1906.02629v3)
- Formula: $${y\_ls = (1 - \alpha) * y\_one\_hot + \alpha / K}$$
- Where: $y\_hot$ is result after softmax
- Example 1:
$\alpha = 0.1$
$y\_hot = [1, 0 , 0]$
=> $K=3$
=> $y\_ls = [0.9333, 0.0333, 0.0333]$

- Example 2:
$\alpha = 0.1$
$y\_hot = [0.8, 0.2 , 0]$
=> $K=3$
=> $y\_ls = [0.7533, 0.2133, 0.0333]$

- Label smoothing effect on different datasets:
![[Images/AI_note_images/Label_smoothing_experiments_with_different_datasets.png]]

# 

---
Status: #writing

Tags: #tips_and_tricks #machine_learning #hyperparameter

References:
-  [# Maximum Entropy Reinforcement Learning](https://medium.com/intro-to-artificial-intelligence/maximum-entropy-reinforcement-learning-ee7ad77289c0)
-  [Regularizing neural networks by penalizing confident output distrbutions](https://arxiv.org/abs/1701.06548)
-  [(Label smoothing proposing paper) Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/pdf/1512.00567.pdf)
-  [# Empirical Rule - Statistics](https://medium.com/geekculture/empirical-rule-statistics-811b004d58b8)
-  [# Optimization Techniques - Simulated Annealing](https://towardsdatascience.com/optimization-techniques-simulated-annealing-d6a4785a1de7)
-  [# Calibration in Machine Learning](https://medium.com/analytics-vidhya/calibration-in-machine-learning-e7972ac93555)
-  [# What is Label Smoothing?](https://towardsdatascience.com/what-is-label-smoothing-108debd7ef06)
-  [# When Does Label Smoothing Help?](https://arxiv.org/abs/1906.02629v3)

Related:
- [Entropy explained](https://twitter.com/TivadarDanka/status/1475456688547250176)
