from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] is runnung {func.__name__()}")
        result = func(*args, **kwargs)
        print(f"[log] is finsished {func.__name__}()")
        return result
    return wrapper


def validate_input(func):
    @wraps(func)
    def wrapper(tasks, *args, **kwargs):
        if not tasks.strip():
            print("tasks cannot be empty")
            return func(tasks, *args, **kwargs)
        
    return wrapper



