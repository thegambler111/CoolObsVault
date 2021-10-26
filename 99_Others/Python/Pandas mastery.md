# Nested dict (3 layers) to DataFrame
```python
user_dict = {12: {'Category 1': {'att_1': 1, 'att_2': 'whatever'},
                  'Category 2': {'att_1': 23, 'att_2': 'another'}},
             15: {'Category 1': {'att_1': 10, 'att_2': 'foo'},
                  'Category 2': {'att_1': 30, 'att_2': 'bar'}}}

df_test = pd.DataFrame.from_dict({(i,j): user_dict[i][j]
                           for i in user_dict.keys()
                           for j in user_dict[i].keys()},
                       orient='index')
```

``` python
# Result
               att_1     att_2
12 Category 1      1  whatever
   Category 2     23   another
15 Category 1     10       foo
   Category 2     30       bar
```

Change orient to 'columns' to swap row and column

# Change DataFrame row order

```python
# Row 'sum' is in df
# Move row 'sum' to the last line
new_index = df.index.drop('sum').tolist() + ['sum']
df = df.reindex(new_index)

```


# 

---
Status: #done

Tags: #python #dict #nested_dict #pandas #dataframe

References:
- [Reorder row](https://stackoverflow.com/a/42434256)
- [Nested dict to dataframe](https://stackoverflow.com/a/13581730)

Related:
