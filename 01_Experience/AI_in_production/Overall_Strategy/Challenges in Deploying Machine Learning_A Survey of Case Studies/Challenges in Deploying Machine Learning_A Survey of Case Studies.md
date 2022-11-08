# Life cycle

| Deployment Stag       | Deployment Step           | Considerations, Issues and Concerns |
|-----------------------|---------------------------|-------------------------------------|
| Data management       | Data collection           | Data discovery                      |
|                       | Data preprocessing        | Data dispersion                     |
|                       |                           | Data cleaning                       |
|                       | Data augmentation         | Labeling of large volumes of data   |
|                       |                           | Access to experts                   |
|                       |                           | Lack of high-variance data          |
|                       | Data analysis             | Data profiling                      |
| Model learning        | Model selection           | Model complexity                    |
|                       |                           | Resource-constrained environments   |
|                       |                           | Interpretability of the model       |
|                       | Training                  | Computational cost                  |
|                       |                           | Environmental impact                |
|                       | Hyper-parameter selection | Resource-heavy techniques           |
|                       |                           | Hardware-aware optimization         |
| Model verification    | Requirement encoding      | Performance metrics                 |
|                       |                           | Business driven metrics             |
|                       | Formal verification       | Regulatory frameworks               |
|                       | Test-based verification   | Simulation-based testing            |
| Model deployment      | Integration               | Operational support                 |
|                       |                           | Reuse of code and models            |
|                       |                           | Software engineering anti-patterns  |
|                       |                           | Mixed team dynamics                 |
|                       | Monitoring                | Feedback loops                      |
|                       |                           | Outlier detection                   |
|                       |                           | Custom design tooling               |
|                       | Updating                  | Concept drift                       |
|                       |                           | Continuous delivery                 |
| Cross-cutting aspects | Ethics                    | Country-level regulations           |
|                       |                           | Focus on technical solution only    |
|                       |                           | Aggravation of biases               |
|                       |                           | Authorship                          |
|                       |                           | Decision making                     |
|                       | End users’ trust          | Involvement of end users            |
|                       |                           | User experience                     |
|                       |                           | Explainability score                |
|                       | Security                  | Data poisoning                      |
|                       |                           | Model stealing                      |
|                       |                           | Model inversion                     |


# Data management:
- Data is an integral part of any machine learning solution. Overall effectiveness of the solution depends on the training and test data as much as on the algorithm. This stage consumes time and energy that is often not anticipated beforehand.

## Data collection:
- Discover and understand what data is available
- Organize convenient storage for data

## Data preprocessing:
- Imputation of missing values
- Reduction of data into an ordered and simplified form
- Mapping from raw form into a more convenient format

## Data augmentation:
- Solving the absence of labels caused by:
	- Limited access to experts
	- Absence of high-variance data
	- Low volume of data

## Data analysis: uncover potential biases or unexpected distributions:
- Five high-level tasks:
	- Discover data necessary to complete an analysis tasks. Example tasks include finding a data set online, locating the database tables in a MySQL database, or asking a colleague for a spreadsheet.
	- Wrangle data into a desired format. Example tasks include parsing fields from log files, integrating data from multiple sources into a single file or extracting entities from documents.
	- Profile data to verify its quality and its suitability for the analysis tasks. Example tasks include inspecting data for outliers or errors and examining the distributions of values within fields.
	- Model data for summarization or prediction. Examples include computing summary statistics, running regression models, or performing clustering and classification.
	- Report procedures and insights to consumers of the analysis.



# Model Learning:
- Model learning is the stage of the deployment workflow that enjoys the most attention within the academic community.

## Model selection:
- In many practical cases the selection of a model is often decided by one key characteristic of a model: complexity. However, in practice, simpler models are often chosen.
	- Choosing simpler models accelerates the time to get a deployed solution, allows the collection of important feedback and also helps avoid overcomplicated designs.
	- Hardware requirement is lower. This becomes a key decision point in resource constrained environments.
	- The ability to interpret the output of a model into understandable business domain terms often plays a critical role in model selection, and can even outweigh performance considerations.
	
## Training:
- One of the biggest concern with model training is the economic cost associated with carrying the training stage due to the computational resources required.

## Hyper-parameter selection;
- This technique is very expensive and resource-heavy in practice.




# Model verification:
- The goal of the model verification stage is multifaceted, because an ML model should generalize well to unseen inputs, demonstrate reasonable handling of edge cases and overall robustness, as well as satisfy all functional requirements.
## Requirement encoding:
- Defining requirements for a machine learning model is a crucial prerequisite of testing activities. Increasing in model performance often does not translate into a gain in business value, therefore, more specific metrics need to be defined and measured, such as KPIs and other business driven measures.

## Formal Verification:
- This step verifies that the model functionality follows the requirements defined within the scope of the project including mathematical proofs of correctness or numerical estimates of output error bounds.

## Test-based Verification:
- Test-based verification is intended for ensuring that the model generalizes well to the previously unseen data.


          

# Model Deployment:
- Machine learning systems running in production are complex software systems that have to be maintained over time.

## Integration:
 - The model integration step constitutes of two main activities: building the infrastructure to run the model and implementing the model itself in a form that can be consumed and supported.

## Monitoring:
 - Monitoring is one of the issues associated with maintaining machine learning systems, including monitoring of evolving input data, prediction bias and overall performance of ML models.

## Updating:
 - A particularly important problem that directly impacts the quality and frequency of model update procedure is the concept drift. Concept drift in ML is understood as changes observed in joint distribution p(_X_, _y_), where _X_ is the model input and _y_ is the model output.



# Cross-cutting aspects

## Ethics:
 - Ethical considerations should always inform data collection activities.

## End users’ trust:
 - ML is often met cautiously by the end users. On their own accord models provide minimal explanations, which makes it difficult to persuade end users in their utility. In order to convince users to trust ML based solutions, time has to be invested to build that trust.

## Security:
 - Specialized adversarial attacks for ML can occur on the model itself, the data used for training but also the resulting predictions. The three most common attacks reported in practice which affects deployed ML models: data poisoning, model stealing and model inversion.

### Data poisoning:
 - The goal is to deliberately corrupt the integrity of the model during the training phase in order to manipulate the produced results. Poisoning attacks are particularly relevant in situations where the machine learning model is continuously updated with new incoming training data.
 
### Model stealing
 - Another type of adversarial attack is reverse engineering a deployed model by querying its inputs (e.g. via a public prediction API) and monitoring the outputs. The adversarial queries are crafted to maximize the extraction of information about the model in order to train a substitute model.
 
### Model inversion
 - The goal of the model inversion is recovering parts of the private training set, thereby breaking its confidentially.


          

# Discussion of potential solutions

## Tools and services:
 - A typical ML platform would include, among other features, data storage facility, model hosting with APIs for training and inference operations, a set of common metrics to monitor model health and an interface to accept custom changes from the user.
 - Weak supervision has emerged as a separate field of ML which looks for ways to obtain labels of real world data. Consequently, a number of weak supervision libraries are now actively used within the community, and show promising results in industrial applications.

## Holistic approaches:
 - Data Oriented Architectures (DOA), a streaming-based architecture instead of micro-service.
 - ML projects normally do not fit well with commonly used management processes, such as Scrum or Waterfall. Technology Readiness Levels for ML (TRL4ML) framework might be a good choice.




# 

---
- Status: #done 

- Tags: #ai_lifecycle 

- References:
	- [Challenges in Deploying Machine Learning: a Survey of Case Studies](https://arxiv.org/abs/2011.09926)

- Related:
	- [[01_Experience/AI_in_production/Overall_Strategy/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges/Assuring the Machine Learning Life cycle_Desiderata, Methods, and Challenges]]
	- [[01_Experience/AI_in_production/Lifecycle/3_1_Model_training/A Recipe for Training Neural Networks]]