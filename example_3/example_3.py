# We want to track the execution of this code that generates random integers. Let's suppose that the values generated must respet some thresholds wich indicates if a value
# is a warning, an error or a critical error. Let's track the values using logging and track the different levels of message with different handlers:
# +----------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------+
# | Level    | When it’s used                                                                                                                                | Handler       |
# +----------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------+
# | DEBUG    | Detailed information, typically of interest only when diagnosing problems                                                                     | console       |
# | INFO     | Confirmation that things are working as expected                                                                                              | table         |
# | WARNING  | An indication that something unexpected happened, or indicative of some problem in the near future. The software is still working as expected | table         |
# | ERROR    | Due to a more serious problem, the software has not been able to perform some function                                                        | error_file    |
# | CRITICAL |A serious error, indicating that the program itself may be unable to continue running                                                          | critical_file |
# +----------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------+
#
# python example_3.py


import os
import random
import logging
import SQLiteHandler


current_filename = os.path.basename(__file__).rsplit('.', 1)[0]
my_database = current_filename + '.db'
my_table = 'log'

# changing level we can change frome what level we want to log the events

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

attributes_list = ['asctime', 'levelname', 'message']
formatter = logging.Formatter(
    '%(' + ((')s' + SQLiteHandler.DEFAULT_SEPARATOR + '%(').join(attributes_list)) + ')s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

sql_handler = SQLiteHandler.SQLiteHandler(
    database=my_database, table=my_table, attributes_list=attributes_list)
sql_handler.setLevel(logging.INFO)
sql_handler.setFormatter(formatter)

error_file_handler = logging.FileHandler(current_filename + '_error.log')
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)

critical_file_handler = logging.FileHandler(current_filename + '_critical.log')
critical_file_handler.setLevel(logging.CRITICAL)
critical_file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(sql_handler)
logger.addHandler(error_file_handler)
logger.addHandler(critical_file_handler)


if __name__ == '__main__':
    logger.info('Generate some random integers')

    num_numbers = 10
    min_value = 0
    max_value = 20
    warning_threshold = 5
    error_threshold = 10
    critical_threshold = 15

    logger.debug('Numbers: {}\nMin value: {}\nMax value: {}\nWaring threshold: {}\nError threshold: {}\nCritical threshold: {}'.format(
        num_numbers, min_value, max_value, warning_threshold, error_threshold, critical_threshold))

    logger.debug('Start')
    for i in range(num_numbers):
        logger.debug('Iteration: {}'.format(i))
        value = random.randint(min_value, max_value)

        try:
            logger.debug('\tTry value')
            if value > critical_threshold:
                raise Exception('\tValue: {} -> Critical!'.format(value))
            elif value > error_threshold:
                logger.error('\tValue: {} -> Error!'.format(value))
            elif value > warning_threshold:
                logger.warning('\tValue: {} -> Warning!'.format(value))
            else:
                logger.info('\tValue: {}'.format(value))
        except Exception as e:
            logger.critical(e)
            exit()
        finally:
            logger.debug('The try except is finished')

    logger.debug('End')
else:
    pass
