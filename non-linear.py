import numpy as np

def partial_derivative(f, x, y, h = 1e-6):
    """
        computes the partial derivative with respect to x and y at points x and y with a step of h
        returns [del f /del x, del f / del y]
    """
    del_x = ( (f(x + h,y) - f(x - h,y) ) / 2 * h) * ( 1 / h**2) # the last part removes the exponent from the returned value
    del_y = ( (f(x, y + h) - f(x, y - h)) / 2 * h  ) * (1 / h ** 2) # the last part removes the exponent from the returned value

    return [ del_x, del_y] 


def solve_non_linear_eqn(f,g, x, y, n = 2):
    
    def fn(str):
        def f(x,y):
            return eval(str)

        return f
    f = fn(f)
    g = fn(g)


    i = 1
    while i < n:

        f_0 = f(x,y)
        g_0 = g(x,y)
        delf_delx, delf_dely = partial_derivative(f,x,y)
        delg_delx, delg_dely = partial_derivative(g,x,y)

        mat_d = np.array([[delf_delx, delf_dely], [delg_delx, delg_dely]])
        mat_h = np.array([[-f_0, delf_dely], [-g_0, delg_dely]])
        mat_k = np.array([[delf_delx, -f_0], [delg_delx, -g_0]])
    
        D = round(np.linalg.det(mat_d), 5)
        if D == 0:
            break
        k = (1 / D) * round(np.linalg.det(mat_k),5)
        h = (1 / D) * round(np.linalg.det(mat_h),5)
        x = x + round(h,5)
        y = y + round(k,5)

        i += 1
        
    print(f"x = {x}, y = {y} iterated {i} times")

    return [x, y]

print("x**2 + y**2 - 1 = 0","y - x**3 = 0") 
solve_non_linear_eqn("x**2 + y**2 - 1","y - x**3" ,0.5,0.5,10)
print("x**2 + y - 11 = 0","y**2 + x - 7 = 0") 
solve_non_linear_eqn("x**2 + y - 11","y**2 + x - 7" ,0.1,0.1,10)
