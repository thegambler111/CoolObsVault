# What and Why MLOps?
## ML Production System Components

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/ML Production system components.png]]

## Challenge
- Data Dependencies Cost More than Code Dependencies
	- Code is relatively static, data is always changing
- Not everyone speaks the same language
	- Not everyone uses the same tool
	- Not everyone can share the same fundamental skills
- Responsible AI
	- Explainable
	- Fairness and Unbiased
	- Reproducible
	- Privacy


## MLOps

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/MLOps.png]]


# MLOps Key Features

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/MLOps key features.png]]

## Scoping
- What is the target of project?
- Metrics to measure?
	- Accuracy, Latency, Throughput
	- Business metrics
	- More metrics: Explainable AI, etc.
- Estimate Resource and timeline?

## Data
- What relevant datasets are available?
- Is this data sufficiently accurate and reliable?
- How can stakeholders get access to this data?
- Will this data be available in real time?
- Is there a need to label some of the data with the “ground truth” that is to be predicted, or does unsupervised learning make sense? If so, how much will this cost in terms of time and resources?
- How will data be updated once the model is deployed?
- Will the use of the model itself reduce the representativeness of the data?


## Data Governance:
-  Can the selected datasets be used for this purpose?
-  What are the terms of use?
-  Are there features, such as gender, that legally cannot be used in this business context?
-  Are minority populations sufficiently well represented that the model has equivalent performances on each group?

## Feature Engineering:
-  Derivatives: Infer new information from existing information—e.g. what day of the week is this date?
-  Enrichment: Add new external information—e.g. is this day a public holiday?
-  Encoding: Present the same information differently—e.g. ordinal encoding vs one hot encoding
-  Combination: Link features together—e.g. the size of the backlog might need to be weighted by the complexity of the different items in it.
- MLOps -> Feature Stores

### Feature Stores
- Feature Store provide high throughput for batch serving or real-time serving
- Support training and serving workload.
- Avoid training/serving skew when using Feature Store as same data source for both experiment and inference.

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/Feature Stores.png]]

## Feature Selection:
- The model can become more and more expensive to compute.
- More features require more inputs and more maintenance down the line.
- More features mean a loss of some stability.
- MLOps -> Auto Feature Selection
	- Remove poor features: e.g. features with a lot of missing values
	- Train model with a small set of data to select good features

## Model development is an iterative process for:
- Finding the best modeling parameters (algorithms, hyperparameters, feature preprocessing, etc.
- Tuning some trade-off for a given training cost to fit that definition of “best”
- Finding a balance between model improvement and improved computation costs

### ML pipepline Metadata
- Saving related information of each training 

## Evaluation and Comparing Models:
- Choosing right evaluation metrics
- Choosing validation strategy: Random split, Hold out, Cross validation. 
- MLOps -> AutoML, Experiment Tracking (Versioning: Algorithm & Hyperparameter, Dataset, Result)

## Deployment:
- Distributed Server, Computing Cloud, Edge device (mobile, IoT device), Web browser.
- Metrics:
	- Latency, throughput, memory size, computational cost.
- Monitoring and maintain system.
- Concept drift and Data Drift 
- MLOps -> Monitor data drift and A/B testing

### A/B testing
- Testing model A and B in production then compare

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/AB testing.png]]


### Data Drift Detection

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/Data Drift and Concept Drift.png]]

- Data Drift detection techniques: 
	- Univariate statistical tests:
		- Kolmogorov-Smirnov test (numerical features)
		- Chi-squared test
	- Interpretation of results:
		- Remove the feature
		- Reweight feature


# MLOps Methodology
## MLOps Maturity
- MLOps Maturity:
	- Level automation of ML pipeline determines the maturity of MLOps process
	- As maturity increase, the velocity of training and deployment of new models also speed up
	- Reduce manual intervention
- Target of MLOps Maturity:
	- Automatic train and deploy models into core orchestration system, and provide monitoring and analyzing models
	- Detect and warning data drift, model decay and as well as trigger model pipeline

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/MLOps Maturity.png]]

## MLOps level 0: Manual Process
- Characteristics
	- Each step is manually trained and transit on the notebook.
	- Interactive between data scientist until they create a workable model.

	- Suitable with few code change.
	- Less frequent release.
	- No CI/CD and unit testing.
	- Test is part of notebook or script execution.
	- Deploy model under microservice instead of whole system.
	- Do not monitor model performance degradation and other model behavioral drift

- Model fail to adapt the change of dynamic environment so:
	- Need actively monitoring the model quality in production.
	- Retrain production models with the new data.

## MLOps level 1: CT (Continuous training)/ML pipeline automation
- Characteristics
	- Automatically training model and prediction
	- Enable to retrain production models with the new data.
	- Transition between steps are automatically → Easy to iterate and move whole pipeline into production.

- Challenge
	- Manually test and deploy the ML pipeline.
	- => CI/CD setup to automate the build, test, and deployment of ML pipelines

## MLOps level 2: CI/CD pipeline automation
- Characteristics
	- Reliable update of the pipeline in production.
	- Automatic CI/CD to enable Data Scientist and ML Engineer rapidly explore new idea around feature engineering/model architecture and hyperparameters.
	- Automatically build test and deploy pipeline components to target environment


![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/5_MLOPs/AI Platforms and Frameworks.png]]



# 

---
- Status: #done

- Tags: #mlops 

- References:
	- 

- Related:
	- 
