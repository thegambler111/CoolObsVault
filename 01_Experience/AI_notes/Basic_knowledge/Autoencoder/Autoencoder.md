# Autoencoder
- Autoencoders can be seen as *data compression algorithms* built using neural networks.
	- A network encodes (compresses) the original input into an intermediate representation
	- And another network reverses the process to get the same information back.
- The encoding process generalizes the input data.
	- Its job is to represent the dataset as compactly as possible, so the decoder can do a decent job reproducing the original data.
	- This encoding and decoding process is *lossy*
- Autoencoders are not supervised learning methods.
	- Instead, we can consider them **self-supervised** because they generate labels directly from the training data
- Any unique characteristics in the input data will never make it past the autoencoder's bottleneck.
	- =>This is a great property that we can use to *detect anomalies* in the data!


# 

---
- Status: #done

- Tags: #basic_ai_knowledge 

- References:
	- ["Introduction to autoencoders"](https://www.jeremyjordan.me/autoencoders/)

- Related:
	- 
