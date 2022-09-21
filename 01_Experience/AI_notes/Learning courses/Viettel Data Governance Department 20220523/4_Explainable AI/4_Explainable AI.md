# TLDR
- Model-specific methods:
	- Linear regression
	- Logistic regression
	- Decision tree
- Model-agnostic methods:
	- Partial Dependence Plot (PDP)
	- Individual Conditional Expectation (ICE)
	- Accumulated Local Effects (ALE)
	- Permutation feature importance
	- Global surrogate
	- LIME
	- SHAP
- Example-based explanation:
	- Counterfactual explanation
	- Adversarial example
	- Influential instances
- Neural network interpretation:
	- Learned features
	- Pixel attribution
	- Detecting concepts


# Interpretability
- Interpretability is the degree to which a human can
	- Understand the cause of a decision.
	- Consistently predict the model's result.


# Methods for machine learning interpretability

- Intrinsic interpretability: models that are considered interpretable due to their simple structure
- Post hoc interpretability refers to the application of interpretation methods after model training

- Model-specific interpretation tools are limited to specific model classes
- Model-agnostic tools can be used on any machine learning model and are applied after the model has been trained (post hoc).

- Local interpretation method explain an individual prediction.
- Global interpretation method explain the entire model behavior.


# Model-specific methods
## Linear regression
- Function: $$\hat{y}^{(i)} = \beta_0 + \beta_1*x_1^{(i)} + ... + \beta_p*x_p^{(i)} + \epsilon$$

- $R^2$ is used to evaluate model
- In practice, $R^2 \in [0.7, 0.9]$ can be consider a good model

### Predict the number of rented bicycles
- Table of features and their estimated weights, standard errors (SE) and t-statistic: ![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/4_Explainable AI/Predict the number of rented bicycles.png]]

- $num\_of\_rented\_bikes = intercept\_weight + weight_i*feature\_value_i$
- Standard errors (SE)
- t-statistic: $|t| = \frac{estimated\_weight}{SE(estimated\_weight)}$
- The importance of a feature in a linear regression model can be measured by the absolute value of its t-statistic
- The importance of a feature increases with increasing weight.
- The more variance the estimated weight has (= the less certain we are about the correct value), the less important the feature is.

### Visual interpretation
- Weight plot: ![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/4_Explainable AI/Linear regression visual interpretation weight plot.png]]
	
	- Features with weight that may be 0 is not always affect the number of rented bikes
		- **In practice**, those features are usually removed

- Effect plot: ![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/4_Explainable AI/Linear regression visual interpretation effect plot.png]]

- Effect: $effect_j^{(i)}=weight_j*feature\_value_j^{(i)}$
- This is box plot
- This plot can be used to explain individual prediction

- Pros:
	- Simple to interpret
- Cons:
	- Unintuitive because of correlation between features (e.g. season and temperature)


## Logistic regression
- Function: $$P(\hat{y}^{(i)}=1) = \frac{1}{1+exp(-(\beta_0 + \beta_1*x_1^{(i)} + ... + \beta_p*x_p^{(i)}))}$$
- Odds ratio: $$\frac{P(y=1)}{1-P(y=1)} = exp(-(\beta_0 + \beta_1*x_1^{(i)} + ... + \beta_p*x_p^{(i)}))$$
	- OR $$P(y=1) = \frac{1}{1+odds\_ratio}$$
	- A change in a feature by one unit changes the odds ratio (multiplicative) by a factor of $e^{weight}$
		- => Changes predicted value by $$\frac{1}{1+e^{weight}}$$

- Pros:
	- Can be used for classification problem
- Cons:
	- The interpretation is more difficult because the interpretation of the weights is multiplicative and not additive

## Decision tree
 - Feature importance: how much a feature has reduced the Gini impurity/ variance/ squared error/… through all the splits.
	 - The sum of all importance is scaled to 100

- Reduced squared errors = $$(left\_leaf\_num\_samples/branch\_num\_samples)*(branch\_squared\_errors - left\_leaf\_squared\_errors) + (right\_leaf\_num\_samples/branch\_num\_samples)*(branch\_squared\_errors - right\_leaf\_squared\_errors)$$

 - Pros:
	- Capturing interactions between features in the data
	- Create good explanations
- Cons:
	- Fail to deal with linear relationships
	- Unstable
	- Lack of smoothness

# Model-agnostic methods
## Partial Dependence Plot (PDP)
- Goal: shows the marginal effect one or two features have on the predicted outcome of a machine learning model
- Calculation: using Monte Carlo method:
	- Freeze all features on an instance except one
	- Calculate the prediction while changing that one feature
	- Change the instance and repeats (may repeat a number of time till you get a reasonable outcome)

- Pros:
	- Interpretation is clear
	- Easy to implement
- Cons:
	- Realistic maximum number of features in PDP is two
	- Big problem with assumption of independence
	- Heterogeneous effect might be hidden


## Individual Conditional Expectation (ICE)

- Goal: shows how the instance's prediction changes when a feature changes (one line per instance)
	- In practice, you only use this method to observe a small amount of instances

- Pros:
	- More intuitive to understand than partial dependence plots
	- Can uncover heterogeneous relationships
- Cons:
	- Can only display one feature meaningfully
	- Some points in the lines might be invalid data points
	- Plot can become overcrowded
	- Not be easy to see the average

## Accumulated Local Effects (ALE)
- Plot how the model predictions change in a small "window" of the feature around v for data instances in that window.

- Pros:
	- Unbiased
	- Faster to compute than PDP 
	- Clear interpretation
- Cons:
	- Become a bit shaky
	- Not accompanied by ICE curves
	- Implementation is much more complex
	- Interpretation remains difficult when features are strongly correlated

## Permutation feature importance
- Idea: Changing only 1 feature of all instances, if the model error changes much -> that feature is importance

## Global Surrogate
- A global surrogate model is an interpretable model that is trained to approximate the predictions of a black box model. 
	- => Draw conclusions about the black box model by interpreting the surrogate model

- Pros:
	- Flexible
	- Intuitive
- Cons:
	- Conclusions is about the model, not about the data
	- No intrinsically interpretable models

## Local Surrogate
- Similar to global surrogate but instead of using all instances and features, it only uses a small neighborhood around an instance and a subset of features
	- Features in the subset should be relatable

- Pros:
	- Explanations are short (=selective) and possibly contrastive
	- Work for tabular data, text and images
	- Can use other (interpretable) features than the original model was trained on
- Cons:
	- The correct definition of the neighborhood is a very big, unsolved problem
	- The explanations are unstable

## Shapley values
- Idea: How a feature contributes to the prediction compared to the average prediction
	- Can be used for black box model
- Steps for calculation of Shapley value of feature xi:
	- 1. List all possible coalitions of features, except the feature xi. 
	- 2. For each of these coalitions we compute the target with and without the feature value xi and take the difference to get the marginal contribution.
	- 3. Calculate the (weighted) average of marginal contributions to get Shapley value of feature xi.

## SHAP (SHapley Additive exPlanations)
- Goal: explain the prediction of an instance x by computing the contribution of each feature to the prediction.








# 

---
- Status: #done

- Tags: #explainable_ai 

- References:
	- 

- Related:
	- 
