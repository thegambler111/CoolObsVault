# TLDR
 ![[Images/AI_note_images/Transformer_architecture.png]]
 
|                                                                         |                                                                  |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------- |
| ![[Images/AI_note_images/Transformer_scaled_dot_product_attention.png]] | ![[Images/AI_note_images/Transformer_muilti_head_attention.png]] |
|                                                                         |                                                                  |

- The input and previous output is vectorized and combined with positional information.
- Each then go though a different multi-headed attention layer to get vector representing attention (or contextual relationship) of each word to other words in the same sentence.
- At Encoder-Decoder multi-headed attention, the relationship between output and input are learned.
- The result vector go through final linear and softmax layer to get the output word.

# Problem with RNN
- Reference window:
	- Normal RNN has a small reference window
	- LSTM has a bigger reference window but is still limited
	- Attention mechanism in theory has an infinite reference window
- Training speed:
	- Normal RNN is slow, LSTM is more complex, therefore, is even slower.
	- One reason is that input data needs to be passed in sequentially one after another which does not make use of GPU's parallel computation power.

# Transformer

![[Images/AI_note_images/Transformer_architecture.png]]

## Pass 1:

#### Word vectorization:
- Input embedding: 
	- This embedding space maps each word to a vector
	- This space is the mapping of all words where the ones with similar meaning are physically closer

=> However, the same word in different part of the sentence may have different meanings

- Positional encoding: 
	- This vector contains information on distance between words and the sentence.
	$${
	\begin{align}
	PE(pos, 2i+1) &= cos(\frac{pos}{10000^{2i/d_{model}}}) \\
	PE(pos, 2i) &= sin(\frac{pos}{10000^{2i/d_{model}}})
	\end{align}
	}$$
	- Apply positional encoding to input vectors => word vectors with positional information (or context)


### Encoder block:
|                                                                         |                                                                  |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------- |
| ![[Images/AI_note_images/Transformer_scaled_dot_product_attention.png]] | ![[Images/AI_note_images/Transformer_muilti_head_attention.png]] |

- Multi-headed attention layer:
	- This layer create vectors representing attention (or contextual relationship) of each word to other words in the same sentence.
- Feed forward layer:
	- This feed-forward net transforms attention vectors into the form that digestible by the next block

### Decoder block:
- Masked multi-headed attention:
	- This layer generates attention vector for previous output words.
- Encoder-Decoder multi-headed attention:
	- This layer determined the relationship of all output and input words with respect to each other.
	- => Input to output words mapping happens here.
	- This layer gives attention vectors for both input and output words
- Linear layer:
	- This is another feed-forward layer to extend the vector dimensions into the numbers of words in target embedding space.
- Softmax layer:
	- Transform the vector into a probability distribution.
	- The final word is the word with highest probability

## Pass 2:

### Encoder:
- Query, Key, Value: These concepts come from retrieval systems.
	- You use a Query to search
	- The engine match your Query against a set of Keys
	- Then return best matched Value

- Multi-headed attention layer:
	- Because trios of queries, keys and values (Q, K, V) are independent of each other, therefore, we can separate them into multiple sets and compute them in parallel.
	- As Q, K, V are divided into sets, multiple attention vectors are calculated for each word then taken a weighted average to compute the final attention vector for that word.
	- **=> Multi-head attention**

### Decoder:
- Masked multi-headed attention:
	- While performing parallelization with matrix operation, we **mask** the word appearing later by change their weight to zero so the attention network cannot use them

## Pass 3:
- Multi-headed attention layer:
	- Q, K and V are calculated by feeding input into 3 linear (fully connected) layer.
	- Q, K and V are abstract vectors for every word. Each of those vectors has a corresponding weighted matrix, which are $W^Q$, $W^K$ and $W^V$
	- The attention vector $Z_i$ is calculated as: 
	$${Z_i = softmax(\frac{Q \cdot K^T}{\sqrt{Dimension\, of\, vector\, Q,\, K\, or\, V}}) \cdot V}$$
	- To get the final attention vector for a word, we concatenate all $Z_i$ with a weighted matrix $W^Z$:
	$${Z = Concat(Z_1,\ldots Z_h) \cdot W^Z}$$
	
- For every layer, we apply residual connection.

- Normalization: After every layer, we apply normalization:
	![[Images/AI_note_images/Transformer_normalization.png]]
	- Usually, we use batch normalization which smooths out the lost surface =>Easier to optimize using larger learning rate.
	- We can use layer normalization, which normalize across each feature instead of each sample for better stabilization.



# 

---
Status: #done 

Tags: #RNN #transformer 

References:
- [# Transformer Neural Networks - EXPLAINED! (Attention is all you need)](https://www.youtube.com/watch?v=TQQlZhbC5ps)
- [# More detail: Illustrated Guide to Transformers Neural Network: A step by step explanation](https://www.youtube.com/watch?v=4Bdc55j80l8)
- [# Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [# Attention Mechanism Algorithm Animated (Inside Transformer Neural Networks)](https://www.youtube.com/watch?v=lmepFoddjgQ)


Related:
- [[01_Experience/AI_notes/Model_architecture/RNN  traditional architectures]]
- [[01_Experience/AI_notes/Model_architecture/Attention Mechanism]]