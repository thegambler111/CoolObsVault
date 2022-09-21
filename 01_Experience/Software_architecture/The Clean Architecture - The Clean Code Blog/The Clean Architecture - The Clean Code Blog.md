# Previous ideas regarding the architecture of systems
- 
	-   [Hexagonal Architecture](http://alistair.cockburn.us/Hexagonal+architecture) (a.k.a. Ports and Adapters) by Alistair Cockburn and adopted by Steve Freeman, and Nat Pryce in their wonderful book [Growing Object Oriented Software](http://www.amazon.com/Growing-Object-Oriented-Software-Guided-Tests/dp/0321503627)
	-   [Onion Architecture](http://jeffreypalermo.com/blog/the-onion-architecture-part-1/) by Jeffrey Palermo
	-   [Screaming Architecture](http://blog.cleancoders.com/2011-09-30-Screaming-Architecture) from a blog of mine last year
	-   [DCI](http://www.amazon.com/Lean-Architecture-Agile-Software-Development/dp/0470684208/) from James Coplien, and Trygve Reenskaug.
	-   [BCE](http://www.amazon.com/Object-Oriented-Software-Engineering-Approach/dp/0201544350) by Ivar Jacobson from his book _Object Oriented Software Engineering: A Use-Case Driven Approach_
- Each of these architectures produce systems that are:
	-  Independent of Frameworks. 
		- Does not depend on some library of feature laden software. This allows you to use such frameworks as tools, rather than having to cram your system into their limited constraints.
	-  Testable. The business rules can be tested without the UI, Database, Web Server, or any other external element.
	-  Independent of UI. The UI can change easily, without changing the rest of the system. A Web UI could be replaced with a console UI, for example, without changing the business rules.
	-  Independent of Database. You can swap out Oracle or SQL Server, for Mongo, BigTable, CouchDB, or something else. Your business rules are not bound to the database.
	-  Independent of any external agency. In fact your business rules simply don’t know anything at all about the outside world.

# 
![[Images/Clean_architecture/clean_code_blog_clean_architecture.png]]





# 

---
Status: #writing

Tags: #code_architecture #clean_code

References:
-  [The Clean Architecture - The Clean Code Blog](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Related:
- 
