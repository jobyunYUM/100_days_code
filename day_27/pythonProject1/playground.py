def add(*args):
    total = 0
    for n in args:
        total += n
    return total

def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add=3,multiply=5)

yup = add(1,2,3,4,5,6,7,8,9,10)
print(yup)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.model = kw.get("model")
        self.make = kw.get("make")

my_car = Car(make="Nissan",model="Tesla")
print(my_car.model)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)