import sqlite3

db_name="FaceBase.db"
try:
    sqliteConnection = sqlite3.connect(db_name)
    sqlite_create_table_query = '''CREATE TABLE People (
                                id INTEGER PRIMARY KEY NOT NULL,
                                Name STRING NOT NULL,
                                MaSV BIGINT UNIQUE,
                                Birthday DATE,
                                Gender TEXT,
                                Address TEXT
                                );'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")