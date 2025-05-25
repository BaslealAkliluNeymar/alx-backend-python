import seed

def stream_user_ages():
    """
    Generator function that yields the ages of users from the database.

    Yields:
        int: The age of each user.
    """
    db = seed.Seed('localhost', 'root', '1209', 'ALX_prodev')
    connection = db.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")


    rows = cursor.fetchall()
    for row in rows:
        yield row[0]
    cursor.close()
    connection.close()

  
def average_age():
    """
    Function to calculate the average age of users from the database.

    Returns:
        float: The average age of users.
    """
    total_age = 0 
    count = 0
    for age in stream_user_ages():
        total_age += int(age)
        count += 1
        print(f"Average age of users:{total_age / count if count > 0 else 0}")
    
   
print(average_age())

