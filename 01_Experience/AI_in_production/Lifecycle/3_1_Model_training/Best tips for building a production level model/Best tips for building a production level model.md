# TLDR
1. Evaluation = speed
2. GPUs everywhere
3. Limit your architectures
4. Kaggle solutions are a DB
5. Refactor more
6. Pipelines > models

# Model evaluation is the best time saver
Experiments done with a bad evaluation strategy are a waste of time.
Conversely, a good evaluation setup is the most powerful tool for iterating to a good solution.
This is arguably the highest-leverage time investment in an ML project.

# Use a GPU wherever you can

- [@RAPIDSai](https://twitter.com/RAPIDSai)is an absolute blessing.
- For 95% of my tabular problems, I can change 2 lines of code to make the whole thing run on my GPU. 
- Everything from feature engineering to model training.
- I've seen instances where this speeds pipelines up by 50x.


# Skip to the good models
- For any given problem, there are 3-5 model architectures you should focus (unless you have a really good reason).
- The less time you're playing with models, the more time you're spending on high-leverage tasks (feature engineering, data exploration).


# Pick 1 model and max it out
- Your first goal should be to take one of those 3-5 models and improve it until you can't anymore.
- On image tasks, I usually start by improving efficientnet-b0 until I can't anymore.
- On tabular tasks, it's usually LightGBM or a random forest.

# Reuse old Kaggle solutions
- Kaggle solutions are like a database for battle-tested solutions.
- If you have a similar enough problem to an old competition, those solution writeups are an absolute goldmine.
- My first stop on any problem for "literature review" is Kaggle.


# Create your own framework
- 99% of my projects follow the exact same structure.
- Down to the names of the files, what goes in them, and when they are created.
- It's probably not the most efficient setup, but having such a deep knowledge of the structure makes me work much faster.


# Refactor, refactor, refactor
- ML code can get out of hand really quickly.
- With rapid iteration comes a rapid mess.
- Don't be afraid to spend 30 minutes cleaning up your code instead of training models.

# Pipelines > models
- Most of the code that goes into training ML models is written either for getting the data to the model or getting the predictions out.
- Want fast and reliable models? Spend more time improving your pipelines.


# 

---
- Status: #done

- Tags: #production 

- References:
	- [Source](https://twitter.com/marktenenholtz/status/1565308627145019392)

- Related:
	- 
