
info_format = "Executing function '{0}' with params: {1} {2}"


def func_invocation_info(func, *args, **kwargs):
    argsStr = ", ".join(args)
    kwargsStr = ", ".join(["{0}={1}".format(k, v) for k, v in kwargs.items()])
    return info_format.format(func.__name__, argsStr, kwargsStr)
