# Tip #1
- When building models with the Functional API (https://keras.io/guides/functional_api/), you can use an intermediate output as entry point to define a new Model.
- This is especially useful to create pairs of models where one includes preprocessing (e.g. for inference), and one does not.


![[01_Experience/AI_notes/Keras/Various Keras tips/1.png]]



# Tip #2
- Once you have a Keras model and a Dataset, you can train on any hardware -- a CPU, a single GPU, multiple GPUs, a TPU. You just need to create and compile your model inside a tf.distribute scope of your choice.


![[01_Experience/AI_notes/Keras/Various Keras tips/2_1.png]]
![[01_Experience/AI_notes/Keras/Various Keras tips/2_2.png]]

# Tip #3
- Mixed precision is a way to train models significantly faster (~2x) on modern GPUs at virtually no loss of accuracy. It consists of using a lower precision (float16) for forward pass computation while keeping model state in float32. You can enable it in Keras in 1 line.


![[01_Experience/AI_notes/Keras/Various Keras tips/3.png]]


# Tip #4 
- "step fusing" consists of running multiple steps of model training back-to-back on an accelerator device (a GPU or TPU) without syncing with the host CPU RAM. It's a great way to get to near-100% device utilization without having to increase your batch size.

![[01_Experience/AI_notes/Keras/Various Keras tips/4.png]]

# Tip #5:
- XLA is a linear algebra compiler capable of automatically fusing & optimizing TensorFlow operations, which can lead to significant speed ups for many model architecture / device combinations.
- You can compile your Keras training loop to XLA via `jit_compile=True`.

![[01_Experience/AI_notes/Keras/Various Keras tips/5.png]]




# Tip #6
- Use `set_random_seed()` to make your workflow deterministic. This will simultaneously seed Python's `random` module, NumPy, and TF/Keras.
- If you need CUDA op determinism, then also use `tf.config.experimental.enable_op_determinism()`, which comes at a performance cost.

![[01_Experience/AI_notes/Keras/Various Keras tips/6.png]]


# Tip #7
- Use `keras.utils.plot_model(model)` and `model.summary()` to get succinct visualizations of the contents and structure of your model.

![[01_Experience/AI_notes/Keras/Various Keras tips/7.png]]







# 

---
- Status: #done 

- Tags: #keras #tips_and_tricks 

- References:
	- [Source](https://twitter.com/fchollet/status/1502453560805449733)

- Related:
	- 
