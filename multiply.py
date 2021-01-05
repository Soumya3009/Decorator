class Power(object):
    def __init__(self, args):
        self._args=args

    def __call__(self, a, b):
        val=self._args(a,b)
        return val**2

@Power
def mul(a,b):
    return a*b

print(mul)
print(mul(2,2))

