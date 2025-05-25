import mysql.connector
import seed
from itertools import islice
def stream_users():
    """
    Generator function that yields each user from the provided list of users.

    Args:
        users (list): A list of user dictionaries.

    Yields:
        dict: The next user in the list.
    """
    
    db = seed.Seed("localhost", "root", "1209", "ALX_prodev")
    conn = db.connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")

    for user in cursor:
        yield {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "age": user[3],
            "created_at": user[4]
        }
    

    cursor.close()
    db.connect_to_prodev().close()


for user in islice(stream_users(), 6):
    print(user)