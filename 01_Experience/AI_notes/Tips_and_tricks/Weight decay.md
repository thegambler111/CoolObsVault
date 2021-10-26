#


# Weight_decay
0.3 is best with lr = 3e-3 in fastai experience
Implement of weight decay like in https://www.fast.ai/2018/07/02/adam-weight-decay/

```python
for group in optimizer.param_groups:
	for param in group['params']:
		param.data = param.data.add(- weight_decay * group['lr'], param.data)
```


# 

---
Status: #done 

Tags: #training #weight_decay #pytorch #tips_and_tricks #hyperparameter 

References:
- 

Related:
