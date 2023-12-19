This is my file on the project. Thank you

Python - Object-relational mapping using MySQLdb and SQLAlchemy
Within this project, I delved into the world of object-relational mapping (ORM) and its significance in database scripting. The focus was on utilizing two powerful tools: MySQLdb and SQLAlchemy. Through these, I honed my skills in querying, creating, modifying, and deleting tables within MySQL databases.

Tests :heavy_check_mark:
tests: This folder houses a collection of SQL and Python scripts crucial for setting up test tables associated with all project files. These scripts have been provided by ALX.
Tasks :page_with_curl:
Throughout this project, I engaged in a series of tasks that offered practical hands-on experience in ORM with MySQL databases:

0. Get all states

0-select_states.py: A Python script employing MySQLdb to list all states within the hbtn_0e_0_usa database.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>.
Results are ordered in ascending order based on states.id.
1. Filter states

1-filter_states.py: A Python script leveraging MySQLdb to list states with names starting with N in the hbtn_0e_0_usa database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>.
Results are ordered in ascending order based on states.id.
2. Filter states by user input

2-my_filter_states.py: A Python script utilizing MySQLdb to display all values matching a specified name in the states table of the hbtn_0e_0_usa database.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>.
Results are ordered in ascending order based on states.id, employing string formatting for constructing the SQL query.
3. SQL Injection...

3-my_safe_filter_states.py: A Python script employing MySQLdb to display all values matching a given name in the states table of the hbtn_0e_0_usa database. This script ensures protection against SQL injections.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>.
Results are ordered in ascending order based on states.id.
4. Cities by states

4-cities_by_state.py: A Python script utilizing MySQLdb to list all cities from the hbtn_0e_4_usa database.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>.
Results are ordered in ascending order based on cities.id.
<!-- Continuing with the remaining tasks... -->
This project was a comprehensive exploration of ORM techniques using Python alongside MySQL databases, delving into querying, manipulation, and relational aspects through various tasks and scripts.
