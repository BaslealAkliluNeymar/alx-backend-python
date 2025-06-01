import sqlite3 
import functools

def with_db_connection(func):
    """ your code goes here""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, kwargs['age'])
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            result = None
        finally:
            conn.close()
        return result
    return wrapper


@with_db_connection 
def get_user_by_id(conn, age): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE age = 28")

    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(age=28)
print(user)

