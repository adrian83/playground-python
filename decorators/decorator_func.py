

def log(func):
    def wrapper(*args, **kwargs):
        print("Exectuing {0} with params {1} {2}"
              .format(func.__name__, *args, **kwargs))
        return func(*args, **kwargs)
    return wrapper


@log
def save(first_name, last_name, test="uuu"):
    print("{0} {1}".format(first_name, last_name))


save("John", "Doe")
