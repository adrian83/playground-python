
class Log:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Exectuing {0} with params {1} {2}"
              .format(self.func.__name__, args, kwargs))
        return self.func(*args, **kwargs)


@Log
def save(first_name, last_name):
    print("{0} {1}".format(first_name, last_name))


save("John", "Doe")
