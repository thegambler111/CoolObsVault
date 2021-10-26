# TLDR
![[Images/AI_note_images/RNN_traditional.gif]]

- Recurrent neural network:
	- Uses state $h^t$ to store information from all previous inputs.
	- Combine previous state $h^{t-1}$ and current input $x^t$ to calculate current state $h^t$ which in turn is used to calculate the current output.
	- All input information are learned passively.


![[Images/AI_note_images/RNN_LSTM.png]]

- LSTM:
	- Actively forget unnecessary previous information and update selected input information through gate system.
	- => Better at control memory of the network.
	- Gate system:
		- Forget gate: Forget unnecessary previous information.
		- Input gate: Select information to remember.
		- Output gate: Calculate output.

![[Images/AI_note_images/RNN_GRU.png]]

- GRU:
	- Reducing the number of gates and computation while maintaining the same function as LSTM.
	- => Slightly faster to train.




# Recurrent neural network
![[Images/AI_note_images/RNN_traditional.gif]]
![[Images/AI_note_images/RNN_state.png]]
- Denote $h^t$ is the current state of the system.
- $h^t$ represents information seen before it.
- Because $h^t$ is a fixed length vector and there can be any number of previous inputs, $h^t$ cannot remember every inputs.
- Assume that there is a function $f$ determining the next state of the system: $$h^{t+1} = f(h^t,\, x^{t+1};\, \theta)$$
- => What is retained and what is forgotten is determined by $f$

![[Images/AI_note_images/RNN_math.png]]

- $a^t$ represents information from current input ($x^t$) and pass input seen before ($h^{t-1}$): $$a^t = W \cdot h^{t-1}+U \cdot x^t+b_u$$
- Next hidden layer $h^t$ is calculated using non-linear activation function (here use $tanh$): $$h^t = tanh(a^t)$$
- Output $o^t$ is computed by: $$o^t = softmax(V \cdot h^t + b_v)$$
- Lost at a time step is: $$L^t = Loss(o^t, y^t)$$
- Total lost is: $$L = \sum_t L^t$$


# Tanh activation

![[Images/AI_note_images/Tanh_activation.gif]]

- The tanh function squishes values to always be between -1 and 1..
- => Ensure that the values stay between -1 and 1.
- => Avoid vanishing and exploding gradient.


# Sigmoid activation

![[Images/AI_note_images/Sigmoid_activation.gif]]

- Sigmoid function squishes values between 0 and 1.
- Any number getting multiplied by 0 is 0, causing values to disappears or be "forgotten".
- Any number multiplied by 1 is the same value therefore that value stay’s the same or is "kept".
- =>The network can learn which data is not important therefore can be forgotten or which data is important to keep.


# Traditional approach:

![[Images/AI_note_images/RNN_traditional_method.png]]

The traditional approach is suffered from vanishing gradient.
=> Early layers cannot learn.
=> Information from early words is not used for predicting the latter words.

# LSTM
![[Images/AI_note_images/RNN_LSTM_legend.png]]
![[Images/AI_note_images/RNN_LSTM.png]]

Note:
- Sigmoid function ($\sigma$) is used to decide which value to use.
- Tanh function is used to enforce the vector to [-1, 1] to prevent vanishing and exploding gradient

- Cell state: memory of the network.

![[Images/AI_note_images/RNN_LSTM_update_gate.gif]]
- Forget gate: Cell memories set to 0? $$f^t = \sigma(W^f [h^{t-1}, x^t]+b^f)$$
	- Information of previous hidden state and current input is  passed through sigmoid function:
	- Squish values to range of [0, 1]
	- Multiply with cell state: 
		- Value multiply with 0 will be 0 => Be forgotten
		- Value multiply with 1 will be the same => Be kept
	- => Learn what information to keep, what information to forget

![[Images/AI_note_images/RNN_LSTM_input_gate.gif]]
- Input gate: Cell state updated? $$i^t = \sigma(W^i [h^{t-1}, x^t]+b^i)$$
	- Information of previous hidden state and current input is passed through sigmoid function to decide which value will be update.
	- Information of previous hidden state and current input is also passed through tanh function (to squish values to range of [-1, 1]) to regulate the network. $$\overline{C}^t = tanh(W^c [h^{t-1}, x^t]+b^c)$$
	- Output from tanh and sigmoid function are multiplied together. The sigmoid output decide which information to keep for tanh output.

![[Images/AI_note_images/RNN_LSTM_cell_state.gif]]
- Update cell state: $$C^t = f^t \cdot C^{t-1} + i^t \cdot \overline{C}^t$$
	- To forget unnecessary information (dropping values), cell state is multiple by forget vector.
	- To update with new value, cell state is point-wise added by update vector.

![[Images/AI_note_images/RNN_LSTM_output_gate.gif]]
- Output gate: Current cell state information visible? $$o^t = \sigma(W^o [h^{t-1}, x^t]+b^o)$$
	- Information of previous hidden state and current input is passed through sigmoid function to decide which hidden value will be use.
	- New cell state is pass through tanh function.
	- We multiply tanh output and sigmoid output to decide which information new hidden state should carry.
	- The output will be the current hidden state. $$h^t = tanh(C^t) x\times o^t$$
- The new cell state and hidden state are carried over to the next time step.

![[Images/AI_note_images/RNN_LSTM_sudo_code.png]]


# GRU
![[Images/AI_note_images/RNN_GRU.png]]

- GRU uses hidden state to transfer information.
- Update gate = LSTM update gate + forget gate.
	- This gate decides which information to throw away and which new information to add.
- Reset gate: decide how much pass information to forget.
- GRU are a little faster to train compared to LSTM.



# 

---
Status: #done 

Tags: #RNN #LSTM #GRU #key_knowledge

References:
- [Video # Illustrated Guide to LSTM's and GRU's: A step by step explanation](https://www.youtube.com/watch?v=8HyCNIVRbSU)
- [# Illustrated Guide to LSTM’s and GRU’s: A step by step explanation](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)
- [# Recurrent Neural Networks - EXPLAINED!](https://www.youtube.com/watch?v=yZv_yRgOvMg)
- [# LSTM Networks - EXPLAINED!](https://www.youtube.com/watch?v=QciIcRxJvsM)
- [# Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

Related:
