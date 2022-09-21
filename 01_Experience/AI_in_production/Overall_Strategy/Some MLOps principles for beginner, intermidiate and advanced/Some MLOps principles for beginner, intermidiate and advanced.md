# Beginner
- Beginner: use pre-commit hooks. ML code is so, so ugly. Start with the basics — black, isort — then add pydocstyle, mypy, check-ast, eof-fixer, etc. Honestly I put these in my research codebases too, lol
- Beginner: always train models using *committed* code, even in development. This allows you to attach a git hash to every model. Don’t make ad hoc changes in Jupyter & train a model. Someday someone will want to know what code generated that model…
- Beginner: use a monorepo. Besides known software benefits (simplified build & deps), a monorepo reduces provenance & logging overhead (critical for ML). I’ve seen separate codebases for model training, serving, data cleaning, etc & it’s a mess to figure out what’s going. on
- Beginner: version your training & validation data! Don’t overwrite train.pq or train.csv, because later on, you may want to look at the data a specific model was trained on.
- Beginner: put SLAs on data quality. ML pipelines often break bc of some data-related bug. There are preliminary tools to automate data quality checks but we can't solely rely on them. Have an on-call rotation to manually sanity-check the data (eg look at histograms of cols)


# Intermidiate
- Intermediate: put *some* effort into ML monitoring. Plenty of ppl are like, “oh we have delayed labels so we don’t monitor accuracy.” Make an on-call rotation for this: manually label a handful of predictions daily, and create a job to update the metric. Some info > no info
- Intermediate: retrain models on a cadence (eg monthly) rather than when a KL divergence for an arbitrary feature arbitrarily drops. A cadence is less cognitive overhead. Do some data science to identify a cadence and make sure a human validates the new model every rotation

	
# Advanced
- Advanced: shadow a less-complicated model in production so you can easily serve those predictions with one click if the main model goes down / is broken. ML bugs can take a while to diagnose so it’s good to have a reliable backup
- Advanced: put ML-related tests in CI. You can do almost anything in Github Actions. Create test commands that: overfit your training pipeline to a tiny batch of data, verify data shapes, check integrity of features, etc. Whatever your product needs.



# 

---
- Status: #done

- Tags: #mlops #production 

- References:
	- [Source](https://twitter.com/sh_reya/status/1521903041003225088)

- Related:
	- 
