# Architecture evolution on ImageNet

![[01_Experience/AI_notes/Model_architecture/Architecture evolution of computer vision on ImageNet#Architecture evolution of computer vision on ImageNet]]


# Training and regularization methods

- When training models for more epochs, **regularization** methods have significantly improved generalization such as 
	- Dropout ([Srivastava et al., 2014](https://jmlr.org/papers/v15/srivastava14a.html))
	- Label smoothing ([Szegedy et al., 2016](https://arxiv.org/abs/1512.00567))
	- Stochastic depth ([Huang et al., 2016](https://arxiv.org/abs/1603.09382))
	- Dropblock ([Ghiasi et al., 2018](https://arxiv.org/abs/1810.12890))
	- Data augmentation:
		- [Zhang et al., 2017](https://arxiv.org/abs/1710.09412)
		- [Yun et al., 2019](https://arxiv.org/abs/1905.04899)
		- [Cubuk et al., 2018](https://arxiv.org/abs/1805.09501); [2019](https://arxiv.org/abs/1909.13719)

- Improved **learning rate** schedules have further increased final accuracy:
	- [Loshchilov & Hutter, 2016](https://arxiv.org/abs/1608.03983)
	- [Goyal et al., 2017](https://arxiv.org/abs/1706.02677))


# Scaling strategy

- Increasing the model dimensions (e.g. width, depth and resolution):
	- [Rosenfeld et al., 2019](https://arxiv.org/abs/1909.12673)
	- [Hestness et al., 2017](https://arxiv.org/abs/1712.00409)
- Sheer scale was exhaustively demonstrated to improve performance of neural language models ([Kaplan et al., 2020](https://arxiv.org/abs/2001.08361))
	- Which motivated the design of ever larger models including
		- GPT-3 ([Brown et al., 2020](https://arxiv.org/abs/2005.14165))
		- Switch Transformer ([Fedus et al., 2021](https://arxiv.org/abs/2101.03961)).
	- Similarly, scale in computer vision has proven useful
		- [Huang et al. 2018](https://arxiv.org/abs/1811.06965) designed and trained a 557 million parameter model, 
		- [AmoebaNet](https://arxiv.org/abs/1802.01548), which achieved 84.4% top-1 ImageNet accuracy.
		- Typically, ResNet architectures are scaled up by adding layers (depth): ResNets, suffixed by the number of layers, have marched onward from ResNet-18 to ResNet-200, and beyond
			- [He et al., 2016](https://arxiv.org/abs/1603.05027)
			- [Zhang et al., 2020](https://arxiv.org/abs/2004.08955)
			- [Bello, 2021](https://arxiv.org/abs/2102.08602)
		-  Scale the width:
			-  Wide ResNets [Zagoruyko & Komodakis, 2016](https://arxiv.org/abs/1605.07146)
			-  MobileNets [Howard et al., 2017](https://arxiv.org/abs/1704.04861)
- Increasing image resolutions has also been a reliable source of progress. Thus as training budgets have grown, so have the image resolutions:
	- 600 image resolutions: EfficientNet([Tan & Le, 2019](https://arxiv.org/abs/1905.11946))
	- 448 image resolutions: 
		- ResNeSt ([Zhang et al., 2020](https://arxiv.org/abs/2004.08955))
		- TResNet ([Ridnik et al., 2020](https://arxiv.org/abs/2003.13630))
- *Compound scaling rule* in EfficientNet is sub-optimal for not only ResNets, but EfficientNets as well (proof in section 7.2).


# Additional training data


Another popular way to further improve accuracy is by training on additional sources of data (either labeled, weakly labeled, or unlabeled).
- Pretraining on large-scale datasets
	- Research on large-scale datasets:
		- [Sun et al., 2017](https://arxiv.org/abs/1707.02968)
		- [Mahajan et al., 2018](https://arxiv.org/abs/1805.00932)
		- [Kolesnikov et al., 2019](https://arxiv.org/abs/1912.11370)
	-  Resulting in significant push in the state-of-the-art:
		- [ViT (Dosovitskiy et al., 2020)](https://arxiv.org/abs/2010.11929)
		- [NFNets (Brock et al., 2021)](https://arxiv.org/abs/2102.06171)
- Noisy Student, a semi-supervised learning method, obtained 88.4% ImageNet top-1 accuracy by using pseudolabels on an extra 130M unlabeled images [(Xie et al., 2020](https://arxiv.org/abs/1911.04252)).
- Meta pseudo-labels ([Pham et al., 2020](https://arxiv.org/abs/2003.10580)), an improved semi-supervised learning technique, currently holds the ImageNet state-of-the-art (90.2%)





# 

---
Status: #done 

Tags: #computer_vision  #evolution #data_augmentation #model_architecture #ai_training #scaling

References:
- [# Revisiting ResNets: Improved Training and Scaling Strategies](https://arxiv.org/abs/2103.07579)


Related:
- [[01_Experience/AI_notes/Model_architecture/Architecture evolution of computer vision on ImageNet]]
