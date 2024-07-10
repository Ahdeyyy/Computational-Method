def bisection_method(f, precision = 0.0, a = 1, b = -1):
    def fn(str):
        def f(x):
            return eval(str)
        return f
    f = fn(f)
    while (f(a) * f(b)) > 0:
        if abs(f(a)) > abs(f(b)):
            b -= 0.1
        elif abs(f(a)) < abs(f(b)): 
            a += 0.1
        else:
            b = 0
            a += 2
    c = (a + b) / 2
    
    if c == 0:
        return c

    i = 1
    while f(c) != 0:
        if f(a) * f(c) > 0:
            a = c
            c = (a + b) / 2
            if abs(c - a) <= precision:
                print(f"root = {c}, iterated {i} times")
                return c
        elif f(a) * f(c) < 0:
            b = c
            c = (a + b) / 2
            if abs(c - b) <= precision:
                print(f"root = {c} iterated {i} times")
                return c
        i = i + 1

    print(f"root = {c} iterated {i} times")
    return c

print("x**3 - x - 1")
bisection_method("x**3 - x - 1")
print("x**3 - 2*x - 1")
bisection_method("x**3 - 2*x - 5")
    
def derivative(f,x ,h = 1e-6):
    """
        computes the derivative of a function f at point x with a step of h
    """
    
    return ( (f(x + h) - f(x - h) ) / 2 * h) * ( 1 / h**2) # the last part removes the exponent from the returned value


def newton_raphson_method(f, precision = 0.0, a = 1):
    MAX_ITERATION = 100
    def fn(str):
        def f(x):
            return eval(str)
        return f
    f = fn(f)
    x = a
    i = 1
    while True:
        h = - f(x) / derivative(f, x)
        x2 = x + h
        if abs(x2 - x) <= precision :
            x = x2
            print(f"root = {x} iterated {i} times")
            return x
        x = x2
        if i == MAX_ITERATION:
            break
        i = i + 1
    
    return x
#     
# print("x**3 - x - 1")
# newton_raphson_method("x**3 - x - 1", a=1)
# print("x**3 - 2*x - 1")
# newton_raphson_method("x**3 - 2*x - 5", a=2)
