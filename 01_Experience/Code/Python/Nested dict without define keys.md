#
```python
from collections import defaultdict
mydict = lambda: defaultdict(mydict)
result = mydict()
result['Python']['rules']['the world'] = "Yes I Agree"
result['Python']['rules']['the world']
```
> 'Yes I Agree'


# 

---
Status: #done

Tags: #python #dict #nested_dict

References:
- [Source](https://stackoverflow.com/a/20411103)

Related:
