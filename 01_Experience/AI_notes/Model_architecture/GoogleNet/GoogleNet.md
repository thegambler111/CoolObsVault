# GoogleNet (or Inception 1)


# Inception module

![[01_Experience/AI_notes/Model_architecture/GoogleNet/dog.jpeg]]
- Salient parts in the image can have extremely large variation in size.
	- Other networks use many conv layers (very deep) to coop with that which makes the network computationally expensive.
	- Inception-v1 use multiple filters with different size on each layer. This approach makes the network a bit “wider” but significantly less “deep” while maintaining robustness with size variation.
	- ![[01_Experience/AI_notes/Model_architecture/GoogleNet/incep_layer.png]]



# 1×1 Convolution

- The author uses 1x1 convolutions to reduce the number of operations. Here is a comparison between using and not using 1x1 conv layer:

## Without the Use of 1×1 Convolution
- Number of operations = (14×14×48)×(5×5×480) = 112.9M

![[01_Experience/AI_notes/Model_architecture/GoogleNet/incept2.png]]

## With the Use of 1×1 Convolution

- Number of operations for 1×1 = (14×14×16)×(1×1×480) = 1.5M
- Number of operations for 5×5 = (14×14×48)×(5×5×16) = 3.8M
- Total number of operations = 1.5M + 3.8M = 5.3M << 112.9M 

![[01_Experience/AI_notes/Model_architecture/GoogleNet/incept3.png]]
	

# Global average pooling

- The last fully-connected layer is replace with a global average pooling in order to reduce the number of weights which helps overfitting.
- Number of weights reduce from: 7×7×1024×1024 = 51.3M to 0 (as pooling does not use weight)

![[01_Experience/AI_notes/Model_architecture/GoogleNet/incept4.png]]


# Auxiliary Classifiers for Training
![[01_Experience/AI_notes/Model_architecture/GoogleNet/Auxiliary Classifiers.png]]

- There are some auxiliary classifiers (intermediate softmax branches) at the middle used for training only. These branches consist of:
	- 5×5 Average Pooling (Stride 3)
	- 1×1 Conv (128 filters)
	- 1024 FC
	- 1000 FC
	- Softmax
- The loss is added to the total loss, with weight 0.3.
- Authors claim it can be used for combating gradient vanishing problem, also providing regularization.


# Other notable techniques
- GoogLeNet are used for ensemble prediction (this is a kind of boosting approach, i.e. using failed predictions from previous model to train next model)
- Multi-scale testing is used just like VGGNet, with shorter dimension of 256, 288, 320, 352. (4 scales)
- Multi-crop testing is used, same idea but a bit different from and more complicated than AlexNet.
- First, for each scale, it takes left, center and right, or top, middle and bottom squares (3 squares). Then, for each square, 4 corners and center as well as the resized square (the full image) (6 crops) are cropped as well as their corresponding flips (2 versions) are generated.
- The total is 4 scales×3 squares×6 crops×2 versions=144 crops/image



# Inception-v1 (GoogLeNet) full architecture:

[Inception-v1 (GoogLeNet) full architecture](https://miro.medium.com/max/2588/1*ZFPOSAted10TPd3hBQU8iQ.png)









# 

---
- Status: #done

- Tags: #CNN #model_architecture 

- References:
	- [Source](https://medium.com/coinmonks/paper-review-of-googlenet-inception-v1-winner-of-ilsvlc-2014-image-classification-c2b3565a64e7)
	- [Comparing Inception versions](https://towardsdatascience.com/a-simple-guide-to-the-versions-of-the-inception-network-7fc52b863202)

- Related:
	- 