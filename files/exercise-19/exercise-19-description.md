# Exercise 19 : /etc/passwd to dict

## For this excercise
Write a function __passwd_to_dict__ that reads from a Unix-style
"password file", commonly stored as /etc/passwd, and returns a _dict_ based on it.

Each line is one user record, divided into colon-separated fields.

The function should return a dict based on _/etc/passwd_ in which the dict's keys 
are usernames and the values are the user' IDs.
