# 

ResNet introduces skip connection (or shortcut connection) to fit the input from the previous layer to the next layer without any modification of the input.

# Problem with deep network:

- During backpropagation (the learning, changing weight process) of the plain (old) network, we need to take partial derivative of the error function on each layer. For an n-layer network, this process has the effect of multiplying n of these small / large numbers to compute gradients of the “front” layers.
- If these n numbers are small, the gradients of the “front” layers will become zero (vanished); or if these n numbers are big, the gradients will become too large (explode).
- Therefore, very deep plain networks get higher training error and test error than moderately deep ones.


# Skip / shortcut connection in Residual Network:

- To solve this problem, a skip / shortcut connection is added to add the input x to the output after few weight layers:
![[01_Experience/AI_notes/Model_architecture/ResNet/Residual_block.png]]

- Hence, the output $H(x)= F(x) + x$. The weight layers actually is to learn a kind of residual mapping: $F(x)=H(x)-x$.
- Even if there is vanishing gradient for the weight layers, we always still have the identity x to transfer back to earlier layers.
- In traditional neural networks, each layer feeds into the next layer. In a network with residual blocks, each layer feeds into the next layer and directly into the layers about 2–3 hops away.

# Architecture:

![[01_Experience/AI_notes/Model_architecture/ResNet/Architecture_comparison.png]]

- The VGG-19 is a state-of-the-art approach in ILSVRC 2014.
- 34-layer plain network (middle) is treated as the deeper network of VGG-19, i.e. more conv layers.
- 34-layer residual network (ResNet) is the plain one with addition of skip / shortcut connection.

# Bottleneck Design

- Bottleneck design is used to reduce the complexity as follows:

![[01_Experience/AI_notes/Model_architecture/ResNet/Bottleneck_design.png]]

- The 1×1 conv layers are added to the start and end of network as in the figure (right). This is a technique suggested in Network In Network and GoogLeNet (Inception-v1) to reduce the number of connections (parameters) while not degrading the performance of the network so much.
- This help creating much deeper network becomes possible. he overall architecture for all network is as below:

![[01_Experience/AI_notes/Model_architecture/ResNet/Multiple_architectures.png]]

# Other Settings

- Batch Normalization (from Inception-v2) is used after each conv.
- 10-crop testing is used.
- Fully convolutional form with averaging the scores at multiple scales {224, 256, 384, 480, 640} is adopted.
- 6 models are used for ensemble boosting.


# 

---
- Status: #done 

- Tags: #CNN #model_architecture 

- References:
	- [Source](https://towardsdatascience.com/review-resnet-winner-of-ilsvrc-2015-image-classification-localization-detection-e39402bfa5d8)

- Related:
	- 