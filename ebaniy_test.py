import pytest
import sqlite3
import CDatabase

@pytest.fixture
def db_connection():
    connection = sqlite3.connect('server')
    cursor = sqlite3.connect('server').cursor()

    cursor.execute('''
        CREATE TABLE data (
            id INTEGER PRIMARY KEY,
            btc INTEGER,
            ltc INTEGER,
            eth INTEGER,
            sol INTEGER,
            trx INTEGER,
            xrp INTEGER,
            dot INTEGER,
            atom INTEGER,
            waves INTEGER
        )
    ''')
    connection.commit()
    yield connection
    connection.close()


def test_is_new_user(chat_id):
    cursor = sqlite3.connect('server').cursor()

    assert CDatabase.is_new_user(chat_id) is True
    CDatabase.reg_new_user(chat_id)
    assert CDatabase.is_new_user(chat_id) is False
def test_no_user_in_db(chat_id):
    cursor = sqlite3.connect('server').cursor()

    return CDatabase.is_new_user(chat_id) is False
    CDatabase.reg_new_user(chat_id)
    return CDatabase.is_new_user(chat_id) is True


def test_reg_new_user(chat_id):
    cursor = sqlite3.connect('server').cursor()

    CDatabase.reg_new_user(chat_id)

    cursor.execute("SELECT * FROM data WHERE id=?", (chat_id,))
    user_data = cursor.fetchone()
    assert user_data is not None
    assert user_data[0] == chat_id


def test_get_all_user_data(user_id):
    conn = sqlite3.connect('server')
    cursor = conn.cursor()

    data = cursor.execute(f"SELECT * FROM data WHERE id={user_id}")
    records = cursor.fetchall()
    conn.close()

    return records