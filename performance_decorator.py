import datetime
from time import *

def performance(log_file):
    def inner(func):
        def create_func_log():
            start = time()
            result = func()
            end = time()
            exec_time = end - start
            f = open(log_file, 'a')
            f.write("{0} was called and took {1} seconds to complete\n".format(func.__name__ , exec_time))
            f.close()
            return result
        return create_func_log
    return inner

@performance('log2.txt')
def something_heavy():
    sleep(2)
    return "I am done!"

print(something_heavy())
