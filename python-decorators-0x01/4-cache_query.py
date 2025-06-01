from functools import wraps
import sqlite3
def cache_query(func):
    cache = {}

    @wraps(func)
    def wrapper(query, *args, **kwargs):
        if query in cache:
            print("[CACHE]:cahce result reuturned")
            return cache[query]
        result = func(query, *args, **kwargs)
        cache[query] = result
        return result
    return wrapper

# Example usage
@cache_query
def fetch_data(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()
