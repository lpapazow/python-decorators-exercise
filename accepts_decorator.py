def accepts(*args):
    def inner(funct):
        def check_errors(*fargs):
            for arg_idx in range(len(args)):
                if args[arg_idx] != type(fargs[arg_idx]):
                    raise TypeError("Argument {0} of {1} is not {2}".format(arg_idx + 1, funct.__name__, args[arg_idx].__name__) + "")
            return funct(*fargs)
        return check_errors
    return inner


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello(4)

