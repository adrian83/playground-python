import types


info_format = "Executing '{0}' with params: {1} {2}"


def func_invocation_info(call, *args, **kwargs):
    nameable = call if isinstance(call, types.FunctionType) else call.__class__
    argsStr = ", ".join(args)
    kwargsStr = ", ".join(["{0}={1}".format(k, v) for k, v in kwargs.items()])
    return info_format.format(nameable.__name__, argsStr, kwargsStr)


def introduce(first_name, last_name, **info):
    print("First name: {0}".format(first_name))
    print("Last name: {0}".format(last_name))
    for key, value in info.items():
        print("{0}: {1}".format(key, value))
