# Definitions
## Definition
- Relational databases imposes on the data a tabular like structure.
- Data is stored in form of table and each table represents a specific entity.
	- The columns represent attributes of the entity.
	- The rows (or records) are instances of the entity.

## Schema
- All tables are defined according to a specific schema (a set of rule) and every record needs to be conform to the schema.

## SQL
- Most of relational databases support SQL (Structured Query Language). 
	- SQL enables powerful queries to retrieve data on relational databases.
- Theoretically it is possible to implement complex queries using a programming language
	- However, it is impossible with huge data as you need to load them in memory


# ACID transaction

- It is a combination of operations that satisfy 4 properties: 
	- Atomicity: 
		- All the operations are treated as a unit and they will all succeed or fail
		- If only 1 fails then all fail, the entire transaction is rolled back
	-  Consistency:
		- Any transaction shall be conform to the database rules 
		- Any future transaction will always take into account any past one. 
	- Isolation: 
		- Multiple transactions can occur at the same time but are executed as they occurred sequentially.
	- Durability: 
		- The effect of a transaction is permanent.



# Database indexes
- An index is an additional data structure in the database that is optimized for fast searching on a specific attribute in a table.

- This data structure stores the attribute entries in sorted order, pointing them to the corresponding row in the original table.

- Query time is reduce from O(N) to O(log N) or O(1) 

- The trade off are:
	- The additional data structure take up more space
	- Every write operation is a bit slower because of updating the index


# When to chose relational DB

## Powerful queries
- First when you need to execute very powerful queries to retrieve data (i.e. multi-rows SQL transactions). 
- Non relational DB have their own query language, but this not always support complicated types of queries like SQL.

## Strong consistency
- Second when you need strong consistency on your data. 
- For example, when you make an update in the DB you want to immediately see these updates reflected everywhere.
- Non relational DB are usually not fully ACID compliant and guarantee only eventual consistency.




# 

---
- Status: #done 

- Tags: #database

- References:
	- [Source](https://twitter.com/Franc0Fernand0/status/1486731467933683728)

- Related:
	- 
