# What to do with new dataset
If you are starting with machine learning / deep learning and get a new dataset to work on, either on kaggle or in real-world or just for fun. There are a few things you must always take care of to squeeze the most out of your model and make it awesome: 

- Look at the data carefully. Do **Exploratory Data Analysis** (EDA). 
- Look at the targets. See how they are distributed and what kind of problem this is.
- Choose the right metric to evaluate your models
- Split the data into folds. You can use this for cross validation or for hold out based validation
- Build a first basic model. This is going to be your baseline. 
- Now try to improve on the baseline by adding new features
- To add new features, go back to data. Look at the EDA. That's why its quite important
- When you think you have reached a limit with feature engineering, try different models
- Keep log of all the scores, features and models
- When you think you have reached a limit with different models, try **feature selection**
- Done with feature engineering and feature selection? You will realize that by following above steps, you have also chosen a few best models that work well with your data
- Now its time to do hyperparameter optimization and squeeze the last few drops from your best models
- Wrap everything in docker, so that it's reproducible.
- Build a simple API endpoint or a fully-fledged web application to serve your model and brag about it ;)

# 

---
Status: #done

Tags: #dataset #how_to #model_training #optimize #production

References:

Related:
