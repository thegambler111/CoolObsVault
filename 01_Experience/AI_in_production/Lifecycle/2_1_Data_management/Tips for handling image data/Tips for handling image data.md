# 1. Consider how the data is captured
- Is it fixed cameras?
- Is the hardware standard?
- Are illumination conditions the same across the board?
- Are all pictures taken from the same angle?
- Is the quality of the images roughly the same?


# 2. Consider the frequency of new images coming in
- How much do you need to scale to process new images?
- How do you store the images? How about security and privacy? 
- How fast will data drift impact your model? How frequently do you need to retrain it?

# 3. Is there necessary metadata associated with them
- How do you process that metadata? How do you store it and secure it?
- Is "time" an essential factor in processing the images and the data?


# 4. Consequences of failing
- What are the consequences of your model failing to recognize anything?
- What are the consequences of your model recognizing the wrong object?

# 5. Best trade-off
- What's worse, a False Positive or a False Negative? 
- How do you optimize your model to ensure it is cost-effective and does no harm?



> You can tell how well a data scientist understands their image data by how they augment it during training.


# 

---
- Status: #done

- Tags: #computer_vision #data_analysis 

- References:
	- [Source](https://twitter.com/svpino/status/1520010034331066368)

- Related:
	- 
