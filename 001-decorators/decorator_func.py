from base import func_invocation_info, introduce


def log(func):
    def wrapper(*args, **kwargs):
        print(func_invocation_info(func, *args, **kwargs))
        return func(*args, **kwargs)
    return wrapper


@log
def introduce_ex1(first_name, last_name, **info):
    introduce(first_name, last_name, **info)


introduce_ex1("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")


def log2(level, file_name):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            info = func_invocation_info(func, *args, **kwargs)
            print("[{0}] [{1}] {2}".format(level, file_name, info))
            return func(*args, **kwargs)
        return wrapper2
    return wrapper1


@log2("INFO", "decorator_func.py")
def introduce_ex2(first_name, last_name, **info):
    introduce(first_name, last_name, **info)


introduce_ex2("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")


@log2("INFO", "decorator_func.py")
@log
def introduce_ex3(first_name, last_name, **info):
    introduce(first_name, last_name, **info)


introduce_ex3("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")
