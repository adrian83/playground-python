import types
import time

info_format = "Executing '{0}' with params: {1} {2}"
time_format = "Execution of '{0}' took {1} millisecond(s)"


now_in_ms = lambda: int(round(time.time() * 1000))


def func_invocation_info(call, *args, **kwargs):
    nameable = call if isinstance(call, types.FunctionType) else call.__class__
    argsStr = ", ".join(args)
    kwargsStr = ", ".join(["{0}={1}".format(k, v) for k, v in kwargs.items()])
    start = now_in_ms()
    argsInfo = info_format.format(nameable.__name__, argsStr, kwargsStr)
    end = now_in_ms()
    timeInfo = time_format.format(nameable.__name__, end-start)
    return "{0}\n{1}".format(argsInfo, timeInfo)


def introduce(first_name, last_name, **info):
    print("First name: {0}".format(first_name))
    print("Last name: {0}".format(last_name))
    for key, value in info.items():
        print("{0}: {1}".format(key, value))
