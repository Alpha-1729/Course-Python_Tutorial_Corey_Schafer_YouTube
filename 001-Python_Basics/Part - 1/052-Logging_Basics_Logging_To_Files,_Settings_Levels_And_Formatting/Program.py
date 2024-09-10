#!/usr/bin/python3
# Logging Basics Logging To Files, Settings Levels And Formatting

"""
>>>> Logging Levels
        Logging levels allow us to specify exactly what we want to log by separating into categories.
        There are 5 standard logging levels.

        DEBUG
            Detailed information, typically of interest only when diagnosing problems.
        INFO
            Confirmation that things are working as expected.
        WARNING
            An indication that something unexpected happened, or indicative of some problem in the near future. (Eg. Disk space low). The software is still working as expected.
        ERROR
            Due to a more serious problem, the software has not been able to perform some function.
        CRITICAL
            A serious error, indicating that the program itself may be unable to continue running.
>>>> The default level for logging is set to WARNING.
        It will capture everything that is WARNING, ERROR, CRITICAL.
        It will ignore DEBUG and INFO.
>>>> Logging format
        Refer LogRecord attribute heading.
        Reference Link: https://docs.python.org/3/library/logging.html
>>>>
"""
import logging

# logging.basicConfig(level=logging.DEBUG)

# Logging into a file with formatting.
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    "Divide Function"
    return x / y


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
print("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
print("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
print("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
print("Div: {} / {} = {}".format(num_1, num_2, div_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
