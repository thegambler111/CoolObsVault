# Covariant shift
Data distribution changing: The distribution of training set and testing set are different (The use case is not similar to the training set)

# Batch normalization (for hidden layers)

![[01_Experience/AI_notes/Model_architecture/Inception 2/BatchNorm.png]]

(Here we learn γ, β)

+ Calculation speeds up
+ Latter layers are more robust to change of earlier layers (reduce the amount of distribution of the hidden units shift around)
+ Having slight regularization effect:


- Each mini-batch mean and variance are computed which adds some noise to that mini-batch because the mean and variance value of the mini-batch don’t represent those of the data set well.
- (At test time, the mean and variance are calculated as average of means and variances of all mini-batch in the test data set)


# 

---
- Status: #done 

- Tags: #CNN #model_architecture 

- References:
	- [Source](https://sh-tsang.medium.com/review-batch-normalization-inception-v2-bn-inception-the-2nd-to-surpass-human-level-18e2d0f56651)
	- [Comparing Inception versions](https://towardsdatascience.com/a-simple-guide-to-the-versions-of-the-inception-network-7fc52b863202)

- Related:
	- 