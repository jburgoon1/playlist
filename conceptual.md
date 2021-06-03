### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostrgeSQL is an database system
- What is the difference between SQL and PostgreSQL?
PostgreSQL is an updated system with more functionality than SQL
- In `psql`, how do you connect to a database?
\c db_name
- What is the difference between `HAVING` and `WHERE`?
having is looking for something contained in a list, where is looking for the exact match to the parameter
- What is the difference between an `INNER` and `OUTER` join?
inner join combines everything that overlaps between two tables, outer joins are showing evrything from both tables no matter if they overlap
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
left outer shows everything frim the table that is in the left of the command, right outer shows everything from the table that is to the right of the command
- What is an ORM? What do they do?
Object relational mapping, it allows you to edit and grab data from a database using objects
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
ajax requires you to handle json for the data while requests allows you to grab data without handling json
- What is CSRF? What is the purpose of the CSRF token?
Cross site reference, csrf is a token that the app tests to make sure it is from the form you are submitting so no one can send requests from another site
- What is the purpose of `form.hidden_tag()`?
this allows you to loop over a form without showing you csrf token on the screen. 
