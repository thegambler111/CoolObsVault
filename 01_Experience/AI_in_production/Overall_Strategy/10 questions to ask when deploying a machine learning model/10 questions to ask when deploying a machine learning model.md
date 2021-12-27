# Some questions you may have to answer every time you deploy a machine learning model
1. What's the input format expected by your service?

2. How can we validate the input is valid? What's the appropriate action if it isn't.

3. What transformations are needed to turn the service's input into the model's input?

4. What transformations are needed to turn the model's output into the service's output?

5. Do we need to allow for batch processing of data?

6. How much time do we have to return an answer?

7. What's the throughput of the service? In other words, how many requests per second can the service handle?

8. Do we need to worry about automatically scaling the service? What are the criteria to scale in and out

9. How do we automatically deploy changes in the code? How do we deploy changes in the model?

10. How do we determine when the model needs updates? (Concept and data drift?)


# 

---
- Status: #done 

- Tags: #machine_learning #mlops 

- References:
	- [Questions to ask when deploying a machine learning model](https://twitter.com/svpino/status/1461666018468716549)

- Related:
	- 