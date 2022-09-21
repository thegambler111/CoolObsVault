# RPN
- From paper:
	- We re-scale the images such that their shorter side is s = 600 pixels.
	- On the re-scaled images, the total stride for both ZF and VGG nets on the last convolutional layer is 16 pixels, and thus is ∼10 pixels on a typical PASCAL image before resizing (∼500×375).
	- For anchors, we use 3 scales with box areas of 128^2, 256^2, and 512^2 pixels, and 3 aspect ratios of 1:1, 1:2, and 2:1
	- During training, we ignore all cross-boundary anchors so they do not contribute to the loss. For a typical 1000 × 600 image, there will be roughly 20000 (≈ 60 × 40 × 9 (1000/16 and 600/16 with 16 = stride and 9 is number of anchor sizes) anchors in total. With the cross-boundary anchors ignored, there are about 6000 anchors per image for training.
	- Some RPN proposals highly overlap with each other. To reduce redundancy, we adopt non-maximum suppression (NMS) on the proposal regions based on their cls scores. We fix the IoU threshold for NMS at 0.7, which leaves us about 2000 proposal regions per image.



# Fix runtime error for Faster-RCNN in Keras
- ValueError: Shape must be rank 1 but is rank 0 for 'bn_conv1/Reshape_4' [1,1,1,64],[]

- Change in lib "lib/python3.6/site-packages/keras/backend/tensorflow_backend.py":
	- tf.reshape(smt, (-1)) -> tf.reshape(smt, [-1])

# 

---
- Status: #done 

- Tags: #CNN #model_architecture 

- References:
	- 

- Related:
	- 