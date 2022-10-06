# Loss function based on dataset imbalance
- Here is a quick list of function losses depending on the dataset:
	- Balanced dataset: Binary Cross-entropy
	- Mildly imbalanced: Dice Loss
	- Highly imbalanced dataset: Focal loss and Focal Tversky Loss

# Loss function based on multi-label/multi-class
- Binary cross-entropy is the loss function used for multi-label classification problems.
- Categorical cross-entropy is the loss function used for multi-class classification problems.

# Triplet loss
- [Triplet loss](https://en.wikipedia.org/wiki/Triplet_loss) is helpful in [similarity learning problems](https://en.wikipedia.org/wiki/Similarity_learning) where the goal is to learn a function that measures how similar two objects are
- The Triplet loss takes the three inputs:
	- The anchor
	- A positive sample
	- A negative sample
- It minimizes the anchor—positive distance while maximizing the anchor—negative distance.

# Contrastive loss
- [Contrastive loss](https://medium.com/@maksym.bekuzarov/losses-explained-contrastive-loss-f8f57fe32246) in similarity learning problems
- This function receives two inputs and calculates whether they represent the same concept or not.

#
---
- Status: #done
- Tags: #basic_ai_knowledge
- References:
- Related:
