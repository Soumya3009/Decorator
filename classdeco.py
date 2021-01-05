class MyClass:
    def __init__(self, func):
        self.func=func

    def __call__(self):
        print("I am from call")
        self.func()

@MyClass
def func():
    print("Soumya")

func()

