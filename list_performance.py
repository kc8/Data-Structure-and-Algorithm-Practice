import timeit

def create_list_with_for(): 
    l = []
    for i in range(1000):
        l += [i]

def append_for_loop():
    l = []
    for i in range(1000):
        l.append(i)

def create_list_with_for_2():
    l = [i for i in range(1000)]

def list_constructor():
    l = list(range(1000))

t1 = timeit.Timer("create_list_with_for()", "from __main__ import create_list_with_for")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("append_for_loop()", "from __main__ import append_for_loop")
print("concat ", t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("create_list_with_for_2()", "from __main__ import create_list_with_for_2")
print("concat ", t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer("list_constructor()", "from __main__ import list_constructor")
print("concat ", t4.timeit(number=1000), "milliseconds")