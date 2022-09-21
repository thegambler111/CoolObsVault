# TLDR:
1. Scroll through data as much as possible and try to find patterns
2. Find a good benchmark (your own accuracy is fine)
3. (Empty in source)
4. Setup simple pipelines
5. Overfit the model
6. Generalize the model
7. Repeat step 5 and 6 until no more improvement in validation



# 7 steps to train any computer vision model

## 1. Immerse yourself in the data
- You should scroll through as many images as possible and try to find patterns.
- While you're scrolling, ask yourself questions like: 
	- Does spatial position matter?
	- Are there any data issues (i.e. duplicates)
	- How noisy is the target?
	- Is the target ever occluded?


## 2. Create a human baseline
- While you're scrolling through images, try to get a gauge of your own accuracy.
- A human benchmark is much better than a naive one, like the target mean.
- You can also use Kaggle leaderboard as a benchmark


## 4. Set up your pipeline
- Start off with an extremely minimal pipeline:
	- Fixed random seed
	- No augmentation
	- Small pretrained model (resnet18, efficientnet-b0)
	- Adam optimizer with no scheduler
	- Implement logging
	- Sanity check your metric

- Set up some QA steps, for example:
	- Set inputs to all zeros and compare loss to normal run
	- Visualize some samples right before they enter your model
	- Ensure training loss is decreasing


## 5. Overfit
- Try to get your training error as low as possible:
	- Increases to model size
	- Increased image size
	- Bigger output head
- **Make sure you only try one new thing at a time!**


## 6. Reduce overfitting

- Overfit model ✅ -> Generalize model

- I usually follow these 4 steps, in order:
	1. Get more data
	2. Augmentation
	3. Regularization (i.e. dropout, weight decay)
	4. Smaller architecture

- Here are some situational tricks:
	- Crop out as much background as possible
	- Decrease batch size
	- Add a learning rate scheduler (I do this very often)
- These tricks are helpful, but not as much as the 4 steps above


## 7. Repeat steps 5 + 6
- Your goal now should be to keep trying to overfit and then reduce that overfitting.
- You can stop when you run out of time or when you're no longer seeing improvements in validation accuracy when you regularize.



# 

---
- Status: #done 

- Tags: #machine_learning #model_training #tips_and_tricks 

- References:
	- [Source](https://twitter.com/marktenenholtz/status/1493933208525631488)

- Related:
	- 
