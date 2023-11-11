from datetime import datetime

from utility.custom_logger import root_logger


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        root_logger.info(f"Время выполнения функции {func.__name__}: {execution_time}")
        return result
    return wrapper
