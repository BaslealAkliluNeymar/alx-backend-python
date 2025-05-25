from seed import Seed

def paginate_users(page_size, offset):
    seed  = Seed('localhost', 'root', '1209', 'ALX_prodev')
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator function that yields users in pages from the database.

    Args:
        page_size (int): The number of users to yield in each page.

    Yields:
        list: A list of user dictionaries, each representing a user.
    """
    
    offset = 0 

    while True:
        users = paginate_users(page_size,offset)
        if not users:
            break
        for user in users:
            yield user
        offset += page_size


for user in lazy_paginate(5):
    print(user)