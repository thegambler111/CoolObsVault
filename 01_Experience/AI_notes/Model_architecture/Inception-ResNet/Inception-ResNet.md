# Architecture:

- Inception-ResNet-v1 and v2 share the same architecture.
- Inception-v4 vs Inception-ResNet-v1 and v2:
![[01_Experience/AI_notes/Model_architecture/Inception-ResNet/Architecture_comparison.png]]


# Change in modules:

- For residual addition to work, the input and output after convolution must have the same dimensions. Hence, we use 1x1 convolutions after the original convolutions, to match the depth sizes (Depth is increased after convolution)

- Inception-ResNet-v1: Module A, B and C
![[01_Experience/AI_notes/Model_architecture/Inception-ResNet/V1_module_A_B_C.png]]


- Inception-ResNet-v2: Module A, B and C

![[01_Experience/AI_notes/Model_architecture/Inception-ResNet/V2_module_A_B_C.png]]


- Inception-ResNet-v1 and v2 only differences are the amount of hyperparameters.
- The pooling operation inside the main inception modules were replaced in favor of the residual connections. However, those operations are still in the reduction blocks.
- Reduction block A is the same as Inception-v4’s, but block B changes a little:
![[01_Experience/AI_notes/Model_architecture/Inception-ResNet/Reduction_module.png]]

- Networks with residual units deeper in the architecture caused the network to “die” if the number of filters exceeded 1000. Hence, to increase stability, the authors scaled the residual activations by a value around 0.1 to 0.3.

![[01_Experience/AI_notes/Model_architecture/Inception-ResNet/Scaling_block.png]]

- The original paper only use BatchNorm on top of the traditional layer, not after summation in order to fit the entire model on a single GPU.

- It was found that Inception-ResNet models were able to achieve higher accuracies at a lower epoch.

# 

---
- Status: #done 

- Tags: #CNN #model_architecture 

- References:
	- [Source](https://towardsdatascience.com/review-inception-v4-evolved-from-googlenet-merged-with-resnet-idea-image-classification-5e8c339d18bc)
	- [Comparing Inception versions](https://towardsdatascience.com/a-simple-guide-to-the-versions-of-the-inception-network-7fc52b863202)

- Related:
	- 