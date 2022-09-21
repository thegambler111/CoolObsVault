# Definition

- A system that gives suggestions / recommendations to users. 
	- Suggestions should be meaningful
	- Not only algorithms!
	- What to know: Architecture, Process, Data, Algorithm, Testing, Evaluation and Monitoring

- Recommendation system pros
	- Companies:
		- Encourage customers to consume
		- Satisfy customers => Increase loyalty
	- Customers:
		- Personalization
		- Not be spammed!
		- Time-saving


# Data
## Types of data

- Demographic
	- Data about user’s characteristics
- Historical
	- Behavior of user in history
- Content
	- Data about items
- Context
	- Context where users consume items, such as time, location, weather, …

# Algorithm

## Non-personalized recommendation
- Make recs based on rating or editor’s knowledge. No personalization
	- It is easy to be implemented.
	- We do not have enough data about users.
	- The system is not ready for personalized recommendation.

## Personalized recommendation

## Formal Model

- X= set of Customers 
- S= set of Items
- Utility function: X×S -> R
	- R = set of ratings
	- R is a totally ordered set
	- e.g., 1-5 stars, real number in $[0,1]$

## Utility Matrix
- Utility Matrix is rating matrix of set of customers X for set of items S

### Key Problems
- How to collect the data for the utility matrix
	- Explicit rating
		- Rating that users give to items
			- Not always available!
			- Can be manipulated!
		- The matrix might be too sparse
			- => We should use multiple types of behavior to establish the user-item matrix
			- ![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/2_Recommendation System/Generate explicit rating.png]]
	- Implicit rating
		- Are collected by monitoring user’s behaviors
		- Contains various types of data about users.
- Extrapolating unknown ratings from the known ones
	- Utility matrix U is sparse
	- Cold start:
		- New items have no ratings
		- New users have no history
- Evaluating extrapolation methods

# Content-based Recommendation System
## Definition
- Recommend to customer x items similar to previous items rated highly by x
- For each item, create an item profile

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/2_Recommendation System/Content-based Recommendation System.png]]

## Text Features
- Profile = set of important words in item (document)
- Use TF-IDF

- TF:
	- Dividing by $max_k f_{kj}$ to normalize
- IDF:
	- Using log to reduce 
	- IDF is used to reduce the importance (weight) of frequently used words that does not give much meaning like "to", "the", ...
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/2_Recommendation System/TF-IDF.png]]

## User profile
- Simple approach:
	- Each rated items has weight = rating
	- User profile = average of (item weight x item profile)

- Using cosine similarity of user and item profiles to give recommendation
	- Cosine similarity calculate the distance between 2 vectors
		- The closer the 2 vectors, the more likely they are

## Pros
- No need for data on other users
	- No item cold-start problem, no user sparsity problem
- Able to recommend to users with unique tastes
- Able to recommend new & unpopular items
- Able to provide explanations


## Cons
- Finding the appropriate features is hard
- Hard to build profile for new users
- Overspecialization
	- Never recommend items outside user’s content profile
	- People might have multiple interests
	- Unable to exploit quality judgments of other users

# Collaborative Filtering
- Idea: 
	- Predict the opinion the user will have on the different items based on the user previous likings and the opinions of other like minded (“Similar”) users

# Collaborative Filtering: Nearest neighbor

## User-User Collaborative Filtering
- Find a set N of other users whose ratings are similar to user x’s ratings
- Estimate user x’s ratings based on ratings of users in N

### Finding Similar User
- Jaccard Similarity:
	- Problem: Ignores the value of the rating
- Cosine similarity;
	- Problem: Treats some missing ratings as negative
- Pearson correlation coefficient (Centered cosine):
	- **Normalize ratings by subtracting row mean**
		- Captures intuition better:
			- Missing rating treated as "average"
			- Handle "tough raters" and "easy raters"
		- 0 means no information

### Rating Predictions
- $r_{xi}$ = rating of user x for item i
- $S_{xy}$ = Similarity between user x and y
- $$r_{xi} = \frac{\sum_{y\in N}S_{xy}*r_{yi}}{\sum_{y\in N}S_{xy}}$$

## Item-Item Collaborative Filtering
- Similar to User-User Collaborative Filtering

- In practice, we calculate a baseline estimate for $r_{xi}$ to use as normalization


## Item-Item vs. User-User
- In Theory, user-user and item-item are dual approaches.
- In practice, item-item outperforms user-user in many use cases

## Pros
- Works for any kind of item
	- No feature selection needed

## Cons
- Cold Start: Need enough users in the system to find a match
- The user/ratings matrix is sparse
- Cannot recommend an item that has not been previously rated
- Popularity bias:
	- Cannot recommend items to someone with unique taste
	- Tends to recommend popular item

## Hybrid Filtering
- Implement two or more different recommenders and combine prediction

# Collaborative Filtering: Matrix Factorization

## Latent Factor Models

![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/2_Recommendation System/Latent Factor Models.png]]

- From rating, calculate user and item matrices
- Calculate missing rating using user and item matrices


# Evaluation and testing
## Evaluating process
![[01_Experience/AI_notes/Learning courses/Viettel Data Governance Department 20220523/2_Recommendation System/Evaluating process.png]]

## Error matrix
- Error metrics:
	- MAE/MSE/RMSE
- Ranking metrics:
- 






	



# 

---
- Status: #done

- Tags: #recommendation_system

- References:
	- 

- Related:
	- 
