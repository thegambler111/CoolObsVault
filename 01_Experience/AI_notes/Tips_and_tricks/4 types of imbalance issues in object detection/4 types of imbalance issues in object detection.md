# 4 types of imbalance issues
![[01_Experience/AI_notes/Tips_and_tricks/4 types of imbalance issues in object detection/4 types of imbalance issues.png]]

## Scale imbalance
- It happens when the objects have different sizes with different numbers of objects: e.g. small objects vs. big objects
- Potential Solution
	- Oversample small objects using the Copy&Paste data augmentation
	- Use higher resolution images


## Objective imbalance
- It happens when calculating a total loss (classiﬁcation and regression losses). One loss might dominate another. 
- Potential Solution
	- Use the weighted loss

## Class imbalance:
- It might be related to either:
	- Foreground-Background imbalance classes
	- Foreground-Foreground (positive) classes: e.g. Person class vs Parking Meter class in the COCO dataset
- Potential Solution:
	- For Case 1: Use the Focal Loss
	- For Case 2: Oversample under-represented classes

## Spatial imbalance:
- It refers to a set of factors related to the spatial properties of the bounding boxes such as regression penalty, location, and IoU. 
	- For example, the L2 loss penalizes more severely shifted predicted boxes than the L1 or Smooth L1 losses.
- Potential Solution:
	- Use L1 or Smooth L1 Loss
	- Use anchor-free models

# 

---
- Status: #done 

- Tags: #tips_and_tricks #object_detection

- References:
	- [Source](https://twitter.com/ai_fast_track/status/1488353683461095424)

- Related:
	- 
