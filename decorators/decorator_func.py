from base import func_invocation_info, introduce


def log(func):
    def wrapper(*args, **kwargs):
        print(func_invocation_info(func, *args, **kwargs))
        return func(*args, **kwargs)
    return wrapper


@log
def introduce_1(first_name, last_name, **info):
    print("PERSONAL DATA")
    introduce(first_name, last_name, **info)
    print("")


introduce_1("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")


def log2(level, file_name):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            info = func_invocation_info(func, *args, **kwargs)
            print("[{0}] [{1}] {2}".format(level, file_name, info))
            return func(*args, **kwargs)
        return wrapper2
    return wrapper1


@log2("INFO", "decorators_func.py")
def introduce_2(first_name, last_name, **info):
    print("PERSONAL DATA")
    introduce(first_name, last_name, **info)
    print("")


introduce_2("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")


@log2("INFO", "decorators_func.py")
@log
def introduce_3(first_name, last_name, **info):
    print("PERSONAL DATA")
    introduce(first_name, last_name, **info)
    print("")


introduce_3("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")
