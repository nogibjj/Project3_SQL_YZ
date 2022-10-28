import sqlite3
import csv
import pandas as pd
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(cur, create_table_sql):
    """ create a table from the create_table_sql statement
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        cur.execute(create_table_sql)
    except Error as e:
        print(e)
    

def add_data_to_db(cur, filename, db_name, num_cols, enc="utf-8"):
    """Add data to db from csv file
    :param cur: cursor object
    :param filename: csv file name
    :param db_name: db name
    :param num_cols: number of columns in csv file
    :param enc: encoding of csv file
    :return:
    """
    file = open(filename, "r", encoding=enc)
    contents = csv.reader(file)
    questionmarks = ", ".join(["?"] * num_cols)
    insert_text = " INSERT INTO " + db_name + " VALUES (" + questionmarks + ")"
    cur.executemany(insert_text, contents)


def main():
    db_connection = create_connection("airbnb_database.db")
    cursor = db_connection.cursor()
    create_table(
        cursor,
        """CREATE TABLE IF NOT EXISTS train_user (
            id text PRIMARY KEY,
            date_account_created date,
            timestamp_first_active text,
            date_first_booking date,
            gender text,
            age integer,
            signup_method text,
            signup_flow integer,
            language text,
            affiliate_channel text,
            affiliate_provider text,
            first_affiliate_tracked text,
            signup_app text,
            first_device_type text,
            first_browser text,
            country_destination text
        );""",
    )
    cursor.execute("DELETE FROM train_user")

    add_data_to_db(cursor, "train_users_2.csv", "train_user", 16)

    # Chcek if data is loaded
    df = pd.read_sql_query("SELECT * FROM train_user", db_connection)
    print(df.sample(5))

    db_connection.commit()
    db_connection.close()


if __name__ == '__main__':
    main()

