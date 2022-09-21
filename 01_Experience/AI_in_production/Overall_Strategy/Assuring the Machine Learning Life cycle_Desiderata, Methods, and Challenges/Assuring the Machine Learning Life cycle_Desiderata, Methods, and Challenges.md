# The machine learning life cycle

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/The machine learning life cycle.png]]

# Data management:

- Input/Output: Model requirements => Training and validation data sets
- Four key activities:
	- Data collection: This activity is concerned with collecting data from an originating source
	- Data preprocessing: preprocessing is a one-to-one mapping: it adjusts each collected (raw) sample in an appropriate manner. (read DSMOTE)
		- Imputation of missing values
		- Reduction of data into an ordered and simplified form
		- Mapping from raw form into a more convenient format
	- Data augmentation: Augmentation increases the number of samples in a data set, generally, a one-to-many mapping.
	- Data analysis: Analysis may be required to guide aspects of collection and augmentation
- Desiderata: Desired attributes
	- Relevant: intersection between the data set and the desired behaviour
	- Complete: samples distribution across the input domain and subspaces
	- Balanced: distribution of features that are included in the data set
	- Accurate: measurement issues can affect the way that samples reflect the intended operational domain (i.e. sensor accuracy)

## Assurance methods

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Assurance methods for the Data Management stage.png]]

## Open challenges

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Open challenges for the assurance concerns associated with the Data Management (DM) stage.png]]



# Model learning:
- Input/Output: Data sets => Trained model
- Activities:
	- Model selection: decides the model type, variant, structure and, where applicable
	- Training: optimizes the performance of the model with respect to an objective function that reflects the requirements for the model
	- Hyper parameter selection: select the parameters associated with the training activity
	- Transfer learning
- Desiderata:
	- Performance: considers quantitative performance metrics (accuracy,...) applied to the model
		- Ensemble learning: 
			- Bagging
			- Boosting
		- AdaBoost > Other Boost
		- SMOTE: unbalance data set
	- Robust: considers the model’s ability to perform well in circumstances where the inputs encountered at run time are different to those present in the training data (i.e. environmental uncertainty)
		- **k-fold cross-validation**
		- Deep learning models are susceptible to some carefully constructed small noise called **adversarial perturbations**, which when added to an input image, cause the network output to change drastically without making perceptible changes to the input image.
		- **Random Erasing + Random Cropping**: 
			- Note: the values inside the square are random
			- ![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Random erasing.png]]
			- ![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Random cropping + erasing.png]]
		- **DropConnect**: drop connection instead of output like Dropout
	- Reusable: considers the ability of a model, or of components of a model, to be reused in systems for which they were not originally intended
	- Interpretable (~explainable): considers the extent to which the model can produce artifacts that support the analysis of its output, and thus of any decisions based on it.

## Assurance methods

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Assurance methods for the Model Learning stage.png]]

## Open challenges
![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Open challenges for the assurance concerns associated with the Model Learning (ML) stage.png]]


# Model verification:

- Input/Output: Trained model => Verified model
- Activities:
	- Requirement Encoding: transform requirements into both tests and mathematical properties, where the latter can be verified using formal techniques
	- Test-Based Verification: provide test cases (i.e., specially-formed inputs or sequences of inputs) to the trained model and checking the outputs against predefined expected results; involves an independent examination of properties considered during the Model Learning stage.
	- Formal Verification: use mathematical techniques to provide irrefutable evidence that the model satisfies formally-specified properties derived from its requirements
- Desiderata:
	- Comprehensive (~complete): concern with the ability of Model Verification to cover:
		- All the requirements and operating conditions associated with the intended use of the model
		- All the desiderata from the previous stages of the ML lifecycle (e.g., the completeness of the training data, and the robustness of the model)
	- Contextually Relevant: map test cases to contextually meaningful aspects
	- Comprehensible (~understandable): consider the extent to which verification results can be understood by those using them in activities ranging from data preparation and model development to system development and regulatory approval.

## Assurance methods

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Assurance methods for the Model Verification stage.png]]

## Open challenges

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Open challenges for the assurance concerns associated with the Model Verification (MV) stage.png]]


# Model deployment:
+ Input/Output: Verified model => Deployed model.
+ Activities:
	- Integration: This activity involves integrating the ML model into the wider system architecture.
	- Monitoring: 
		- Inputs.
		- System environment.
		- Model internals.
		- Model output.
	- Updating:
+ Desiderata:
	- Fit-for-Purpose: the ML model needs to be fit for the intended purpose within the specific system context.
	- Tolerated: the wider system must be able to tolerate the occasional incorrect output from the ML model.
	- Adaptable: ease to change made to deployed ML model

## Assurance methods

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Assurance methods for the Model Deployment stage.png]]

## Open challenges

![[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Open challenges for the assurance concerns associated with the Model Deployment (MD) stage.png]]



# 

---
- Status: #done 

- Tags: #ai_life_cycle

- References:
	- [Assuring the Machine Learning Life cycle: Desiderata, Methods, and Challenges](https://arxiv.org/abs/1905.04223)

- Related:
	- [[01_Experience/AI_in_production/Overall_Strategy/Challenges in Deploying Machine Learning_A Survey of Case Studies/Challenges in Deploying Machine Learning_A Survey of Case Studies]]
	- [[01_Experience/AI_in_production/Lifecycle/3_1_Model_training/A Recipe for Training Neural Networks]]
