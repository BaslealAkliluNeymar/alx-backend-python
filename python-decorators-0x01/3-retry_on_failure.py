import time
from functools import wraps

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print(f" Attempt: {attempt} failed: {e}")
                    if attempt < retries:
                        time.sleep(delay)
                    else:
                        print("failed to load all entries")
                        raise
        return wrapper
    return decorator


@retry_on_failure(retries=3, delay=1)
def unstable_db_operation():
    raise Exception("Transient DB error")
