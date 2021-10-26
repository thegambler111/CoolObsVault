# TLDR
- Neural network training is usually not fully understood, and hard to notice errors.
- How one can avoid making model training errors altogether (or fix them very fast):
	- Build things from simple to complex
	- Thoroughly inspecting the data:
		- Understand the distribution and look for patterns of the data.
		- Select model architecture from data
	- Set up a full training + evaluation skeleton:
		- Experiment with some basic models
		- Try basic things only (no fancy here, keep it for later step)
		- Reduce randomness
		- Verify things thoroughly
		- Visualize data and prediction
	- Find a good enough to overfit model:
		- Try models from the most related paper
		- Adding complexity one at a time
		- Use default values with selection
	- Regularize the overfit model:
		- Get more data (real or augmented)
		- Use pretrained weight
		- Try fancy stuffs here
		- Verify the model improvement using visualization
	- Hyper-parameter optimization
	- Using ensembles.
	- Let model train more even if it seems to converge
- Read [[#Additional content]]

# Most common neural network mistakes: 
- You didn't try to overfit a single batch first.
- You forgot to toggle train/eval mode for the net
- You forgot to .zero\_grad() (in pytorch) before .backward(). 
- You passed softmaxed outputs to a loss that expects raw logits.
- You didn't use "bias=False" for your Linear/Conv2d layer when using BatchNorm, or conversely forget to include it for the output layer .This one won't make you silently fail, but they are spurious parameters
- Thinking view() and permute() are the same thing (& incorrectly using view)


# 2 problems when training neural network 


## Neural network training is a leaky abstraction

- You usually learn new techniques in programming through abstractions (simple explanations) which hides complexity (details) and let you create apps without fully understanding the technology which in turn make your app less reliable.
- Neural network training is not an exception. You learn backpropagation as a leaky abstraction which makes you be much less effective at building and debugging neural networks


## Neural net training fails silently

- Syntactical error will often get some kind of an exception and it's often possible to create unit tests for a certain functionality.
- However, in training neural nets, everything could be correct syntactically, but the whole thing isn't arranged properly, and it's really hard to tell.
- The "possible error surface" is large, logical (as opposed to syntactic), and very tricky to unit test. Most of the time it will train but silently work a bit worse.
- For example:
	- Perhaps you forgot to flip your labels when you left-right flipped the image during data augmentation. Your net can still (shockingly) work pretty well because your network can internally learn to detect flipped images and then it left-right flips its predictions.
	- Or maybe your autoregressive model accidentally takes the thing it’s trying to predict as an input due to an off-by-one bug.
	- Or you tried to clip your gradients but instead clipped the loss, causing the outlier examples to be ignored during training.
	- Or you initialized your weights from a pretrained checkpoint but didn’t use the original mean.
	- Or you just screwed up the settings for regularization strengths, learning rate, its decay rate, model size, etc. Therefore, your misconfigured neural net will throw exceptions only if you’re lucky.
- => The qualities correlate most strongly to success in deep learning are **patience** and **attention to detail**.

# The recipe

- We will build things from simple to complex:
	- At every step of the way, we make concrete hypotheses about what will happen
	- then either validate them with an experiment 
	- or investigate until we find some issue.
-  We try very hard to prevent introducing of a lot of "unverified" complexity at once.


## Become one with the data

- What to do next: thoroughly inspecting the data.
- The aim is to understand the distribution and look for patterns of the data 
	- => duplicates, corrupted files, imbalances and biases
- From classifying the data to selecting the model architecture:
	- Are local features enough or we still need global context?
	- How much variation is there and what form does it take?
	- What variation is spurious and could be preprocessed out?
	- Does spatial position matter or do we want to average pool it out?
	- How much does detail matter and how far could we afford to downsample the images?
	- How noisy are the labels?
- We can understand model predictions from the data. If your network is giving you some predictions that doesn't seem consistent with what you've seen in the data, something is off.
- Once you get a qualitative sense of the data, you can visualize the **distributions** and the **outliers** (along any axis) of data attributes (e.g. type of label, size of annotations, number of annotations, etc.)
	- The outliers especially almost always uncover some bugs in data quality or preprocessing.

## Set up the end-to-end training/evaluation skeleton + get dumb baselines

- What we have: understanding of our data
- What to do next: 
	- Set up a full training + evaluation skeleton
	- Gain trust in its correctness via a series of experiments.
- It is best to pick some simple model that you couldn't possibly have screwed up somehow - e.g. a linear classifier, or a very tiny ConvNet. We'll want to:
	- Train it
	- Visualize the losses, any other metrics (e.g. accuracy), model predictions
	- Perform a series of ablation experiments with explicit hypotheses along the way.
- Tips & tricks for this stage:
	- Fix random seed (removes a factor of variation).
	- Simplify. Make sure to disable any unnecessary fanciness (e.g. data augmentation).
	- Add significant digits (more number after comma) to your eval.
	- Verify loss at initiation. Verify that your loss starts at the correct loss value ❓(e.g. $-\log{(1/n\_classes)}$ for a final layer softmax).
	- Initialize well. Initialize the final layer weights correctly ❓(should do more research on this topic).
	- Human baseline. Monitor metrics other than loss that are human interpretable and checkable (e.g. accuracy)
	- Annotate the test data twice and for each example treat one annotation as prediction and the second as ground truth.
	- ❓ Input-independent baseline (baseline is a very basic model). Train an input-independent baseline, (e.g. easiest is to just set all your inputs to zero). This should perform worse than when you actually plug in your data without zeroing it out. Does it? i.e. does your model learn to extract any information out of the input at all?
	- Overfit **one batch**. 
		- Overfit a single batch of only a few examples (e.g. as little as two) by increasing the capacity of the baseline.
		- Reaching the lowest achievable loss (e.g. zero)
		- Verify label and prediction at minimum loss using visualization
	- Verify decreasing training loss.
		- Baseline model should be underfitting on dataset.
		- Increase model capacity a bit. Does your training loss go down?
	- Visualize just before the net. Visualize the data and labels after all preprocessing (e.g. augmentation) and right before feeding into the model (e.g. $output=model(data)$)
	- Visualize prediction dynamics on a fixed test batch during training.
		- If the model wiggles too much in some way, it is unstable.
		- Very low or very high learning rates are also easily noticeable in the amount of jitter.
	- Use backprop to chart dependencies.
		- Gradients give you information about what depends on what in your network
		-  One way to debug all the complicated operations is to set the loss to be something trivial like the sum of all outputs of example **i**, run the backward pass all the way to the input, and ensure that you get a non-zero gradient only on the i-th input.
	- Generalize a special case.
		- Write a very specific function to what I’m doing right now, get that to work.
		- Then generalize it later making sure that I get the same result.


## Overfit

- What we have:
	- Good understanding of the dataset
	- A full training + evaluation pipeline working.
	- A metric that we trust.
	- Performance for an input-independent baseline
	- Performance of a few dumb baselines that we had to beat
	- Rough sense of human performance which we hope to reach
- What to do next: Find a good model in 2 steps
	- Get a model large enough to overfit (focus of training loss)
	- Regularize it appropriately (give up some training loss to improve validation loss)
- Tips & tricks for this stage:
	- Picking the model.
		- Start from find the most related paper and copy their simplest architecture that archives good performance.
		- You can custom the model later
	- Adam is safe, commonly use with a learning rate of 3e-4. Or you can follow what the most related papers do.
	- Complexify only one at a time. Trying things one by one and every time ensure that you get a performance boost you’d expect.
	- Do not trust learning rate decay defaults. In my own work I always disable learning rate decays entirely (I use a constant LR) and tune this all the way at the very end.

## Regularize

- What we have: a large model fitting at least the training set.
- What to do next: regularize it and gain some validation accuracy by giving up some training accuracy.
- Tips & tricks for this stage:
	- Get more data:
		- The by far best and preferred way to regularize a model in any practical setting is to add more real training data.
		- The other would be ensembles (if you can afford them), but that tops out after ~5 models.
	- Data augmentation. The next best thing to real data is half-fake data - try out more aggressive data augmentation.
	- Creative augmentation (fake data). For example:
		- [Domain randomization](https://openai.com/blog/learning-dexterity/)
		- Use of [simulation](http://vladlen.info/publications/playing-data-ground-truth-computer-games/)
		- Clever [hybrids](https://arxiv.org/abs/1708.01642) such as inserting (potentially simulated) data into scenes
		- GAN.
	- Pretrain. It rarely ever hurts to use a pretrained network if you can, even if you have enough data.
	- Stick with supervised learning. Do not get over-excited about unsupervised pretraining.
	- Smaller input dimensionality.
		- Remove features that may contain spurious signal (hard to notice or easily mistaken with something else)
		- If low-level details don’t matter much, try to reduce input size.
	- Smaller model size. Try to reduce model complexity using domain knowledge constraints.
	- Decrease the batch size. ❓ Due to the normalization inside batch norm smaller batch sizes somewhat correspond to stronger regularization. This is because the batch empirical mean/std are more approximate versions of the full mean/std so the scale & offset "wiggles" your batch around more.
	- Add dropout. Use dropout2d (spatial dropout) for ConvNets. Use this sparingly/carefully because dropout [does not seem to play nice](https://arxiv.org/abs/1801.05134) with batch normalization.
	- Weight decay. Increase the weight decay penalty.
	- Early stopping.
	- Try a larger model. I mention this last and only after early stopping but I've found a few times in the past that larger models will of course overfit much more eventually, but their "early stopped" performance can often be much better than that of smaller models.
-  To gain additional confidence of your model:
	-  Visualize the network's first-layer weights and ensure you get nice edges that make sense.
	-  Visualize the activations result to ensure that there is no odd artifacts.


## Tune

- What to do next: find architectures that achieve low validation loss on our dataset
- Tips & tricks for this stage:
	- Random over grid search (find the optimal hyperparameters).
		- [[01_Experience/AI_notes/Tips_and_tricks/Hyperparameter - Grid search vs random search | Grid search vs random search]]
		- It is [best to use random search instead](http://jmlr.csail.mit.edu/papers/volume13/bergstra12a/bergstra12a.pdf).
		- Intuitively, this is because neural nets are often much more sensitive to some parameters than others.
	- Hyper-parameter optimization. There is a large number of fancy bayesian hyper-parameter optimization toolboxes.


## Squeeze out the juice

- What we have: the best types of architectures and hyper-parameters
- What to do next: squeeze out the last pieces of juice
- Tips & tricks for this stage:
	- Ensembles.
		- Model ensembles is computational expensive but has a high chance to improve the accuracy.
		- To reduce computation, distill your ensemble into a network using 
	- Leave it training. When it seems like the validation loss stop decreasing, keep training (instead of early stopping), the model may improve in a later epoch.


# Conclusion

After all those step you now have:
- A deep understanding of the technology, the dataset and the problem.
- The entire training/evaluation infrastructure set up.
- High confidence in model accuracy.
- Increasingly complex models explored.
- Performance improvements in ways you've predicted.


# Additional content

- Do not forget to create document on how to reproduce the results in significant models.




#

---
Status: #done

Tags: #machine_learning #model_training #model_evaluation #model_optimization #production #dataset 

References:
- [Source](http://karpathy.github.io/2019/04/25/recipe/)
- [# Understanding the Disharmony between Dropout and Batch Normalization by Variance Shift](https://arxiv.org/abs/1801.05134)

Related: 
- [[01_Experience/AI_notes/Tips_and_tricks/Hyperparameter - Grid search vs random search]]
- [[01_Experience/AI_notes/Basic_knowledge/Backpropagation]]
