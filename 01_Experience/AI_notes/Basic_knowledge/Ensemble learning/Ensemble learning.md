# Bagging vs Boosting

![[01_Experience/AI_notes/Basic_knowledge/Ensemble learning/Bagging vs Boosting.png]]

| Similarities                                                                               | Differences                                                                                                                                           |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Both are ensemble methods to get N learners from 1 learner                                 | but, while they are built independently for Bagging, Boosting tries to add new models that do well where previous models fail.                        |
| Both generate several training data sets by random sampling                                | but only Boosting determines weights for the data to tip the scales in favor of the most difficult cases.                                             |
| Both make the final decision by averaging  the N learners (or taking the majority of them) | but it is an equally weighted average for Bagging and a weighted average for Boosting, more weight to those with better performance on training data. |
| Both are good at reducing variance and provide higher stability                            | but only Boosting tries to reduce bias. On the other hand, Bagging may solve the over-fitting problem, while Boosting can increase it                 |
|                                                                                            |                                                                                                                                                       |





# 

---
- Status: #done 

- Tags: #ai_training #ensemble_learning

- References:
	- 

- Related:
	- 