# Key takeaways by Sergios Karagiannakos

- ML systems fail due to both software system failures such as dependency errors, deployment errors, hardware errors, and ML-specific failures such as data distribution shifts and degenerate feedback loops.
- When designing feedback loops, one should be aware of the feedback loop length and the fact that the predictions themselves can influence the feedback (degenerate feedback loops).
- Data distribution shifts can happen due to covariate shift, label shift or concept drift depending on which data distribution changes (input data, output data, or their relationship).
- Data distribution shifts can be detected with two-sample hypothesis tests.
- The most common approach to solve distribution shifts is to retrain your model from scratch or fine-tune it using labeled data from the target distribution
- Monitoring and Observability are essential to detecting ML system failures. Measuring operational metrics( error rate, downtime etc) and ML-specific metrics (accuracy, features) when combined with logs and dashboards, makes all the difference in the world.

# Distribution shifts: Venn diagram by Charles Frye

- https://twitter.com/charles_irl/status/1497412218928779267


# 

---
- Status: #writing

- Tags: #Model_deployment #machine_learning #drift_in_ml 

- References:
	- [Source](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html)[Twitter source](https://twitter.com/chipro/status/1490924046350909442)
	- [Source for Key takeaways](https://twitter.com/KarSergios/status/1491410606746136581)
	- [Source for Venn diagram](https://twitter.com/charles_irl/status/1497412218928779267)

- Related:
	- 
