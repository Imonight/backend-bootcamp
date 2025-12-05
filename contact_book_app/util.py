from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] is running...{func.__name__}()")
        result = func(*args, **kwargs)
        print(f"[log] is exiting...{func.__name__}()")
        return result
    return wrapper


def validate_input(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.name.strip() or not self.phone.strip():
            print("name and phone can't be empty")
            return
        return func(self, *args, **kwargs)
    return wrapper
        
