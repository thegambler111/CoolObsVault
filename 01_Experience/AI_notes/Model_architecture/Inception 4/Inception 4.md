# Architecture:

- The goal of inception-v4 is to make the modules more uniform.
- Architecture:

![[01_Experience/AI_notes/Model_architecture/Inception 4/Architechture.png]]



# Stem layer:
- Inception-v4 apply efficient grid size reduction technique to the stem layer.
- Stem from inception-v1 and stem from inception-v4:

![[01_Experience/AI_notes/Model_architecture/Inception 4/Stem.png]]

# Three main inception modules (similar to inception-v3):

- Inception Module A:
![[01_Experience/AI_notes/Model_architecture/Inception 4/Module_A.png]]

- Inception Module B:
![[01_Experience/AI_notes/Model_architecture/Inception 4/Module_B.png]]

- Inception Module C:
![[01_Experience/AI_notes/Model_architecture/Inception 4/Module_C.png]]


# Reduction modules:
- Reduction modules (are used to change the width and height of the grid):

- Reduction modules A and B:
![[01_Experience/AI_notes/Model_architecture/Inception 4/Reduction_module_A_and_B.png]]



# 

---
- Status: #done 

- Tags: #CNN #model_architecture 

- References:
	- [Source](https://towardsdatascience.com/review-inception-v4-evolved-from-googlenet-merged-with-resnet-idea-image-classification-5e8c339d18bc)
	- [Comparing Inception versions](https://towardsdatascience.com/a-simple-guide-to-the-versions-of-the-inception-network-7fc52b863202)

- Related:
	- 