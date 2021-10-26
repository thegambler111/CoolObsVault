# Chapter 4: Developing models

- What Is a Machine Learning Model?
	- A machine learning model = basic formula + parameters
	- Parameters = Basic formula + Hyperparameters + Training Data + Training
	- A ML model is an approximate representation of a real thing
	- Training components = Training data + A performance metric + ML algorithm + Hyperparameters + Evaluation dataset
	- High bias = underfitting
	- High variance = overfitting

- Data collection:
	- [ ] What relevant datasets are available?
	- [ ] Is this data sufficiently accurate and reliable?
	- [ ] How can stakeholders get access to this data?
	- [ ] What data properties (known as features) can be made available by combining multiple sources of data?
	- [ ] Will this data be available in real time?
	- [ ] Does this data need to be labeled? How much time and resource will it take for labeling?
	- [ ] What platform should be use?
	- [ ] How will data be updated once the model is deployed?
	- [ ] Will the use of the model itself reduce the representativeness of the data?
	- [ ] How will the KPIs, which were established along with the business objectives, be measured?
- Data exploration:
	- [ ] **Are there anybody with domain knowledge?**
	- [ ] Exploratory data analysis (EDA) techniques?
		- [ ] Build hypotheses about the data
		- [ ] Identify data cleaning requirements
		- [ ] Inform the process of selecting potentially significant features.
		- [ ] Visualize for intuitive insight and statistically
	- [ ] Data exploration process:
		- [ ] Full documents of data process and assumptions
		- [ ] Plotting?
		- [ ] From the summarizing statistics of the data:
			- [ ] Domain of each column?
			- [ ] Missing value in row?
			- [ ] Obvious mistakes?
			- [ ] Strange outliers?
			- [ ] No outliers?
		- [ ] Data distribution?
		- [ ] Data augmentation: Cleaning, filling, reshaping, filtering, clipping, sampling, etc?
		- [ ] Checking correlations between the different columns
		- [ ] Running statistical tests on some subpopulations
		- [ ] Fitting distribution curves
		- [ ] Comparing with other data on the same category:
			- [ ] Usual information but missing?
			- [ ] Comparably distributed?
- Feature engineering and selection
	- [ ] Plotting?
	- [ ] Exploring new features
		- [ ] Infer new information from existing model
		- [ ] Add new external information
		- [ ] Present the same information differently
		- [ ] Link feature together
	- [ ] Dealing with unavailable data
		- [ ] Impact coding
	- [ ] Encoding data
		- [ ] One-hot coding
		- [ ] Embedding
	- [ ] Transfer learning
	- [ ] Automated feature selection?
		- [ ] Suggested libraries: Auto-sklearn, AutoML
		- [ ] Which inputs to use?
		- [ ] How to encode them?
		- [ ] How they interact or interfere with each other?
	- [ ] Manual feature selections?
		- [ ] Collecting more data?
		- [ ] Building business-friendly features?
	- [ ] **Building feature store?**
		- [ ] Offline part
		- [ ] Online part
	- [ ] Trade-off
		- [ ] Model too expensive to train?
		- [ ] Too much inputs and maintenance?
		- [ ] Stability loss?
		- [ ] Privacy concern?
-  Model experimentation
	- [ ] Automated experimenting?
		- [ ] What should be test?
		- [ ] Prior knowledge?
		- [ ] Constraints (i.e. computation, budget)? 
	- [ ] For each experiment:
		- [ ] Version control?
		- [ ] Time and computation budget?
		- [ ] Assumptions?
		- [ ] Randomness?
		- [ ] Environment?
		- [ ] Acceptable threshold?
		- [ ] Training data
		- [ ] Performance metrics
		- [ ] ML algorithm
		- [ ] Transfer learning
		- [ ] Hyperparameters
		- [ ] Evaluation dataset
		- [ ] Feature preprocessing
		- [ ] Bias/Variance trade-off (how much is overfit)
		- [ ] Improvement and computation cost trade-off
		- [ ] Plotting outputs
		- [ ] Conclusions
		- [ ] **Documentation of all things above**
- Evaluation and comparing models
	- [ ] Single model evaluation
		- [ ] Plotting?
		- [ ] Any baseline as a comparison?
		- [ ] Model doing bad job for a specific subset of cases?
		- [ ] Is model too good?
		- [ ] Maths metrics and business evaluation trade-off
		- [ ] Validation dataset is simple split or k-fold cross validation? (better k-fold when you can't make an representative validation dataset from the whole dataset)
	- [ ] Cross-checking models?
		- [ ] Plotting?
		- [ ] Introduce new metrics?
		- [ ] Cross-checking metrics
		- [ ] Model reactions to different inputs?
		- [ ] Model behaviors and metrics across different subpopulations on one particular dimension?
	- [ ] Model predictions explanation
		- [ ] Do we need to understand each individual prediction?
		- [ ] Methods for individual prediction explanations:
			- [ ] Shapley value
			- [ ] Individual conditional expectation computations
		- [ ] "Fairness" between subpopulations
- Version Management and Reproducibility
	- [ ] Can these versions be used to recreate the final decision?
	- [ ] Model facets need to be documented:
		- [ ] Assumptions
		- [ ] Randomness
		- [ ] Data
		- [ ] Settings
		- [ ] Results
		- [ ] Implementation
		- [ ] Environment























# 

---
Status: #writing

Tags: #mlops #machine_learning #data_analysis #data_management #data_augmentation #check_list

References:
-  

Related:
- 
