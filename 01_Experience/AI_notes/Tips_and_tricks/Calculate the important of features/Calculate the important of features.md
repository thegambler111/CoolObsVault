# Leave-one-out feature importance (LOFO) + LightGBM
- Most data scientists use linear/logistic regression to figure out which features are important in a dataset
- Instead, I generally use leave-one-out feature importance (LOFO) + LightGBM.

## Correlated features
- Linear models struggle to provide useful insights when dealing with correlated features.
	- Out-of-the-box GBDT feature importance can also fall prey to this
- LOFO removes that worry by grouping correlated features together

## Negative feature importance
- If you overload your models with features, it will hurt performance.
- LOFO actually assigns negative importance to those features.

## Strong generalization
- Since LOFO is calculated over your cross-validation splits, it provides strong estimates of true importance.
- Plus, you get a variance for each importance score to see if it ever drops into the negatives.

# Permutation importance vs LOFO
| Permutation importance    | LOFO                |
| ------------------------- | ------------------- |
| Uses a trained model      | Re-trains the model |
| More time efficient       | More accurate       |
| Can get unrealistic input |                     |

- You can try FLOFO (fast LOFO) as an alternative

#
---
- Status: #done
- Tags: #tips_and_tricks #machine_learning
- References:
	- [Source](https://twitter.com/marktenenholtz/status/1577992133079756801)
- Related:
