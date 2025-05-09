# Logging examples

## Introduction

Logging means to track what events happens when you run some software. In Python the easiest way to do that is to use print() statements when your code needs to perform actions that you want to track. If you need some more advanced logging (i.e. save the logs in a file or in a database table) the easiest way is to use [logging](https://docs.python.org/3/library/logging.html)

Another point to consider is: when do you have to use logging vs raise an exception? In a nutshell as always it depends on what you have to do. How the software is expected to behave? Is the error so critical that further steps cannot/should not be done? In this case the exception is the expected behaviour. Is it ok to go on with the execution of the code even if we got some errors? Ok in this case let's keep track that we got some errors but let's continue if the execution of the code. Really interesting discussion on reddit about this [topic](https://www.reddit.com/r/learnpython/comments/9l0aqb/when_should_i_use_loggererror_vs_raise_exception/)

Setup for this examples: let's generates random integers and let's suppose that the values generated must respect some thresholds which indicates if a value is a warning, an error or a critical error. We will use the logging levels:

| Level    | When it’s used                                                                                                                                |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| DEBUG    | Detailed information, typically of interest only when diagnosing problems                                                                     |
| INFO     | Confirmation that things are working as expected                                                                                              |
| WARNING  | An indication that something unexpected happened, or indicative of some problem in the near future. The software is still working as expected |
| ERROR    | Due to a more serious problem, the software has not been able to perform some function                                                        |
| CRITICAL | A serious error, indicating that the program itself may be unable to continue running                                                         |


## Software and libraries

This project uses Python 3.11.9 and the most important packages are:

* [logging](https://docs.python.org/3/library/logging.html)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)

To setup a new local enviroment and install all dependencies you can run `.\my_scripts\Set-Up.ps1`

Alternatively to create the virtual enviroment you can run `python -m venv .venv`.

## Testing

You can run `.\my_scripts\Test.ps1`.

Alternatively from the project folder run `pytest`

To run a single test: `pytest .\tests\test_dummy.py::test_dummy`

## Code styling

[PEP8](https://peps.python.org/pep-0008/) is the style guide for Python code, and it's good practice to follow it to ensure your code is readable and consistent.

To check and format my code according to PEP8 I am using:
- [pycodestyle](https://pypi.org/project/pycodestyle/): tool to check the code against PEP 8 conventions.
- [autopep8](https://pypi.org/project/autopep8/): tool to automatically format Python code according to PEP 8 standards.

You can run `.\my_scripts\FormatAndLint.ps1`.

Alternatively to run pycodestyle on all files in the project folder and create a report: `pycodestyle --statistics --count . > code_style\report.txt`

To run autopep8 on all files in the project folder: `autopep8 --recursive --in-place .`

I prefere to check and update one file at the time because the previous recursive commands affect also `.\venv\` files. For example:

`pycodestyle .\example_1\example_1.py > .\code_style\example_1_report.txt`

`autopep8 --in-place .\example_1\example_1.py`

## Running the code

There are 3 examples:
* example_1: let's use print() to log what is happening in the code.
* example_2: using example_1 as base let's use logging module and create a log file.
* example_3: using the example_2 as base let's track different errors level in different ways. In this example I have also created SQLiteHandler.py to log error messages on a SQL table.

From each example folder you can run `python example_1.py`, `python example_2.py` or `python example_3.py`

The module SQLiteHandler.py can be also run with `python SQLiteHandler.py` to test if everything is working as expected.

## List of activities

In the [TODO](TODO.md) file you can find the list of tasks and on going activities.

## Licensing and acknowledgements

Have a look at [LICENSE](LICENSE.md) and many thanks to Yarin Kessler for [file_sqlite_handler.py](https://gist.github.com/ykessler/2662203#file_sqlite_handler.py). Also thanks to Corey Schafer for this fantastic video [Python Tutorial: Logging Advanced - Loggers, Handlers, and Formatters](https://www.youtube.com/watch?v=jxmzY9soFXg&t=42s).

## Outro

I hope this repository was interesting and thank you for taking the time to check it out. On my Medium you can find a more in depth [story](https://medium.com/@simone-rigoni01/logging-with-logging-in-python-d3d8eb9a155a) and on my Blogspot you can find the same [post](https://simonerigoni01.blogspot.com/2024/05/ricerca-di-donatori-per-il-progetto.html) in italian. Let me know if you have any question and if you like the content that I create feel free to [buy me a coffee](https://www.buymeacoffee.com/simonerigoni).
