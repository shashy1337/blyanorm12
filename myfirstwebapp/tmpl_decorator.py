from functools import wraps

#Создание декортаора
def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1.Code to execute before calling the decorated function
        # 2. Вывод декорируемой функции и возврат полученных от нее результатов.
        return func(*args, **kwargs)
    return wrapper