# Before Machine Learning
Rule #1: Don’t be afraid to launch a product without machine learning.
Rule #2: Make metrics design and implementation a priority.
Rule #3: Choose machine learning over a complex heuristic.
# ML Phase I: Your First Pipeline
Rule #4: Keep the first model simple and get the infrastructure right.
Rule #5: Test the infrastructure independently from the machine learning.
Rule #6: Be careful about dropped data when copying pipelines.
Rule #7: Turn heuristics into features, or handle them externally.
## Monitoring
Rule #8: Know the freshness requirements of your system.
Rule #9: Detect problems before exporting models.
Rule #10: Watch for silent failures.
Rule #11: Give feature sets owners and documentation.
## Your First Objective
Rule #12: Don’t overthink which objective you choose to directly optimize.
Rule #13: Choose a simple, observable and attributable metric for your first objective.
Rule #14: Starting with an interpretable model makes debugging easier.
Rule #15: Separate Spam Filtering and Quality Ranking in a Policy Layer.
# ML Phase II: Feature Engineering
Rule #16: Plan to launch and iterate.
Rule #17: Start with directly observed and reported features as opposed to learned features.
Rule #18: Explore with features of content that generalize across contexts.
Rule #19: Use very specific features when you can.
Rule #20: Combine and modify existing features to create new features in human understandable ways.
Rule #21: The number of feature weights you can learn in a linear model is roughly proportional to the amount of data you have.
Rule #22: Clean up features you are no longer using.
## Human Analysis of the System
Rule #23: You are not a typical end user.
Rule #24: Measure the delta between models.
Rule #25: When choosing models, utilitarian performance trumps predictive power.
Rule #26: Look for patterns in the measured errors, and create new features.
Rule #27: Try to quantify observed undesirable behavior.
Rule #28: Be aware that identical short-term behavior does not imply identical long-term behavior.
## Training-Serving Skew
Rule #29: The best way to make sure that you train like you serve is to save the set of features used at serving time, and then pipe those features to a log to use them at training time.
Rule #30: Importance weight sampled data, don’t arbitrarily drop it!
Rule #31: Beware that if you join data from a table at training and serving time, the data in the table may change.
Rule #32: Re-use code between your training pipeline and your serving pipeline whenever possible.
Rule #33: If you produce a model based on the data until January 5th, test the model on the data from January 6th and after.
Rule #34: In binary classification for filtering (such as spam detection or determining interesting emails), make small short-term sacrifices in performance for very clean data.
Rule #35: Beware of the inherent skew in ranking problems.
Rule #36: Avoid feedback loops with positional features.
Rule #37: Measure Training/Serving Skew.
# ML Phase III: Slowed Growth, Optimization Refinement, and Complex Models
Rule #38: Don’t waste time on new features if unaligned objectives have become the issue.
Rule #39: Launch decisions will depend upon more than one metric.
Rule #40: Keep ensembles simple.
Rule #41: When performance plateaus, look for qualitatively new sources of information to add rather than refining existing signals.
Rule #42: Don’t expect diversity, personalization, or relevance to be as correlated with popularity as you think they are.
Rule #43: Your friends tend to be the same across different products. Your interests tend not to be.


# 

---
- Status: #done

- Tags: #production #ai_lifecycle 

- References:
	- [Source](https://twitter.com/iamtrask/status/1565294744892329984)
	- [Source2](https://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf)
	- [Related](https://developers.google.com/machine-learning/guides/rules-of-ml/)

- Related:
	- 
