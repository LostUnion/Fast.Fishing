import sqlite3 as sq

db = sq.connect('handlers/database/authentication.db')
cur = db.cursor()

def delete_login_and_password(service):
    cur.execute(f"DELETE FROM auth WHERE service = \"{service}\"")
    db.commit()

def get_login(service: str):
    cur.execute(f"SELECT login FROM auth WHERE service = \"{service}\"")
    result = cur.fetchone()
    return result[0] if result else None
    
def get_password(service: str):
    cur.execute(f"SELECT password FROM auth WHERE service = \"{service}\"")
    result = cur.fetchone()
    return result[0] if result else None

def login_and_password_input(service: str):
    while True:
        log = get_login(service)
        pas = get_password(service)
        if log is None and pas is None:
            login = input('Enter your username from the account: ')
            password = input('Enter your password from the account: ')
            if not login or not password:
                print("Both login and password are required. Please try again.")
            else:
                return login, password
        else:
            return log, pas

def db_auth(service: str):
    login, password = login_and_password_input(service)
    cur.execute(f'SELECT login FROM auth WHERE login = ? AND password = ? AND service = \"{service}\"', (login, password))
    existing_entry = cur.fetchone()
    if existing_entry is None:
        cur.execute(f"INSERT INTO auth VALUES (?, ?, ?)", (login, password, service))
        db.commit()
        print("Inserted new login and password into the database.")
    else:
        print("Login and password already exist in the database.")

def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS auth("
                "login TEXT, "
                "password TEXT, "
                "service TEXT )")
    db.commit()