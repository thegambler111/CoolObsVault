# TLDR

- Architecture:
	- ResNet-D
	- Squeeze-and-Excitation
- Training
	- Image resolution: [160, 192, 224, 256, 320]
	- Depth: [50, 101, 152, 200, 270, 350, 420]
	- Epochs: 350
	- Learning rate: from $0.1 / batch \, size$ decayed to 0 (cosine schedule)
	- Optimizer: Momentum
	- EMA: 0.9999 (for both weights and Batch Norm moving averages)
	- Label smoothing rate: 0.1
	- Stochastic depth rate: 0.0 or 0.1
	- Augmentation method:
		- RandAugment: 10 or 15
		- OR Scale jittering
	- Dropout rate: 0.25 or 0.4
	- Weight decay: $4e-5$



# Vision model improvement since AlexNet 2012

![[01_Experience/AI_notes/Model_architecture/Vision evolution]]


# Architecture changes


## ResNet-D
[He et al., 2018](https://arxiv.org/abs/1812.01187)

- The 7×7 convolution in the stem is replaced by three smaller 3×3 convolutions
- The stride sizes are switched for the first two convolutions in the residual path of the downsampling blocks.
- The stride-2 1×1 convolution in the skip connection path of the downsampling blocks is replaced by stride-2 2×2 average pooling and then a non-strided 1×1 convolution
- The stride-2 3×3 max pool layer is removed and the downsampling occurs in the first 3×3 convolution in the next bottleneck block

| Block Group | Output Size      | Convolution Layout                                                                    |
| ----------- | ---------------- | ------------------------------------------------------------------------------------- |
| stem        | $112 \times 112$ | $\begin{bmatrix}3\times3, 64, s2 \\3\times3, 64 \\3\times3, 64\end{bmatrix}\times 1$  |
| c2          | $56 \times 56$   | $\begin{bmatrix}1\times1, 64 \\3\times3, 64 \\1\times1, 256\end{bmatrix}\times 3$     |
| c3          | $28 \times 28$   | $\begin{bmatrix}1\times1, 128 \\3\times3, 128 \\1\times1, 512\end{bmatrix}\times 4$   |
| c4          | $14 \times 14$   | $\begin{bmatrix}1\times1, 256 \\3\times3, 256 \\1\times1, 1024\end{bmatrix}\times 23$ |
| c5          | $7 \times 7$     | $\begin{bmatrix}1\times1, 512 \\3\times3, 512 \\1\times1, 2048\end{bmatrix}\times 3$  |
|             | $1 \times 1$     | $\begin{bmatrix}Avg \, Pool \\Dropout \\ 1000-d \, FC \end{bmatrix}\times 3$          |



## Squeeze-and-Excitation
[Hu et al., 2018](https://arxiv.org/abs/1709.01507)

- Channels are reweighed via cross-channel interactions by average pooling signals from the entire feature map with a Squeeze-and-Excitation ratio of 0.25 (based on preliminary experiments).



# Training method changes

## Matching the EfficientNet Setup.

Our training method closely matches that of EfficientNet, where we train for 350 epochs, but with a few small differences.
- We use the cosine learning rate schedule ([Loshchilov & Hutter, 2016](https://arxiv.org/abs/1608.03983)) instead of an exponential decay for simplicity (no additional hyperparameters).
- We use RandAugment ([Cubuk et al., 2019](https://arxiv.org/abs/1909.13719)) in all models, whereas EfficientNets were originally trained with AutoAugment ([Cubuk et al., 2018](https://arxiv.org/abs/1805.09501))
- We use the Momentum optimizer instead of RMSProp for simplicity.


|                      | ResNet (2015) | ResNet-RS (2021) | EfficientNets (2019) | $\Delta$ |
| -------------------- | ------------- | ---------------- | -------------------- | -------- |
| Epochs Trained       | 90            | 350              | 350                  | +0.1     |
| LR Decay Schedule    | Stepwise      | Cosine           | Exponential Decay    | ?        |
| Optimizer            | Momentum      | Momentum         | RMSProp              | ?        |
| EMA of Weights       |               | ✅               | ✅                   | _        |
| Label Smoothing      |               | ✅               | ✅                   | +0.5     |
| Stochastic Depth     |               | ✅               | ✅                   | +1.2     |
| RandAugment          |               | ✅               | ✅                   | _        |
| Dropout on FC        |               | ✅               | ✅                   | +1.0     |
| Smaller Weight Decay |               | ✅               | ✅                   | +0.2     |
| Squeeze-Excitation   |               | ✅               | ✅                   | +0.5     |
| Stem Modifications   |               | ✅               | ✅                   | ?        |
| Scale jittering      |               | ✅               |                      | +1.0     | 


## Regularization

For regularization, we apply:
- Weight decay
- Label smoothing
- Dropout
	- Dropout ([Srivastava et al., 2014](https://dl.acm.org/doi/10.5555/2627435.2670313)) is applied to the output after the global average pooling occurs in the final layer.
- Stochastic depth
	- Stochastic depth ([Huang et al., 2016](https://arxiv.org/abs/1603.09382)) drops out each layer in the network (that has residual connections around it) with a specified probability that is a function of the layer depth.


## Data Augmentation

We use RandAugment ([Cubuk et al., 2019](https://arxiv.org/abs/1909.13719)) data augmentation as an additional regularizer.


## Hyperparameter Tuning

To select the hyperparameters, we use a held-out validation set comprising 2% of the **ImageNet** training set (20 shards out of 1024).

- Epochs: 350
- Weight decay: $4e-5$
- EMA: 0.9999 (for both weights and Batch Norm moving averages)
- RandAugment: 10 or 15
- Label smoothing rate: 0.1
- Learning rate: from $0.1 / batch \, size$ decayed to 0 (cosine schedule)
- Dropout rate: 0.25 or 0.4
- Stochastic depth rate: 0.0 or 0.1
- Image resolution: [160, 192, 224, 256, 320]
- Depth: [50, 101, 152, 200, 270, 350, 420]


## Additive Study of Improvements

- Increasing training duration to 350 epochs only becomes useful once the regularization methods are used.
- The performance deceases when we add dropout and/or stochastic depth unless we decease wight decay. (The intuition is that since weight decay acts as a regularizer, its value must be decreased in order to not overly regularize the model when combining many techniques)


#  Improved Scaling Strategies


- Scaling strategy depends on the training regimes (model size or number of epochs):
	- Width scaling is better at lower regimes (~10 epochs)
	- Depth scaling is better at higher regimes (~350 epochs)
- Slower image resolution scaling is better (slower than in EfficientNet).
- Scaling strategies from small regimes cannot generalize for bigger regimes.
- Scaling strategies can be affected by sub-optimal initial architecture.



















# 

---
Status: #done 

Tags: #computer_vision #classification #resnet #resnet_rs #tips_and_tricks #hyperparameter 

References:
- [# Revisiting ResNets: Improved Training and Scaling Strategies](https://arxiv.org/abs/2103.07579)
- [ResNet-RS Tensorflow configs](https://github.com/tensorflow/tpu/tree/master/models/official/resnet/resnet_rs)
- [ResNet-RS in Keras](https://github.com/sebastian-sz/resnet-rs-keras)


Related:
- [[01_Experience/AI_notes/Model_architecture/Vision evolution]]
