# CSE304 / DBMS

## Syllabus

{% file src="../.gitbook/assets/CSE304 DBMS Syllabus BTECH-IT.pdf" %}

## Resources

<details>

<summary>M1: Introduction to DBMS</summary>

* Concept and Goals of DBMS
  * Definition of DBMS
  * Goals of DBMS (e.g., data independence, consistency, security, etc.)

- Database Languages
  * Data Definition Language (DDL)
  * Data Manipulation Language (DML)
  * Data Control Language (DCL)
  * Transaction Control Language (TCL)

* Database Users
  * End users
  * Database administrators (DBAs)
  * Application developers

- Database Abstraction
  * Levels of abstraction (physical, logical, and view)
  * Data independence (physical and logical)

* Entity-Relationship (ER) Model
  * Basic Concepts of ER Model
    * Entities, Attributes, Relationships
    * Keys: Primary, Foreign, Candidate
  * Relationship Sets: One-to-one, One-to-many, Many-to-many
  * Keys: Superkey, Candidate key, Primary key, Foreign key
  * Mapping: Cardinality and participation constraints
  * Design of ER Model
  * Generalization, Aggregation, and Specialization in ER Models
  * Transforming ER Diagram into Tables

- Other Data Models
  * Object-Oriented Data Model
  * Network Data Model
  * Relational Data Model

</details>

<details>

<summary>M2: Relational Data models</summary>

* Fundamentals of Relational Model
  * Domains: Set of valid values for an attribute
  * Tuples: Rows in a table
  * Attributes: Columns in a table
  * Relations: Tables
  * Characteristics of Relations: Uniqueness, order, etc.

- Keys and Attributes of Relation
  * Primary Key
  * Candidate Key
  * Foreign Key
  * Superkey

* Relational Database Concepts
  * Schemas: Logical design of the database
  * Integrity Constraints
    * Entity Integrity
    * Referential Integrity
  * Intension and Extension: Schema vs. actual data
  * Relational Query Languages
    * SQL (Structured Query Language)
      * DDL (Data Definition Language): CREATE, ALTER, DROP
      * DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE
      * Integrity Constraints: Not Null, Unique, Primary Key, Foreign Key
      * Complex Queries
      * Joins: Inner join, Outer join (left, right, full)
      * Indexing: B-tree indexing, Hash indexing
      * Triggers: Event-based actions in response to DML operations

- Relational Algebra and Relational Calculus
  * Relational Algebra Operations:
    * Select, Project, Join, Union, Difference, Intersection
    * Division Operation
  * Tuple Relational Calculus

</details>

<details>

<summary>M3: Data Base Design</summary>

* Database Design and Normalization
  * Introduction to Normalization
  * Normal Forms: 1NF, 2NF, 3NF, BCNF, 4NF, 5NF
  * Functional Dependency
  * Decomposition: Breaking relations into smaller, well-structured relations
  * Dependency Preservation: Ensuring all functional dependencies are maintained after decomposition
  * Lossless Join: Property of decomposition where original relation can be reconstructed without data loss
  * Null-Valued and Dangling Tuples: Issues and handling
  * Multivalued Dependencies

</details>

<details>

<summary>M4: Transaction Processing Concepts</summary>

* Transaction System
  * Definition of a Transaction
  * ACID Properties (Atomicity, Consistency, Isolation, Durability)

- Serializability
  * Testing of Serializability
  * Conflict and View Serializable Schedules

* Recoverability
  * Recovery from Transaction Failures
  * Log-Based Recovery: Write-Ahead Logging (WAL)
  * Checkpoints: Savepoints for recovery

- Concurrency Control Techniques
  * Locking Techniques: Two-Phase Locking (2PL), Deadlock Detection
  * Timestamping Protocols: Ensuring serializability through timestamps
  * Validation-Based Protocol: Ensuring transactions are serializable without locks
  * Multiple Granularity: Locking at different levels of granularity (e.g., row, page, table)
  * Multiversion Schemes: Creating multiple versions of data to allow concurrency
  * Recovery with Concurrent Transactions

</details>

<details>

<summary>M5: Relational DBMS</summary>

* Introduction to RDBMS
  * Study of RDBMS (e.g., Oracle, PostgreSQL, MySQL)
  * RDBMS Architecture
    * Physical Files
    * Memory Structures
    * Background Processes

- Database Storage Concepts
  * Table Spaces: Logical storage units in a database
  * Segments, Extents, and Blocks: Physical storage units
  * Dedicated Server vs. Multi-threaded Server
  * Distributed Database: Concepts and architecture

* Introduction to SQL
  * ANSI SQL: Standard SQL syntax
  * SQL Commands and Operators
    * LIKE, ANY, ALL, EXISTS
    * Views: Creating and using views in SQL
    * Special Operators: IN, BETWEEN, IS NULL, etc.
    * Hierarchical Queries: Using CONNECT BY (in Oracle), recursive queries
    * Inline Queries: Subqueries within SELECT, INSERT, etc.
    * Flashback Queries: Retrieving previous versions of data in databases like Oracle

</details>

## Notes

\[⤓] [CSE304 DBMS Topics Extract](https://drive.google.com/file/d/1PJqtgV_XchcPUUmRwe7mYeGgiyt25Nft/view?usp=drive_link)

{% embed url="https://drive.google.com/file/d/1PJqtgV_XchcPUUmRwe7mYeGgiyt25Nft/view?usp=drive_link" %}

## Question Directory

### Previous Year Questions

\[⤓] [Midsem-CSE304-Y2S3-BTECH-CSE-IT-OCT24](https://drive.google.com/file/d/1HF3IF_yj4V7zaVjgDvEQ9N9E77KII4kA/view?usp=drive_link)

{% embed url="https://drive.google.com/file/d/1HF3IF_yj4V7zaVjgDvEQ9N9E77KII4kA/view?usp=drive_link" %}

\[⤓] [CSE304-PYQ-BTECH-CSE-IT-Sem3Dec23](https://drive.google.com/file/d/10eVRAxshOVndIh51LzoOwLyzvEhuCyjR/view?usp=drive_link)

{% embed url="https://drive.google.com/file/d/10eVRAxshOVndIh51LzoOwLyzvEhuCyjR/view?usp=drive_link" %}

\[⤓] [CSE304-PYQ-BTECH-CSE-IT-Sem3Dec24](https://drive.google.com/file/d/1ceUaYM0lUefMrIbdrPLCq_2Eto2JO5tn/view?usp=drive_link)

{% embed url="https://drive.google.com/file/d/1ceUaYM0lUefMrIbdrPLCq_2Eto2JO5tn/view?usp=drive_link" %}

{% embed url="https://mantavyam.notion.site/18152f7cde8880d699a5f2e65f87374e" %}
Get Credited for sharing your Knowledge Source with your Peer
{% endembed %}

{% embed url="https://mantavyam.notion.site/17e52f7cde8880e0987fd06d33ef6019" %}
Submit Queries/Feedbacks/Suggestions/Complaints using this Form
{% endembed %}
