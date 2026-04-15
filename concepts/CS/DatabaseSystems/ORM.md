# Object Relational Mapping

## Definition
> Object Relational Mapping(ORM) is a technique that is used to map relational database schemas to objects in programming langauges. This technique abstracts away writing the raw sql queries and handles all db operations in the backend by reflection/declaration(metadata) and translation of operations into sql queries, user just calls member functions on the objects. 

## Caution
- If not configured properly the ORM can cause inefficient DB operations like N+1 problem.
- N + 1 problem is when one query is used to fetch data from one table which contain foreign key to other table. If not configured properly then the ORM can run one query for fetching data from one table and N other queries for each row returned to fetch data from the other table. Most ORM provide solution to this by automatically joining two tables called eager loading.
- Object relational impedance mismatch: Objects and tables are different. So mapping "is a" relationship hierarchies to objects can cause inefficient performance.

