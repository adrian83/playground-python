from base import func_invocation_info, introduce


class Log:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(func_invocation_info(self.func, *args, **kwargs))
        return self.func(*args, **kwargs)


@Log
def introduce_1(first_name, last_name, **info):
    print("PERSONAL DATA")
    introduce(first_name, last_name, **info)
    print("")


introduce_1("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")


class Log2:

    def __init__(self, level, file_name):
        self.level = level
        self.file_name = file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            info = func_invocation_info(func, *args, **kwargs)
            print("[{0}] [{1}] {2}".format(self.level, self.file_name, info))
            return func(*args, **kwargs)
        return wrapper


@Log2("INFO", "decorators_class.py")
def introduce_2(first_name, last_name, **info):
    print("PERSONAL DATA")
    introduce(first_name, last_name, **info)
    print("")


introduce_2("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")


@Log2("INFO", "decorators_class.py")
@Log
def introduce_3(first_name, last_name, **info):
    print("PERSONAL DATA")
    introduce(first_name, last_name, **info)
    print("")


introduce_3("William", "Shakespeare", Father="John Shakespeare",
            Mother="Mary Arden")
