def my_decorator(func):
    def warpper():
        print("-- start")
        func()
        print("-- finish")
    return warpper


@my_decorator
def test():
    print("this is a test")

test()