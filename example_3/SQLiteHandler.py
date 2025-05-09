# Logging handler for SQLite
# Based on
#   https://stackoverflow.com/questions/2314307/python-logging-to-database
#   https://docs.python.org/3/library/logging.html#handlers
#   https://gist.github.com/ykessler/2662203#file_sqlite_handler.py
#
# python SQLiteHandler.py


import sqlite3
import logging
import pandas as pd


DEFAULT_SEPARATOR = '|'
DEFAULT_DATA_TYPE = 'TEXT'


# WARNING: attributes must be choosen from https://docs.python.org/3/library/logging.html#formatter-objects
DEFAULT_ATTRIBUTES_LIST = ['asctime', 'levelname', 'name', 'message']


class SQLiteHandler(logging.Handler):
    '''
    Logging handler for SQLite

    Based on Yarin Kessler's sqlite_handler.py https://gist.github.com/ykessler/2662203#file_sqlite_handler.py
    '''

    def __init__(self, database, table, attributes_list):
        '''
        SQLiteHandler class constructor

        Parameters:
            self: instance of the class
            database: database
            table: log table name
            attributes_list: log table columns

        Returns:
            None
        '''
        # super(SQLiteHandler, self).__init__() # for python 2.X
        super().__init__()  # for python 3.X
        self.database = database
        self.table = table
        self.attributes = attributes_list

        # Create table if needed
        create_table_sql = 'CREATE TABLE IF NOT EXISTS ' + self.table + \
            ' (' + ((' ' + DEFAULT_DATA_TYPE + ', ').join(self.attributes)
                    ) + ' ' + DEFAULT_DATA_TYPE + ');'
        # print(create_table_sql)
        conn = sqlite3.connect(self.database)
        conn.execute(create_table_sql)
        conn.commit()
        conn.close()

    def emit(self, record):
        '''
        Save the log record

        Parameters:
            self: instance of the class
            record: log record to be saved

        Returns:
            None
        '''
        # Use default formatting if no formatter is set
        self.format(record)

        # print(record.__dict__)
        record_values = [record.__dict__[k] for k in self.attributes]
        str_record_values = ', '.join("'{0}'".format(v.replace("'", '').replace(
            '"', '').replace('\n', ' ')) for v in record_values)
        # print(str_record_values)

        insert_sql = 'INSERT INTO ' + self.table + \
            ' (' + (', '.join(self.attributes)) + \
            ') VALUES (' + str_record_values + ');'
        # print(insert_sql)
        conn = sqlite3.connect(self.database)
        conn.execute(insert_sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    my_database = 'sqlite.db'
    my_table = 'log'
    print('Test SQLiteHandler\n\tdatabase: {}\n\ttable: {}'.format(
        my_database, my_table))
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    sql_handler = SQLiteHandler(
        database=my_database, table=my_table, attributes_list=DEFAULT_ATTRIBUTES_LIST)
    sql_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(' + ((')s' + DEFAULT_SEPARATOR + '%(').join(DEFAULT_ATTRIBUTES_LIST)) + ')s')
    sql_handler.setFormatter(formatter)

    logger.addHandler(sql_handler)

    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.error('This is an error message')

    conn = sqlite3.connect(my_database)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + my_table + ';')
    records = pd.DataFrame(cursor.fetchall(), columns=DEFAULT_ATTRIBUTES_LIST)
    conn.close()
    print('Records:')
    print(records)
else:
    pass
