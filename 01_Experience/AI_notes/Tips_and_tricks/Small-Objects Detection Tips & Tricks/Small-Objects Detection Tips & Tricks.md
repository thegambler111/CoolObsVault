# Small-Objects Detection Tips & Tricks
- Anchor Boxes
	- Use anchor boxes with size/ratio close to target boxes

- Image Size
	- Use the highest image resolution your GPU can afford.
	- Use progressive resizing: Train with small size image, and gradually increase size
	- Use tiling: Train image patches and combine
	- Use recommended image size for each model

- Data Augmentation
	- Oversample images with small boxes
	- Use data augmentation: select image transforms close to your use case
	- Use Copy & Paste boxes data augmentation
	- Use mosaic data augmentation

- Models
	- Use larger models. They outperform smaller ones
	- Use Focal Loss such as RetinaNet and EfficientDet
	- Try models that leverage multi level prediction by detecting small and large boxes at # levels (e.g., FCOS)
	- Turn an object detection task into a segmentation task. The latter will improve the small object detection task 

- Dataset 
	- Label well your dataset
	- Increase your dataset size before switching to another model
	- Increase the batch size
	- Dataset size depend on whether you start training with pretrained models/backbones or from scratch
 
- Inference
	- In inference, use the same image size as the one you train your model with

# 

---
- Status: #done 

- Tags: #machine_learning #tips_and_tricks #object_detection 

- References:
	- [Source](https://twitter.com/ai_fast_track/status/1407333442145206280)

- Related:
	- 
