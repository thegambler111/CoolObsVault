# Parallel training

## Data Parallelism:
- Train multiple copies of the model on a different subset of the data.
	- Split the dataset into different segments.
	- Train a copy of the model on each segment.
	- Synchronize the updates after every iteration.


## Model Parallelism:
- Train different segments of a model on the entire dataset.

## Parallel training in framework
- If you are using TensorFlow, check:
	- Mirrored Strategy: to distribute training on the same computer with multiple GPUs.
	- Multi-Worker Mirrored Strategy: to distribute training on different computers.
- If you are using PyTorch, check "Distributed Data Parallel."

# 

---
- Status: #done

- Tags: #tips_and_tricks #model_training 

- References:
	- [Source](https://twitter.com/svpino/status/1537767024146845702)

- Related:
	- 
