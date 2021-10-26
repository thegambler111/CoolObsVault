# TLDR
[# Attention in Neural Networks](https://www.youtube.com/watch?v=W2rWgXJBZhU)

![[Images/AI_note_images/Attention_image_captioning_attention.png]]

![[Images/AI_note_images/Attention_soft_attention_unit_2.png]]

- $y_i$ is an internal feature representing a sub region of the image.
- $C$ is context representing everything the RNN has output until now.
- $s_i$ is probability of the sub region contribute to current output (amount of attention output $Z$ pay to sub region $y_i$).
- Combining sub region feature $y_i$ and context $C$, we compute the contribution $s_i$ of sub region $y_i$ to final output $Z$.

# Attention

![[Images/AI_note_images/Attention_frisbee.png]]

Let use image captioning as an example:

![[Images/AI_note_images/Attention_traditional_encoder_decoder.png]]

In traditional way, there are 2 steps:
1. Encode the image into into an internal vector representation h using a convolutional neural network
2. Decode h into words vectors using a recurrent neural network

The problem with this approach is when generating a single word of the caption, the LSTM look at the entire image representation h every time.

![[Images/AI_note_images/Attention_image_captioning.png]]
The image above is a high-level diagram of attention.

To solve the traditional way's problem, we create n different non-overlapping sub regions of the image, hence $h_i$ would be the internal feature representation used to generate the $i^{th}$ word. ($h_i$ is not necessarily the representation of the $i^{th}$ region of the original image.)

Now, when generating the caption, for every word, the decoder only look at a specific region of the image => more accurate description

![[Images/AI_note_images/Attention_image_captioning_attention.png]]
How does it decides the regions to consider?

- An attention unit considers all sub regions $y$ and contexts $C$ as its input. 
- Then, it outputs the weighted arithmetic mean $z$ of these regions which is the inner product of actual region values and their probabilities. 
- These weights and probabilities are determined by the context. 
- Context represents everything the recurrent network output until now.

![[Images/AI_note_images/Attention_soft_attention_unit.png]]

We apply input regions $y_i$ and contexts $C$ to the weight $W$ which constitutes (be apart of) learnable parameters of the attention units as:

$${
m_i = \tanh(y_i W_{y_i} + C W_C)
}$$

![[Images/AI_note_images/Attention_soft_regions_of_interest.png]]

The $\tanh$ activation make very high value close each other and to 1. On the other hand, very low value will be close to each other and close to -1.

=> Smoother choice of regions of interest within each sub region

Then, we calculate the probability $s_i$ for each regions using softmax function:

$${
s_i = \frac{e^{m_i}}{\sum_n e^{m_n}}
}$$

Finally, we take the inner product of probability $s$ and sub region $y$ to calculate the final output Z of relevant regions of the entire image.

$${
z = \sum_n s_n y_n
}$$

# Soft attention
The above example is a soft attention.

The main relevant region $C$ consists of different parts of different  sub regions $y$.

Soft attention is **deterministic**, the result $z$ is always the same.

# Hard attention

![[Images/AI_note_images/Attention_hard_attention_unit.png]]

The main relevant region $C$ consists of only **one** sub regions $y_i$ randomly chosen base on probability $s_i$.

![[Images/AI_note_images/Attention_hard_regions_of_interest.png]]

Hard attention is **stochastic**, the result $z$ may change each time it is calculated.

# Attention short coming

According to this paper [Attention is not all you need: pure attention loses rank doubly exponentially with depth](https://arxiv.org/abs/2103.03404), pure attention suffers from exponential rank losing.

However, by using combination of skip connections (residual connection) and multi-layer perceptrons (which are implemented on transformer), the short coming of pure attention network is tent to.

On the other hand, layer normalization plays no role.



# 

---
Status: #done 

Tags: #attention #transformer

References:
- [# Attention in Neural Networks](https://www.youtube.com/watch?v=W2rWgXJBZhU)
- [# Attention Is All You Need - Yannic Kilcher](https://www.youtube.com/watch?v=iDulhoQ2pro)



- [Attention is not all you need: pure attention loses rank doubly exponentially with depth](https://arxiv.org/abs/2103.03404)

Related:
