# Read log table
#
# python read_log_table.py

import sqlite3
import pandas as pd


MY_DATABASE = 'example_3.db'
MY_TABLE = 'log'
ATTRIBUTES_LIST = ['asctime', 'levelname', 'message'] 

if __name__ == '__main__':
    conn = sqlite3.connect(MY_DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + MY_TABLE + ';')
    records = pd.DataFrame(cursor.fetchall(), columns = ATTRIBUTES_LIST)
    conn.close()
    print('Records:')
    print(records)
else:
    pass