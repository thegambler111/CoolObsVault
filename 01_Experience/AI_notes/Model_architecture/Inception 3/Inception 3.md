# Factorization.
+ The aim of factorizing Convolutions is to reduce the number of connections/parameters without decreasing the network efficiency.
+ **Factorization Into Smaller Convolutions:**
	- Two 3×3 convolutions replaces one 5×5 convolution:
	- By using 1 layer of 5×5 filter, number of parameters = 5×5=25
	- By using 2 layers of 3×3 filters, number of parameters = 3×3+3×3=18

	- New Inception modules A:

![[01_Experience/AI_notes/Model_architecture/Inception 3/Incept_v3_module_A.png]]

+ **Factorization Into Asymmetric Convolutions:**
	- For example:
		- One 3×1 convolution followed by one 1×3 convolution replaces one 3×3 convolution:
		- By using 3×3 filter, number of parameters = 3×3=9
		- By using 3×1 and 1×3 filters, number of parameters = 3×1+1×3=6
- New Inception modules B:

![[01_Experience/AI_notes/Model_architecture/Inception 3/incept_v3_module_B.png]]

- New Inception modules C:

![[01_Experience/AI_notes/Model_architecture/Inception 3/incept_v3_module_C.png]]

(Promoting high dimensional representations = go deeper)

# Auxiliary Classifier:
- Using only 1 as regularizer instead of 2 like in inception-v1
	+ How regularizer ?

# **Efficient Grid Size Reduction:**

- The feature map downsizing in older models is done by max pooling. But the drawback is either too greedy by max pooling followed by conv layer, or too expensive by conv layer followed by max pooling. An efficient grid size reduction is proposed Inception-v3 as follows:

![[01_Experience/AI_notes/Model_architecture/Inception 3/Grid_size_reduction.png]]

- 320 feature maps are done by conv with stride 2. 320 feature maps are obtained by max pooling. These 2 sets of feature maps are then concatenated as 640 feature maps.

# Architecture:

![[01_Experience/AI_notes/Model_architecture/Inception 3/Architecture.png]]


# 

---
- Status: #done 

- Tags: #CNN #model_architecture 

- References:
	- [Source](https://sh-tsang.medium.com/review-inception-v3-1st-runner-up-image-classification-in-ilsvrc-2015-17915421f77c)
	- [Comparing Inception versions](https://towardsdatascience.com/a-simple-guide-to-the-versions-of-the-inception-network-7fc52b863202)

- Related:
	- 