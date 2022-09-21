# Padding for 2D matrix

## Example:
- Sliding window
$$
x[i] = [6, 2]
$$

- Input:
$$
h[i] = [1, 2, 5, 4]
$$
## Full padding

- Padded input:
$$
h[i] = [0, 1, 2, 5, 4, 0]
$$
- Result:
$$
[6, 14, 34, 34,  8]
$$

## Same padding
-  Try to pad evenly left and right, but if the amount of columns to be added is odd, it will add the extra column to the right
- Padded input:
$$
h[i] = [0, 1, 2, 5, 4]
$$
- Result:
$$
[6, 14, 34, 34]
$$

## Valid padding
- Only drop the right-most columns (or bottom-most rows).
- Padded input:
$$
h[i] = [1, 2, 5, 4]
$$
- Result:
$$
[14, 34, 34]
$$










# 

---
- Status: #writing

- Tags: #basic_ai_knowledge #machine_learning 

- References:
	- [Source](https://www.geeksforgeeks.org/types-of-padding-in-convolution-layer/)

- Related:
	- 