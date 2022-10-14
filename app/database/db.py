import sqlite3


__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect(
            'app/database/database.db',
            check_same_thread = False
        )

    return __connection


conn = get_connection()
c = conn.cursor()


# --- Creating Tables --- #
conn = get_connection()
c = conn.cursor()


# --- users table
c.execute('''CREATE TABLE IF NOT EXISTS captcha(
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        captcha_user_id     INTEGER NOT NULL
    )
''')
conn.commit()


# --- captcha status table
c.execute('''CREATE TABLE IF NOT EXISTS captcha_status(
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        status     VARCHAR(255)
    )
''')
conn.commit()


# --- lang table
c.execute('''CREATE TABLE IF NOT EXISTS captcha_lang(
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        lang     VARCHAR NOT NULL
    )
''')
conn.commit()



# --- Methods --- #
def insert_user_into_table(user_id):
    c.execute("INSERT INTO captcha (captcha_user_id) VALUES (?)", (user_id,))
    conn.commit()


def delete_user_into_table(user_id):
    c.execute("DELETE FROM captcha WHERE captcha_user_id = ?", (user_id,))
    conn.commit()


def select_user(user_id):
    c.execute("SELECT captcha_user_id FROM captcha WHERE captcha_user_id = ?", (user_id,))
    return c.fetchone()


def status_off():
    c.execute("UPDATE captcha_status SET status = ?", ('off',))
    conn.commit()


def status_on():
    c.execute("UPDATE captcha_status SET status = ?", ('on',))
    conn.commit()


def insert_default_lang():
    c.execute("INSERT INTO captcha_lang (lang) VALUES (?)", ('ru',))
    conn.commit()


def insert_default_status():
    c.execute("INSERT INTO captcha_status (status) VALUES (?)", ('on',))
    conn.commit()


def lang_ua():
    c.execute("UPDATE captcha_lang SET lang = ?", ('ua',))
    conn.commit()


def lang_ru():
    c.execute("UPDATE captcha_lang SET lang = ?", ('ru',))
    conn.commit()


def lang_en():
    c.execute("UPDATE captcha_lang SET lang = ?", ('en',))
    conn.commit()


def select_status():
    c.execute("SELECT status FROM captcha_status")
    return c.fetchone()


def select_lang():
    c.execute("SELECT lang FROM captcha_lang")
    return c.fetchone()