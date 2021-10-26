# Part-whole hierarchies

![[Images/AI_note_images/GLOM_hierarchies.png]]

![[Images/AI_note_images/GLOM_hierarchies_on_image.png]]

- The image is divided into pixels or small patches
- At each location, there is a column, which is divided into many levels
- Each level tries to represent the location of the images at different resolution in vector form.
- For example, in a picture of a cat, at the position of the ear:
	- The very bottom would represent that this location is the fur
	- The next layer would represent that this location is part of an ear
	- The next layer would represent that this location is part of a cat head
	- The next layer would represent that this location is part of a cat
- This is a process over time where each column intuitively communicate to each other, and within a column, the layers communicate with each other.


### For one column over time:

![[Images/AI_note_images/GLOM_adjacent_levels_interaction.png]]


$${
\begin{align}
l_{t+1}^{L,x} = &\ l_{t}^{L,x} + f_{top\_down}(l_{t}^{L+1,x}) + f_{bottom\_up}(l_{t}^{L-1,x}) +\\
&Attention\_between\_elements\_of\_the\_same\_layer
\end{align}
}$$


At each discrete time and in each column separately, the embedding at a level $l_{t+1}^{L,x}$ is updated to be the weighted average of four contributions:
1. The prediction produced by the bottom-up neural net acting on the embedding at the level below at the previous time. $f_{bottom\_up}(l_{t}^{L-1,x})$
2. The prediction produced by the top-down neural net acting on the embedding at the level above at the previous time. $f_{top\_down}(l_{t}^{L+1,x})$
3. The embedding vector at the previous time step. $l_{t}^{L,x}$
4. The attention-weighted average of the embeddings at the same level in nearby columns at the previous time. => To create islands of similar elements


![[Images/AI_note_images/GLOM_embeddings_attention.png]]

Element in deep blue circle is similar to element on the left => It attends to its left element or the left element affects it more than others

=> Create islands of similar elements

Similarly, element in deep blue circle attends not so much to its right element, and not at all to the yellow arrow element.

=> Making similar elements closer to each other like a clustering algorithm.

![[Images/AI_note_images/GLOM_embeddings_tree.png]]

Parse tree is dynamically constructed base on similar elements in the same layer.

=> Element needs to **attend less** to similar elements in **different path of the parse tree.**


# Contrastive learning


# 

---
Status: #done

Tags: #machine_learning #machine_learning_idea #paper

References:
- [How to represent part-whole hierarchies in a neural network](https://arxiv.org/pdf/2102.12627.pdf)
- [# GLOM: How to represent part-whole hierarchies in a neural network (Geoff Hinton's Paper Explained)](https://www.youtube.com/watch?v=cllFzkvrYmE)

Related:
