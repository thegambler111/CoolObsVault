# What is attention?

Attention is a mechanism by which a network can weigh features by level of importance to a task, and use this weighting to help achieve the task.

The idea of attention was born in the area of seq2seq modeling where input and output length are arbitrary, along with long and varied dependency range.
 
=> A need to learn a flexible dependency mechanism.

In computer vision, this dependency is along the spatial domain instead of time domain. The same texture may be present in multiple areas of an image, and an object may have multiple complex and obscured parts throughout an image.

![[Images/AI_note_images/Attention_complimentary_features.png]]

For more detail, read here: [[01_Experience/AI_notes/Model_architecture/Attention Mechanism|Attention Mechanism]]

# Soft vs. Hard Attention in computer vision

Hard attention is when only a subset of the image is visible, hopefully the part most relevant to the task. This approach requires significantly less computation and memory but is harder to train

Soft attention is when the entire image is still being “seen”, but certain areas are being attended to more. This method requires more memory and computation but has a differentiable objective and can be easily trained with standard back propagation methods.

-   **Soft** Attention: the alignment weights are learned and placed "softly" over all patches in the source image (weight is continuous); essentially the same type of attention as in [Bahdanau et al., 2015](https://arxiv.org/abs/1409.0473).
    -   _Pro_: the model is smooth and differentiable.
    -   _Con_: expensive when the source input is large.
-   **Hard** Attention: only selects one patch of the image to attend to at a time (weight is either 0 or 1).
    -   _Pro_: less calculation at the inference time.
    -   _Con_: the model is non-differentiable and requires more complicated techniques such as variance reduction or reinforcement learning to train. ([Luong, et al., 2015](https://arxiv.org/abs/1508.04025))


# Hard attention in classification

![[Images/AI_note_images/Attention_hard_attention.png]]

Figure: Architecture of the AG-CNN presented in [# Attention Guided Convolutional Neural Network for Thorax Disease Classification](https://arxiv.org/abs/1801.09927) with a ResNet-50 backbone as an example.

The network above consists of three branches:

-   **Global branch** processing the entire image and determining the cropping ROI using the heatmap (attention) layer,
-   **Local branch** exhibiting the attention mechanism and processing the cropped image,
-   **Fusion branch** concatenating the pooling outputs of the global and local branches and performing final classification using dense layers.

Here, the hard attention is use when cropping a part of the image and classify that part simultaneously with the whole picture.

# Soft attention in classification
[# Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)

![[Images/AI_note_images/Attention_channel_soft_attention_with_details.png]]

How it work:
- After each transformation (here is a convolution) $F_{tr}$, the squeeze operation $F_{sq}$ is applied to aggregate global feature on each channel.
- Then, the **channel-wise weight** is calculated using excitation operation $F_{ex}$
- Finally, the output of $F_{tr}$ is subsequently multiplied channel-wise by the result of the excitation.

=> Include global information to the local spatial information from convolution in the decision process of the network.

# Queue, key, value



 

# Self-Attention

**Self-attention**, also known as **intra-attention**, is an attention mechanism relating different positions of a single sequence in order to compute a representation of the same sequence.


## Self-attention vs Convolutional
According to [Stand-Alone Self-Attention in Vision Models](https://arxiv.org/pdf/1906.05909.pdf)

### Stem

Convolutional > self-attention

### Full network

Early convolutional + Late self-attention is the best

## Self-attention components importance
According to [Stand-Alone Self-Attention in Vision Models](https://arxiv.org/pdf/1906.05909.pdf)

### Spatial extent
Large extent (9x9) give better results than small extent (3x3).

### Positional information

Relative positional information is better than having non or absolute one.



# Transformer













**class activation maps**
**activation atlases**
# 

TODO: convo + self attention
self attention standalone




---
Status: #postpone

Tags: #attention 

References: 

- [**# Self-Attention In Computer Vision**](https://towardsdatascience.com/self-attention-in-computer-vision-2782727021f6)
- [# Attention? Attention!](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html#soft-vs-hard-attention)
- [# Attention Guided Convolutional Neural Network for Thorax Disease Classification](https://arxiv.org/abs/1801.09927)
- [# Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)
- [# Self-attention building blocks for computer vision applications in PyTorch](https://github.com/The-AI-Summer/self-attention-cv)
- [# Transformer Neural Networks - EXPLAINED! (Attention is all you need)](https://www.youtube.com/watch?v=TQQlZhbC5ps)
- [# Attention in Neural Networks  - EXPLAINED!](https://www.youtube.com/watch?v=W2rWgXJBZhU)
- [# Attention Is All You Need - Yannic Kilcher](https://www.youtube.com/watch?v=iDulhoQ2pro)






- [# Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [# Prime Sample Attention in Object Detection](https://arxiv.org/abs/1904.04821)
- [# Attention Guided Convolutional Neural Network for Thorax Disease Classification](https://arxiv.org/abs/1801.09927)
- [# Exploring Self-attention for Image Recognition](https://arxiv.org/abs/2004.13621)
- [# Attentional Network for Visual Object Detection](https://arxiv.org/abs/1702.01478)

Related:
- [[01_Experience/AI_notes/Model_architecture/Transformer]]