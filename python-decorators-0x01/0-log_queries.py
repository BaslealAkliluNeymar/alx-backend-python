import sqlite3
from datetime import datetime

#### decorator to log SQL queries

""" YOUR CODE GOES HERE"""
def log_queries(func):
    def wrapper(*args, **kwargs):
        func(kwargs['query'])
        print(f"Executing query: {kwargs['query']}")

    return wrapper
         
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

print(users)