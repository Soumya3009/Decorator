def fun1(fun):
    def wrapper():
        print("Hello")
        fun()
        print("Welcome to python 7pearls")

    return wrapper

#def fun2():
   # print("Learning python")

#fun2=fun1(fun2)
#fun2()

@fun1
def fun2():
    print("Learning python")

fun2()

