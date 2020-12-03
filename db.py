import sqlite3

def get_conn():
    try:
        # conn = mariadb.conn()
        conn = sqlite3.connect('tutoring.db')
        return conn
    except Exception as e:
        print("----------------")
        print("Error Creating Connection", e)
        print("----------------")
        return (False, e)

def close_con(conn):
    try:
        conn.close()
        return True
    except Exception as e:
        print("----------------")
        print("Error Closing Connection", e)
        print("----------------")
        return (False, e)

def insert_one(query, arguments=()):
    # Insert one row into table
    # Returns the id of the row it just inserted"
    conn = get_conn()
    last_row_id = None
    try:
        cursor = conn.cursor()
        cursor.execute(query, arguments)
        last_row_id = cursor.lastrowid
        conn.commit()
        close_con(conn)
        return True, last_row_id
    except Exception as e:
        print("----------------")
        print("Error Inserting", e)
        print(query)
        print(arguments)
        print("----------------")
        return (False, e)

def get_one(query, arguments=()):
    # Return 1 row as a tuple (e.g. (1, "jayp@mail.com", "jayp", "1234"))
    conn = get_conn()
    try:
        cursor = conn.cursor()
        if arguments:
            cursor.execute(query, arguments)
        else:
            cursor.execute(query)
        result = cursor.fetchone()
        close_con(conn)
        return (True, result)
    except Exception as e:
        print("----------------")
        print("Error Getting One", e)
        print(query)
        print(arguments)
        print("----------------")
        return (False, e)

def get_all(query, arguments=()):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(query, arguments)
        result = cursor.fetchall()
        close_con(conn)
        return (True, result)
    except Exception as e:
        print("----------------")
        print("Error Getting All", e)
        print(query)
        print(arguments)
        print("----------------")
        return (False, e)

def update_one(query, arguments=()):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(query, arguments)
        conn.commit()
        close_con(conn)
        return True, None
    except Exception as e:
        print("----------------")
        print("Error Updating One", e)
        print(query)
        print(arguments)
        print("----------------")
        return (False, e)

def delete_one(query, arguments=()):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(query, arguments)
        conn.commit()
        close_con(conn)
        return True, None
    except Exception as e:
        print("----------------")
        print("Error Deleting", e)
        print(query)
        print(arguments)
        print("----------------")
        return (False, e)

def get_user_by_email(email):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, bio, password_hash FROM users WHERE email=?", (email,))
        result = cursor.fetchone()
        close_con(conn)
        return (True, result)
    except Exception as e:
        print("----------------")
        print("Error Getting User by email", e)
        print(email)
        print("----------------")
        return (False, e)