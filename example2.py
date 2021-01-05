def fun1(fun):
    def wrapper(*args, **kargs):
        print("hello")
        fun(*args, **kargs)
        print("Learning python")

    return wrapper

@fun1
def fun2(name):
    print(f"{name}")

fun2("Soumya")

