import time

from utility.custom_logger import root_logger


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        root_logger.info(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result

    return wrapper
