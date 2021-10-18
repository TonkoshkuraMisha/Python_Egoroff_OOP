var = 1
def method():
    var = 3
    def method1():
        global var
        return var
    def method2():
        nonlocal var
        var = 2
        return var
    return method1() + method2() + var
print(method())