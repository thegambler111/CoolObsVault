# Smaller testing scopes = Shorter feedback loops
- Here’s how the various scopes map to concrete tests:
	- Unit: Test individual methods and classes
	- Integration: Test pipeline integration points, such as between data processing and model training pipelines, or checking that trained models are deployed correctly
	- Functional: Test that business requirements are met (e.g., excluding erotica, rolling up movies from the same series, updating recs based on in-session clicks, etc.)
	- End-to-end: Test that the pipeline output/endpoint integrates correctly with the site and recommendations are served correctly based on user ID or behavior
	- Acceptance: Visual inspection and quality assurance of live recommendation slate
	- Performance: Load testing and assessing latency and throughput
	- Smoke: Handcrafted URLs to trigger recommendations on commonly QA-ed items
	- A/B: Evaluate the impact of pipeline or model changes





# 

---
- Status: #done

- Tags: #machine_learning #production #model_testing

- References:
	- [Source](https://eugeneyan.com/writing/testing-pipelines/)

- Related:
	- 
