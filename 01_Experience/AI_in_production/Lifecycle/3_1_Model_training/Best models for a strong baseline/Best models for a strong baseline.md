# TLDR

| Data        | Baseline Model      | 
| ----------- | ------------------- |
| Tabular     | XGBoost/LightGBM/RF |
| Time series | XGBoost/LightGBM/RF |
| Image       | ResNet/EffNet       |
| Text        | RoBERTa             |
| Audio       | ResNet/EffNet       |

# Tabular data
- Tabular data: XGBoost/LightGBM/RF
	- To everyone else, ensemble tree-based models are by far the best plug-and-play tabular models.
	- Neural networks can beat them sometimes, but if GBT models are easy-mode, NNs are hard-mode.


# Time series data
- Time series data: XGBoost/LightGBM/RF
	- That's right -- the best time series models are ones not even built for it.
	- Instead, set a prediction horizon and create time series features for your model (i.e. rolling/lagged features).
	- Then, treat it like any other tabular data!


# Image data
- Image data: ResNet/EffNet
	- ResNet18 and EffNet-B0 are small, quick models that are effective for nearly any type of image data.
	- Once you've squeezed all the juice out of those, you can scale up to their bigger versions and almost always get better accuracy.

# Text data

- Text data: RoBERTa
	- I love starting text problems with a DistilRoBERTa model.
	- Sometimes, the combination of speed and accuracy is exactly what you need.
	- If not, it's the same as above -- scale up to the bigger versions and you'll get that juice accuracy you're looking for.


# Audio data
- Audio data: ResNet/EffNet
	- That's right -- image models for audio data.
	- My favorite way of starting audio problems is converting the audio to a spectrogram and throwing an image model at it.
	- Give it a shot!


# Extra notes
- Regression task
	- Same as classification as far as model architecture

- Biomolecules
	- Custom transformers and graph NNs seem to be the way to go


# 

---
- Status: #done 

- Tags: #model_training #machine_learning #tips_and_tricks 

- References:
	- [Source](https://twitter.com/marktenenholtz/status/1501905740813848582)

- Related:
	- 
