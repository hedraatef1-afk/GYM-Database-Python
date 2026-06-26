 GYM Member Database Management System

A Python-based database scripting project that demonstrates how to integrate Python with SQLite3 to manage and manipulate relational database tables dynamically.

 🛠️ Tech Stack & Tools
Language: Python 3
Database: SQLite3
Editor: VS Code

⚡ Key Features Implemented
Database Initialization: Automatically handles database cleanup using `DROP TABLE IF EXISTS` to ensure a clean state before schema execution.
Data Definition (DDL): Creates robust tables utilizing advanced constraints such as `PRIMARY KEY AUTOINCREMENT` and `NOT NULL` for strict data integrity.
Data Manipulation (DML): Inserts, modifies, and cleans data efficiently using standard SQL operations:
Data Insertion:Simulates live data entry into predefined structures.
 Data Updating:Modifies existing records dynamically based on specific conditions using `UPDATE`.
Data Cleansing: Implements conditional row deletion via `DELETE FROM` with exact `WHERE` clauses to filter out records.
Data Querying & Fetching: Retrieves data dynamically using custom query execution (`SELECT *`) and processes rows directly to the terminal.
 📊 Sample Output
The script successfully outputs structured tuple results directly within the VS Code integrated terminal, ensuring precise execution of the business logic.
