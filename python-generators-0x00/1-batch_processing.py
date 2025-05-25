import seed 
import sys
def stream_users_in_batches(batch_size):
    """
    Generator function that yields users in batches from the database.

    Args:
        batch_size (int): The number of users to yield in each batch.

    Yields:
        list: A list of user dictionaries, each representing a user.
    """
    # Placeholder for database connection and query execution
    # This should be replaced with actual database connection logic
    
    db  = seed.Seed('localhost', 'root', '1209', 'ALX_prodev')
    connection = db.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            return []
        for row in rows:
            yield row

        cursor.close()
        connection.close()



def  batch_processing(batch_size):
    """
    Generator function that yields users in batches from the database.

    Args:
        batch_size (int): The number of users to yield in each batch.

    Yields:
        list: A list of user dictionaries, each representing a user.
    """
    # Placeholder for database connection and query execution
    # This should be replaced with actual database connection logic
    
    db  = seed.Seed('localhost', 'root', '1209', 'ALX_prodev')
    connection = db.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data WHERE age > 25 ")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            return []
        for row in rows:
            yield row

    
try:
    for i in batch_processing(5):
        print(i)
except BrokenPipeError:
    sys.stderr.close()








# print(stream_users_in_batches(5))
# print(batch_processing(50))