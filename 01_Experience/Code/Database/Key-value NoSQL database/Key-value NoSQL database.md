# Definition
- These databases behave much like hash tables data structures. 
- They store collections of key-value pairs, mapping from keys to arbitrary values.
- Both keys and values can be anything, ranging from simple objects like strings to complex compound objects.


# Pros
- Flexibility: no structure is imposed on the values
- Simplicity: is the less complex to use type of NoSQL database
- Speed: accessing values directly through keys means lower latency and higher throughput in the parts of the system where they're used
- Portability: easy to migrate between different systems
- Scalability: highly horizontally scalable compared to relational databases

# Cons
- No query support: 
	- Values can't be filtered using queries
	- After a request/update the whole value is returned/updated
- Mobility: without a unified query language, requests from a database may not be transportable to another key-value database


# Use cases
- Cache frequently accessed data (i.e. responses to network requests) and access them using a hash (i.e. IP address or username)
- Store special configuration parameters used across the system
- Access real time random data like user session attributes in web applications. 
	- Sessions are marked with identifiers and all data recorded about each session are associated to their id.

# Popular implementations
- Dynamo DB:  probably the most widely used key-value storage. Fully managed and serverless, It is part of the AWS portfolio.
- Zookeeper: a strongly consistent, high available key-value storage often used for dynamic configuration
- Redis: an in memory key-value storage. It offer some persistent storage option but used typically as fast, best effort caching solution.
- Etcd: a strongly consistent, high available key-value storage often used for implementing leader election.



# 

---
- Status: #done

- Tags: #database 

- References:
	- [Twitter Source](https://twitter.com/Franc0Fernand0/status/1491454365147803649)

- Related:
	- 
