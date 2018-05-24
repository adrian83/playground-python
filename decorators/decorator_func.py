
from base import func_invocation_info


def log(func):
    def wrapper(*args, **kwargs):
        print(func_invocation_info(func, *args, **kwargs))
        return func(*args, **kwargs)
    return wrapper


@log
def do_something(first_name, last_name):
    print("{0} {1}".format(first_name, last_name))


do_something("John", "Doe")


def log2(level, file_name):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            info = func_invocation_info(func, *args, **kwargs)
            print("[{0}] [{1}] {2}".format(level, file_name, info))
            return func(*args, **kwargs)
        return wrapper2
    return wrapper1


@log2("INFO", "decorators_func.py")
def do_something_usefull(first_name, last_name):
    print("{0} {1}".format(first_name, last_name))


do_something_usefull("Wiliam", "Shakespear")


@log2("INFO", "decorators_func.py")
@log
def do_something_else(first_name, last_name):
    print("{0} {1}".format(first_name, last_name))


do_something_else("Wiliam", "Shakespear")
