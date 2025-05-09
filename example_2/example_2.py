# We want to track the execution of this code that generates random integers. Let's suppose that the values generated must respet some thresholds wich indicates if a value
# is a warning, an error or a critical error. Let's track the values using logging. As shown in the logging doc we can use 5 levels:
# +----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
# | Level    | When it’s used                                                                                                                                |
# +----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
# | DEBUG    | Detailed information, typically of interest only when diagnosing problems                                                                     |
# | INFO     | Confirmation that things are working as expected                                                                                              |
# | WARNING  | An indication that something unexpected happened, or indicative of some problem in the near future. The software is still working as expected |
# | ERROR    | Due to a more serious problem, the software has not been able to perform some function                                                        |
# | CRITICAL |A serious error, indicating that the program itself may be unable to continue running                                                          |
# +----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
#
# python example_2.py


import os
import random
import logging


current_filename = os.path.basename(__file__).rsplit('.', 1)[0]

# changing level we can change frome what level we want to log the events

logging.basicConfig(filename=current_filename + '.log',
                    level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


if __name__ == '__main__':
    logging.info('Generate some random integers')

    num_numbers = 10
    min_value = 0
    max_value = 20
    warning_threshold = 5
    error_threshold = 10
    critical_threshold = 15

    logging.debug('Numbers: {}\nMin value: {}\nMax value: {}\nWaring threshold: {}\nError threshold: {}\nCritical threshold: {}'.format(
        num_numbers, min_value, max_value, warning_threshold, error_threshold, critical_threshold))

    logging.debug('Start')
    for i in range(num_numbers):
        logging.debug('Iteration: {}'.format(i))
        value = random.randint(min_value, max_value)

        try:
            logging.debug('\tTry value')
            if value > critical_threshold:
                raise Exception('\tValue: {} -> Critical!'.format(value))
            elif value > error_threshold:
                logging.error('\tValue: {} -> Error!'.format(value))
            elif value > warning_threshold:
                logging.warning('\tValue: {} -> Warning!'.format(value))
            else:
                logging.info('\tValue: {}'.format(value))
        except Exception as e:
            logging.critical(e)
            exit()
        finally:
            logging.debug('The try except is finished')

    logging.debug('End')
else:
    pass
