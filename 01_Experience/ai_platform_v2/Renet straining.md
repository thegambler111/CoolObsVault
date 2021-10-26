# How to run:

- [Source training file](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py)
- To start training, after modify all the parameters, simply type:
```python
python train.py
```

# Code explain:

## Basic config:
- [basic_config](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L114-127)
- Detail:

| Field                  | Explain                                                                                      |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| images_root            | Root data folder                                                                             |
| save_model_folder      | Where to save all outputs: checkpoint, final model, log,...                                  |
| save_model_dir         | Name of the final model                                                                      |
| checkpoint_dir         | name of the checkpoint file                                                                  |
| batch_size             | Training batch size, default = 16                                                            |
| learning_rate          | Learning rate, default = 1e-4                                                                |
| n_epochs               | Number of training epochs, dafault = 350                                                     |
| early_stop_epoch_limit | Stop training after number of not improving epochs, default = 350                            |
| log_name               | Name of log file                                                                             |
| lr_decrease            | Amount of learning rate decrease after lr_step: new_lr = old_lr * lr_decrease, default = 0.1 |
| lr_step                | Number of epochs between each time lr decrease, default = 10                                 |
| weight_decay           | Weight decay, default = 0.3                                                                  | 




## Root data folder:
- [Declare root data folder](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L40)
- Data folder structure:
	- image_root
		- folder_name can contains any number of labels and labels are separated by '+'
		- folder_name = label_1+label_2
			- all images with the same labels: label_1 and label_2


## Image augmentation
- [Get image augmentation](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L51)
- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/data.py#L17-47)
- Detail:

| Augmentation          | Explanation                                                  |
| -------------------- | ------------------------------------------------------------- |
| RandomRotation       | Rotate image ± x degrees, default = 15                        |
| RandomHorizontalFlip | Randomly flip image horizontally                              |
| Resize               | Resize image into 224x224 (based on Resnet weight)            |
| ToTensor             | Normalize image into [0,1] and transform into tensor          |
| Normalize            | Normalize image again based on default Imagenet normalization | 

- No augmentation for val and test set
	- However, Resize, ToTensor, and Normalize must be used for model to run correctly on any dataset

## Create dataloader

- [Create dataloader](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L53-54)
- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/data.py#L50-83)
- Some information:
	- num_worker is to increase the time to load image from RAM -> GPU, set to 0 if not used
	- pin_memory -> Load image to GPU faster, [more info here](https://discuss.pytorch.org/t/when-to-set-pin-memory-to-true/19723)


## Load model

- [Load model](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L58)
- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/model.py#L34-62)
- Some details:
	- freeze_extractor: To freeze all the layers, except the last ones
	- model.fc: Replace last layers

## Declare loss function and optimizer
- [Declare loss function and optimizer](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L68-71)
- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L13-28)
- Some details:
	- BCEWithLogitsLoss: Used for multi-label, each label will be score separately
	- Adam: The famous optimizer
	- lr_scheduler.StepLR: Change lr by multiply with a number after some epochs


## Train model
- [Train model](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L76-88)
- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L31-271)
- Details:
	- [Weight decay after calculate losses on all parameter and before update parameter](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L103-113)
	- [Output >= 0 means confidence score >= 0.5 (use sigmoid func)](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L121-123)
	- [**Calculate accuracy by comparing each image results with its expected labels, hence the 'dim=1'**](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L126)
	- [Save model if improved](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L205-219)
	- [Or trigger early stopping if not improved](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L220-245)
	- [Check learning rate after each epoch and apply learning rate scheduler](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/multilabel.py#L251-252)

## Save final model
- [Save final model](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/train.py#L96)
- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/multilabel_cleaned_classification/model.py#L65-101)
- Details:
	- Save 'fc' (fully connected) and 'state_dict' to load model
	- Save 'optimizer' and 'optimizer_state_dict' to continue training

## Note
- Remember to use **sigmoid function** on the result to get confidence score

# 



# 

---
Status: #done 

Tags: #ai_platform_v2

References:
-  

Related:
- 

