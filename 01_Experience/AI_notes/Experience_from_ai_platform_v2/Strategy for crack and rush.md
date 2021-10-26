# Strategies

## Segment only the crack and rush
?

## Segment container first (concrete or metal)
?

## Depth estimation

- Aim: Separate focused object and background
- Result:
	- Current solutions do not give clear enough result to separate objects
	- Depend on the background, distance between object and background, lighting, ...
- => Not feasible


## Attention model

- Aim: Guide the model to focus on crack and rust
- Result:
	- Attention models are different from imagination
	- Attention mechanism is more of implementation of transformer to computer vision tasks which is calculating relationship between current pixel and all other pixel of the image (adding global information to the network) instead of just 3x3 region like in convolutional neural network.
	- Have not find to directly guide model to focus on a specific region
- => Still useful but not what we are looking for


## Anomaly detection

- Aim: Apply other anomaly solutions for our tasks
- Result:
	- Anomaly detection solution is either:
		- Classification
		- A combination of segmentation and synthesis:
			- Segment the image
			- Use GAN to recreate image from segmentation result
			- Compare synthetic image and initial image, the difference is the anomaly (which segmentation model did not learn)
	- Most datasets are object-centric 
- => May work but to expensive to train and run.


## Use GAN to add crack and rust to good images then classify them

- Aim: Use GAN to add crack and rust to good images then classify good images and synthetic ones
- Result: ?


## Foreground segmentation or background subtraction

- Aim: Separate foreground and background, use only foreground to segmentation
- Result: 
	- This solution is used in video, not static image
- => Not what we are looking for. 😀 😹 👋👌🙌

	





# 

---
Status: #done 

Tags: #planning #computer_vision #segmentation #anomaly_detection

References:
- 

Related:
- [[02_Raw/AI_notes/Model Architecture/GAN in anomaly detection]]
- [[01_Experience/AI_notes/Model_architecture/Attention Mechanism]]