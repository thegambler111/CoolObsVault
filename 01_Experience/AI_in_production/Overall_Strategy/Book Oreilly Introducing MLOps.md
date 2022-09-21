# Part I: MLOps: What and Why

## Chapter 1: Why now and Challenges

### TLDR
- MLOps is new and many steps are overlooked
- MLOps reduces the risk, enable Explainable AI, and make it easier to scale

### Defining MLOps and Its Challenges


![[Images/AI_in_production/Book_Intro_MLOps_life_cycle.png]]
Figure 1-2. A simple representation of the machine learning model life cycle, which often underplays the need for MLOps, compared to Figure 1-3


![[Images/AI_in_production/Book_Intro_MLOps_roles.png]]
Figure 1-3. The realistic picture of a machine learning model life cycle inside an average organization today, which involves many different people with completely different skill  sets and who are often using entirely different tools.


- MLOps ~ ModelOps
- AIOps != MLOps
- MLOps vs DevOps:
	- Similarities:
		- Robust automation and trust between teams
		- The idea of collaboration and increased communication between teams
		- The end-to-end service life cycle (build, test, release)
		- Prioritizing continuous delivery and high quality
	- Differences:
		- DevOps:
			- Software code is relatively static
		- MLOps:
			- Data is always changing => Models are constantly learning and adapting
- MLOps vs DataOps:
	-  DataOps seeks to provide business-ready data that is quickly available for use, with a large focus on data quality and metadata management.
	-  MLOps Intersects with DataOps at some level but goes a step further and brings even more robustness.

- Challenges: Three key reasons that managing machine learning life cycles at scale is challenging
	- There are many dependencies: Constantly changing data and business
	- Not everyone speaks the same language.
	- Data scientists are not software engineers.


### MLOps to Mitigate Risk

- Risks should be covered:
	- The risk that the model is unavailable for a given period of time
	- The risk that the model returns a bad prediction for a given sample
	- The risk that the model accuracy or fairness decreases over time
	- The risk that the skills necessary to maintain the model (i.e., data science talent) are lost


![[Images/AI_in_production/Book_Intro_MLOps_risk_assessment.png]]
Figure 1-4. A table that helps decision makers with quantitative risk analysis


- Model performance depends on training data
	- => Training data must be a good reflection of data in production environment
	- => When production environment changes, model performance is likely to decrease

### MLOps for Responsible AI

- MLOps is needed to practice Responsible AI and vice versa.


## Chapter 2: People of MLOps

### TLDR
- Subject matter experts:
	- Define business goals and a business way to verify model performance
	- Should work with Data scientists to:
		- Better understand of business goals
		- Brainstorm possible solutions
- Data scientists:
	- Work with Subject matter experts to understand to problems and build a solution
	- Ensure model performance satisfy business needs
	- Need access to model performance along with data pipeline and the ability to change the models quick, easily and safely.
- Data engineers:
	- Optimize the retrieval and use of data
	- Identify and prepare the right data
	- Resolve any data plumbing issues
- Software engineers:
	- Work with data scientists to integrate and ensure ML models work seamlessly with other parts of the projects.
- DevOps:
	- Conduct and build operational systems as well as tests to ensure security, performance, and availability of ML models.
	- Manage CI/CD pipeline.
- Model Risk Manager/Auditor:
	- Prevent loss from potential risks for the company by:
		- Analyzes the initial goal, business questions and model outcomes.
		- Monitors models in production.
		- Ensures initial compliance with internal and external requirements.
	- Need robust reporting tools, better with automated ones
- Machine Learning Architects:
	- Create, maintain and improve ML architecture from data pipeline to model pipeline
	- Identify bottleneck and pinpoint possible new technology or infrastructure to solve problems at heart.


### Role table

| Role                          | Work                                                                                                                                                                                                                                                                                                                                                                                  | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Subject matter expert         | - Provide business questions, goals, or KPIs aroundwhich ML models should be framed. <br> - Continually evaluate and ensure that modelperformance aligns with or resolves the initial need.                                                                                                                                                                                           | - Easy way to understand deployed model performance in business terms.<br> - Mechanism or feedback loop for flagging model results that don’t align with business expectations.                                                                                                                                                                                                                                                                                                            |
| Data scientists               | - Build models that address the business question or needs brought by subject matter experts.<br>- Deliver operationalizable models so that they can be properly used in the production environment and with production data.<br>- Assess model quality (of both original and tests) in tandem with subject matter experts to ensure they answer initial business questions or needs. | - Automated model packaging and delivery for quick and easy (yet safe) deployment to production.<br>- Ability to develop tests to determine the quality of deployed models and to make continual improvements.<br>- Visibility into the performance of all deployed models (including side-by-side for tests) from one central location.<br>-  Ability to investigate data pipelines of each model to make quick assessments and adjustments regardless of who originally built the model. |
| Data engineers                | - Optimize the retrieval and use of data to power MLmodel                                                                                                                                                                                                                                                                                                                             | - Visibility into performance of all deployed models.<br>- Ability to see the full details of individual data pipelines to address underlying data plumbing issues                                                                                                                                                                                                                                                                                                                         |
| Software engineers            | - Integrate ML models in the company’s applications and systems.<br>- Ensure that ML models work seamlessly with other non-machine-learning-based applications                                                                                                                                                                                                                        | - Versioning and automatic tests.<br>- The ability to work in parallel on the same application.                                                                                                                                                                                                                                                                                                                                                                                            |
| DevOps                        | - Conduct and build operational systems and test for security, performance, availability.<br>- Continuous Integration/Continuous Delivery (CI/CD) pipeline management.                                                                                                                                                                                                                | - Seamless integration of MLOps into the larger DevOps strategy of the enterprise.<br>- Seamless deployment pipeline.                                                                                                                                                                                                                                                                                                                                                                      |
| Model risk managers/ auditors | - Minimize overall risk to the company as a result of ML models in production.<br>- Ensure compliance with internal and external requirements before pushing ML models to production.                                                                                                                                                                                                 | - Robust, likely automated, reporting tools on all models (currently or ever in production), including data lineage.                                                                                                                                                                                                                                                                                                                                                                       |
| Machine learning architects   | - Ensure a scalable and flexible environment for ML model pipelines, from design to development and monitoring.<br>- Introduce new technologies when appropriate that improve ML model performance in production.                                                                                                                                                                     | - High-level overview of models and their resources consumed.<br>- Ability to drill down into data pipelines to assess and adjust infrastructure needs.                                                                                                                                                                                                                                                                                                                                    | 


### Subject Matter Expert

- The subject matter expert:s
	- Have a clear understanding of the business, problems and questions which no other role has.
	- Provide business goals and a way to verify ML models performance to align with the business goals.
- The business goals need to be clearly defined.
	- Subject matter experts and Data scientists can work together to up front a better frame the problem and brainstorm possible solutions.
- The subject matter experts needs to provide a way to verify ML models performance as traditional metrics are not enough of a valuation.
- MLOps processes help subject matter experts understand data pipeline behind the models and model performance in business term.



### Data scientists

- MLOps processes need to provide Data scientists with a lot of tools to ease their work and increase their efficiency.
- From the start, Data scientists need to work with Subject matter expert to understand the problems so that they can build a viable machine learning solution
	- This step is hard because most Data scientists are not trained for communicating effectively and also because this step can take a long time.
	- Business decision modeling techniques can help here.
- After that step, the project is handed off to either data engineers or analysts to do some of the initial data gathering, preparation, and exploration.
- Following deployment, data scientists’ roles include constantly assessing model quality to ensure its results align with the business goals.
- As the amount of work for Data scientists is huge, MLOps processes must provide them with:
	- The visibility into the performance of all deployed and A/B test models
	- The ability to drill down into data pipelines and make quick assessments and adjustments
	- The ability to automated model packaging and delivery for quick, easy and safe deployment to production.
	- => Pure efficiency to reduce work time.


### Data engineers

- Data engineers are at the core of data pipelines which in turn are at the core of ML model life cycle
- The role of data engineers is to optimize the retrieval and use of data to eventually power ML models
- Data engineers need to work with:
	- Subject matter experts to identify and prepare the right data
	- Data scientists to resolve any data plumbing issues
- MLOps must provide:
	- Visibility into the performance of all models in production
	- Ability to directly drill down into individual data pipelines
	- Ability to investigate and tweak ML models


### Software Engineers

- Software engineers' task is to work with data scientists to integrate ML models and ensure the functioning of the larger system.
- All the machine learning code, training, testing, and deployment have to fit into the Continuous Integration/Continuous Delivery (CI/CD) pipelines that the rest of the software is using.
- MLOps helps Software engineers and Data scientists to speak the same language and have the same baseline understanding of how different models working together in production.
- MLOps need to provide Software engineers with
	- Model performance details
	- Ability of versioning, automatic testing and working in parallel (work in branches and merge)


### DevOps

- DevOps teams have two primary roles:
	- Conducting and building operational systems as well as tests to ensure security, performance, and availability of ML models.
	- Managing CI/CD pipeline.
	- => It is required to have tight collaboration with data scientists, data engineers, and data architects.
- MLOps needs to be integrated into the larger DevOps strategy of the enterprise, bridging the gap between traditional CI/CD and modern ML. 


### Model Risk Manager/Auditor

- MRM tasks are to prevent catastrophic loss introduced by poorly performing ML models.
- MRM:
	- Analyzes the initial goal, business questions and model outcomes to minimize overall risk.
	- Monitors models in production
	- Ensures initial compliance with internal and external requirements in post-model development and preproduction
- MLOps needs to provide robust reporting tools about performance details and data lineage on all models (both trial and in production), especially automated reporting.


### Machine Learning Architect

- Machine learning architects:
	- Define data and model pipelines
	- Ensure a scalable and flexible environment for model pipelines.
	- Introduce new technologies (when appropriate) that improve ML model performance in production.
	- Pinpoint possible new technology or infrastructure for investment
- Machine learning architects require collaboration across the enterprise, from data scientists and engineers to DevOps and software engineers to properly allocate resources to ensure optimal performance of ML models in production.
- MLOps needs to provide:
	- Information about the ins and outs of data storage, data consumption and how ML models work
	-  A centralized view of resource allocation.
	-  An overview of the situation to identify bottlenecks and use that information to find long-term improvements. 


### ML project as a cooking contest

- The big project is a whole meal
- ML project is a dish
- Subject matter expert is the judge who gives requirements and mark the results
- Data scientist is the cook who experiments and finds the most suitable dish, cooks it and ensures its taste
- Data engineer is the ingredients buyer who ensure the best quality of raw material and the cook can use them anytime
- Software engineers is the head chef who ensures all dishes fit together
- DevOps is the person to set the table and also the food tester who help the cook ensure the food quality.
- Model Risk Manager/Auditor is the observer who watch over the cooking, spot problems and provide suitable solutions.
- Machine Learning Architects is the planner who decide which dishes to cook and how to cook them best



## Chapter 3: Key MLOps Features

### TLDR

- You need ML knowledge to understand key feature of MLOps
- Model development in steps:
	- Establishing business objectives: estimating performance target, infrastructure, cost and change management
	- Data sources and exploratory data analysis:
		- Understanding the data first is essential
		- Exploratory data analysis (EDA) techniques is helpful
		- We need to check status, availability, suitability and legality of the data
	- Feature Engineering and Selection:
		- Feature engineering is transforming raw data into "features" that is more suitable to solve the problem.
	- Training and Evaluation:
		- Training and optimizing is an iterative process of
			- Testing algorithms
			- Automatically generating features
			- Adapting feature selections 
			- Tuning algorithm hyperparameters
		- An experiment tracking to is necessary
		- Solution needs to be evaluated on both training metrics and business metrics
	- Reproducibility:
		- Reproducibility requires version control of all the assets and parameters involved, including data and environment to reproduce same result from scratch.
	- Responsible AI:
		- Documentations on how model is built and tuned and how decision is made are necessary
		- Model explainability is important
		- Most common explainability techniques focus on:
			- Impacts on predictions among features
			- Impacts on predictions among classes
			- Impacts on predictions inside each feature
			- Input sensitivity of the prediction
- Productionalization and Deployment:
	- Model Deployment Types and Contents:
		- 2 types of model deployments:
			- Model-as-a-service
			- Embedded model (an app)
		- Using portable model format or containerization is some ways to reduce dependencies
	- Model Deployment Requirements:
		- Rapid, automated deployment is a must
		- Robust CI/CD pipeline involves:
			- Ensuring all coding, documentation and sign-off standards have been met
			- Re-creating the model in something approaching the production environment
			- Revalidating the model accuracy
			- Performing explainability checks
			- Ensuring all governance requirements have been met
			- Checking the quality of any data artifacts
			- Testing resource usage under load
			- Embedding into a more complex application, including integration tests
- Monitoring
	- DevOps Concerns:
		- Model speed
		- Providing sensible amount of resource and processing time
	- Data Scientist Concerns:
		- Models degradation
		- Using ground truth or input drift to identify the degradation
	- Business Concerns::
		- Model value
		- Model value vs model cost
- Iteration and Life Cycle:
	- Iteration:
		- We need to check for data validation, completion, consistency and feature distributions
		- Model comparison should be done manually
		- Iteration on edge can be either done at a central point or done locally then update the shared model.
	- The Feedback Loop:
		- There are 3 comparison methods:
			- Shadow score: Both models score all requests
				- => Expensive and sometimes unavailable
			- A/B testing: requests are split evenly between models
				- => Hard to compare and contain risks
			-  Bayesian, and in particular multi-armed bandit, tests: requests are split based on models' live results
				-  => Better but more complex than A/B testing
 - Governance:
	- Governance is a set of business controls to ensure ML responsibilities including financial, legal and ethical.
	- MLOps governance falls into:
		- Data governance:
			- Data's origin
			- How data is collected
			- Data's terms of use
			- Is the data accurate and up to date?
			- Sensitive personally identifiable information data
		- Process governance:
			- Process governance focuses on formalizing MLOps steps and associating actions with them


### A Primer on Machine Learning

- To understand the key features of MLOps, it’s essential first to understand how machine learning works and be intimately familiar with its specificities.
- At its core, machine learning is the science of computer algorithms that automatically learn and improve from experience rather than being explicitly programmed. 


### Model Development

- Establishing business objectives:
	- Business objectives naturally come with 3 key performance indicators (KPIs):
		- Performance targets
		- Technical infrastructure requirements
		- Cost constraints
	- Establishing objectives also includes change management for technologies, processes and people of the larger project.
- => Start developing ML model.
-  Data sources and exploratory data analysis:
	-  Data is the essential ingredient to power ML algorithms => Need to understand the pattern in data before training model
	-  Exploratory data analysis (EDA) techniques can help
		-  Build hypotheses about the data
		-  Identify data cleaning requirements
		-  Inform the process of selecting potentially significant features.
		-  Visualize for intuitive insight and statistically
	- Key questions for finding data:
		- What relevant datasets are available?
		- Is this data sufficiently accurate and reliable?
		- How can stakeholders get access to this data?
		- What data properties (known as features) can be made available by combining multiple sources of data?
		- Will this data be available in real time?
		- Does this data need to be labeled? How much time and resource will it take for labeling?
		- What platform should be use?
		- How will data be updated once the model is deployed?
		- Will the use of the model itself reduce the representativeness of the data?
		- How will the KPIs, which were established along with the business objectives, be measured?
	- Questions for data governance:
		- Can the selected datasets be used for this purpose?
		- What are the terms of use?
		- Is there personally identifiable information (PII) that must be redacted or anonymized?
		- Are there features, such as gender, that legally cannot be used in this business context?
		- Are minority populations sufficiently well represented that the model has equivalent performances on each group?
- Feature engineering and selection:
	- Feature engineering is transforming raw data into "features" that better represent the underlining problem to be solved
- Training and evaluation:
	- Training and optimizing a new ML model is iterative
		- Several algorithms may be tested
		- Features can be automatically generated
		- Feature selections may be adapted
		- Algorithm hyperparameters are tuned.
	- An experiment tracking tool can greatly simplify the process of
		- Remembering the data
		- Feature selection
		- Model parameters
		- Performance metrics
	- Best solution depends on both:
		- Quantitative criteria like accuracy or average error
		- Qualitative criteria like explainability or ease of deployment
- Reproducibility:
	- The aim of reproducibility is to save enough environment information to reproduce the same result from scratch.
	- True reproducibility requires version control of all the assets and parameters involved, including the data used to train and evaluate the model, as well as a record of the software environment
- Responsible AI:
	- In order for DevOps to understand how the model was built and how it was tuned, documentations are necessary
	- An automated documentation generating tool is required, however, some documents explaining the choices made will need to be written by hand
	- Model explainability is important to :
		- Sanity-check the model 
		- Help better engineer features
		- Ensure fairness requirements around features
	- Explainability techniques most commonly used today include:
		- Partial dependence plots, which look at the marginal impact of features on the predicted outcome 
		- Subpopulation analyses, which look at how the model treats specific subpopulations and that are the basis of many fairness analyses
		- Individual model predictions, such as Shapley values, which explain how the value of each feature contributes to a specific prediction
		- What-if analysis, which helps the ML model user to understand the sensitivity of the prediction to its inputs


### Productionalization and Deployment

- This is the domain of the software engineer and the DevOps team
- Managing the information exchange between the data scientists and these teams must not be underestimated.
- Model Deployment Types and Contents:
	- There are 2 types of model deployments:
		- Model-as-a-service, or live-scoring model
		- Embedded model (independent application)
	- Model add dependencies to environment
	- Exporting model to portable format such as PMML, PFA, ONNX, or POJO is a way to reduce dependencies
	- Another solution is containerization (i.e. Docker)
- Model Deployment Requirements:
	- Rapid, automated deployment is always preferred to labor-intensive processes.
	- Robust CI/CD pipeline involves:
		- Ensuring all coding, documentation and sign-off standards have been met
		- Re-creating the model in something approaching the production environment
		- Revalidating the model accuracy
		- Performing explainability checks
		- Ensuring all governance requirements have been met
		- Checking the quality of any data artifacts
		- Testing resource usage under load
		- Embedding into a more complex application, including integration tests


### Monitoring

- DevOps Concerns:
	- They concerns about:
		- Model speed
		- Providing sensible amount of resource and processing time
- Data Scientist Concerns:
	- Models may degrade over time => DS concerns about whether the model has degraded or not
	- There are 2 ways to tell if a model's performance is degrading:
		- Ground truth: 
			- Comparing model's predictions in production with ground truth
			- Time to obtain the ground truth may vary depending on the task
		- Input drift:
			- Identifying distinct differences between real world data and training data.
			- All the data required for this test already exists
- Business Concerns:
	- They concerns about:
		- Model value
		- Model value vs model cost


### Iteration and Life Cycle

- Training new and improved models is essential
- Iteration:
	- For new training data, you need to:
		- Validate the data
		- Check its completion and consistency
		- Ensure that the distributions of features broadly similar to those in the previous training set
	- Comparing new and old model is complicated, therefore, it should not be done automatically
	- Iterating on edge: 2 ways:
		- Gathering all feedback to a central point and training there
			- => Expensive
		- Training locally then gathering summaries of improvements to update shared model.
			- => No user’s personal data is collected
			- => Improved model can be used immediately
			- => Overall power consumption is reduced
- The Feedback Loop: 3 methods to comparing old and new models
	- Shadow score:
		- All requests are handled by old model
		- All requests are also scored by new model
		- Results from those requests are used to compare the models
	- A/B testing:
		- Each request is processed by either old or new model
		- Meaningful conclusions requires careful planning
		- => Can be time consuming
	- Bayesian, and in particular multi-armed bandit, tests:
		- This method is adaptive: Based on live results, the better model handles model requests
		- However, it is more complex




### Governance

- Governance is a set of business controls to ensure ML responsibilities including financial, legal and ethical.
- MLOps governance falls into:
	- Data governance
	- Process governance
- Data Governance:
	- Data governance addresses:
		- Data's origin
		- How data is collected
		- Data's terms of use
		- Is the data accurate and up to date?
		- Sensitive personally identifiable information data
- Process Governance:
	- Process governance focuses on formalizing MLOps steps and associating actions with them
	- => Ensure all considerations is made at correct time and acted correctly
	- => Enable overview from outside MLOps process


# Part II: MLOps: How

## Chapter 4: Developing Models

![[Images/AI_in_production/Book_Intro_MLOps_develop_models.png]]


### TLDR

- What Is a Machine Learning Model?
	- In theory:
		- ML model is an approximate representation of some aspects of a real thing or process
	- In reality:
		- ML model is a set of all parameters necessary for rebuild and apply the representation formula
	- Required Components:
		- Training data
		- A performance metric
		- ML algorithm 
		- Hyperparameters
		- Evaluation dataset
	- Different ML Algorithms, Different MLOps Challenges
		- Linear:
			- Linear regression
			- Logistic regression
			- => Easy to overfitting
		- Tree-based:
			- Decision tree
			- Random forest
			- Gradient boosting
			- => Unstable, difficult to understand
		- Deep learning
			- Neural networks
			- => Hardest to understand
			- => Require a lot of time and data to train
- Data exploration
	- Domain knowledge is required in this step
	- Data exploration process:
		- Documenting data collection process and assumptions
		- Data statistics => Mistake and strange outliers
		- Data distribution
		- Data augmentation
		- Data statistics exploration
		- Comparing with others
- Feature engineering and selection
	- Feature engineering categories: 
		- Exiting information => New information
		- Add new information
		- Same information presented differently
		- Feature link with feature
	- Feature engineering technique
		- There is a market for complementary data
		- Impact coding can be used to deal with unavailable features
		- There are some techniques to encode features:
			- One-hot coding
			- Embedding
			- Embedding from transfer learning
	- How feature selection impacts MLOps strategy
		- Adding more features may come with some downsides
		- Automatic feature selection:
			- Input selection
			- Input encoding
			- Model interaction between inputs
		- Manual feature selections:
			- Collecting more information
			- Business-friendly features
		- Feature stores with offline and online parts is a good add-on
- Experimentation
	- Goals:
		- Finding best model with specific building blocks
		- Finding best modeling parameters
		- Tuning bias/variance trade-off
		- Finding a balance between improvement and computation costs
	- Each experiment should have an time, computation budget and acceptability usefulness threshold
	- All experiments, assumptions and conclusions need to be documented
- Evaluation and comparing models
	- No model is perfect and a near perfect model is suspicious
	- Each task needs a baseline to set goal for newer models
	- Choosing evaluation metrics:
		- Trade-off between metrics (maths) and effectiveness (business)
	- Cross-Checking Model Behavior:
		- Cross checking different metrics
		- Checking model reactions to different inputs
		- Checking model behavior in each dimension (feature ❓)
	- Impact of Responsible AI on Modeling
		- Models' individual predictions are also needed to be understood
		- Popular method for individual prediction explanations:
			- Shapley value
			- Individual conditional expectation computations
		- "Fairness" is hard to achieve for ML models
- Version Management and Reproducibility
	- Version control is needed for model evaluation and comparison
	- Version management and reproducibility address:
		- Experimenting model on different "branches"
		- Repeating the experiments to get the final model
	- Model facets need to be documented and reusable:
		- Assumptions
		- Randomness
		- Data
		- Settings
		- Results
		- Implementation
		- Environment



### What Is a Machine Learning Model?

- A machine learning model = basic formula + parameters
- Parameters = Basic formula + Hyperparameters + Training Data + Training
- In theory:
	- A machine learning model is:
		- A projection of reality
		- A partial and approximate representation of some aspect (or aspects) of a real thing or process.
		- A synthetic representation of the data at the time of collection
			- It can be used to make predictions when the future looks like the past
- In practice:
	- A machine learning model is the set of parameters necessary to rebuild and apply the formula including:
		- All the data transformations
		- The parameters of the end formula
		- The possible derived data (like a classification or a decision).
	- The model is usually stateless and deterministic (i.e., the same inputs always give the same outputs, with some exceptions)
- Required Components:

| ML component         | Description                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Training data        | - Training data is usually labeled to represent what is being modeled                                                                 | 
| A performance metric | - A performance metric is what model seeks to optimize                                                                                |
| ML algorithm         | - ML models work in different ways and have different pros and cons<br>- Some algorithms are more suited to certain tasks than others |
| Hyperparameters      | - Hyperparameters are the ways that the algorithm may go to find suitable parameters for the task.                                    |
| Evaluation dataset   | - Evaluation dataset is required to evaluate how the model performs on unseen data                                                    |

- Different ML Algorithms, Different MLOps Challenges
	-  Simpler techniques usually require more costly manual feature engineering to reach the same level of performance as more complex techniques

| Algorithm type | Name              | MLOps considerations                                                                                                 |
| -------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| Linear         | Linear regression | - There is tendency for  overfitting                                                                                 |
|                | Linear regression | - There is tendency for  overfitting                                                                                 |
| Tree-based     | Decision tree     | - Model is unstable: Small changes in data can lead to a large change in decision tree                               |
|                | Random forest     | - Predictions can be difficult to understand<br>- Prediction is relatively slow                                      |
|                | Gradient boosting | - Predictions can be difficult to understand<br>- Model is unstable                                                  |
| Deep learning  | Neural networks   | - Model is the most difficult to understand<br>- Model is extremely slow to train and requires a lot of power (data) |

### Data Exploration

- Domain knowledge is required to make informed decisions during this exploration
- Data exploration process:
	- Documenting data collection process and assumptions
	- From summarizing statistics of the data:
		- Domain of each column?
		- Missing value?
		- Obvious mistakes?
		- Strange outliers?
		- No outliers?
	- Data distribution?
	- Cleaning, filling, reshaping, filtering, clipping, sampling, etc.
	- 
		- Checking correlations between the different columns
		- Running statistical tests on some subpopulations
		- Fitting distribution curves
	- Comparing the data with other data or models in the literature
		- Usual information that missing
		- Data comparably distributed?


### Feature engineering and selection:

- Features are how data is presented to a model

| Feature engineering category | Description                                     | Example                               |
| ---------------------------- | ----------------------------------------------- | ------------------------------------- |
| Derivatives                  | Infer new information from existing information | What day of the week is this date?    |
| Enrichment                   | Add new external information                    | Is this day a public holiday?         |
| Encoding                     | Present the same information differently        | Day of the week or Weekday vs weekend |
| Combination                  | Link features together                          | The size of the backlog might need to be weighted by the complexity of the different items in it                                      |

- Feature engineering techniques
	- There is a market for complementary data
	- Impact coding can be used to fill in for unavailable features
	- There are some techniques for encoding the data
		- One-hot encoding: a feature with 3 values is transformed into 3 yes/no features
		- Embedding
		- Transfer learning may provide some useful embeddings 
- How feature selection impacts MLOps strategy
	- Adding more features downsides:
		- More expensive to compute model
		- More inputs and maintenance
		- A loss of some stability
		- Privacy concerns
	- Automated feature selection can answer: Auto-sklearn or AutoML
		- Which inputs to use?
		- How to encode them?
		- How they interact or interfere with each other?
	- Other choices still require human intervention:
		- Collecting additional information might improve the model?
		- Spending time to building business-friendly features?
	-  Feature stores or feature factories:
		- Are central repositories of different features associated with business entities
		- 2 parts consistent with each other:
			- Offline part: slower, more powerful
			- Online part: quicker, more useful for real-time needs

### Experimentation

- High bias = underfitting
- High variance = overfitting
- Experimentation goals:
	- How useful and good a model can be built with specific building blocks: training data, performance metrics, ML algorithm, hyperparameters, evaluation dataset
	- Finding the best modeling parameters (algorithms, hyperparameters, feature preprocessing, etc.)
	- Tuning the bias/variance trade-off for a given training cost 
	- Finding a balance between model improvement and improved computation costs.
- There should be a time and computation budget and an acceptability usefulness threshold for experimentation.
- All experiments, assumptions and conclusions need to be documented to rerun and reexamined


### Evaluation and comparing models

- A model should not aim to be perfect but good enough to be useful
- Keeping an eye on the uncanny valley - model doing bad job for only a specific subset of cases.
- There need to be a baseline to get an idea of expected outcome for newer model
- A perfect or near-perfect model is suspicious
- Choosing evaluation metrics:
	- Understanding the limits and trade-offs of the metric (maths) and their impacts on the optimization of the model (business)
	- Validation dataset can be simple split or something else like k-fold cross validation
- Cross-Checking Model Behavior:
	- Cross-checking different metrics
	- Checking model reactions to different inputs
	- For each dimension (feature ❓), checking the difference in behaviors and metrics across different subpopulations (i.e. error rate between male and female)
- Impact of Responsible AI on Modeling
	- Depending on the situation, data scientists may also need to understand models' individual predictions
	- Popular method for individual prediction explanations:
		- Shapley value
		- Individual conditional expectation computations
	- "Fairness" is hard to achieve for ML models


### Version Management and Reproducibility

- Version control is needed for model evaluation and comparison
- Version management and reproducibility address:
	- Experimenting model on different "branches"
	- Repeating the experiments to get the final model
- Model facets need to be documented and reusable:
	- Assumptions
	- Randomness
	- Data
	- Settings
	- Results
	- Implementation
	- Environment



## Chapter 5: Preparing for production

![[Images/AI_in_production/Book_Intro_MLOps_preparing_for_production.png]]

###


























#

# Need to learn more

- Business decision modeling techniques can help here. (Part 1, chapter 2, Data scientist)

- Create your own scorecard (set of questions to satisfy all needs)

# 

---
Status: #writing

Tags: #mlops #machine_learning 

References:
-  

Related:
- 
