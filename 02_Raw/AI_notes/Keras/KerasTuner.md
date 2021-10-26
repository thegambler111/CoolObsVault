# Quick tweetorial: using KerasTuner to find good model configs.

Define your model as usual -- but put your code in a function that takes a '*hp*' (hyperparameters) argument.

Then, instead of using values like "*embedding_dim = 512*", use ranges: 
'*hp.Init(...)*'

![[Images/AI_note_images/KerasTuner_hp_init.jpeg]]

Then, instantiate a tuner and pass it your model building function. It will need an '*objective*' to optimize -- this could the name be any metric found in the model logs. For built-in Keras metrics, the tuner will automatically pick whether to maximize or minimize the metric.

![[Images/AI_note_images/KerasTuner_optimization.jpeg]]

'*max_trials*' is the maximum number of model configurations to try. The ominous-sounding '*executions_per_trial*' is the number of model training runs to average for each model config: a higher value reduces results variance.

Finally, '*tuner.search()*' just mirrors '*model.fit()*'

Note that you can implement custom search logic and more advanced workflows by subclassing a tuner class and overriding the `run_trial` method.



# 

---
Status: #done 

Tags: #keras #keras_tuner

References:
- 

Related:
