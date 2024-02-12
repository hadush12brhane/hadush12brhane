"""# Defining Function
def f(x):
    return x**3 - 5*x - 9

# Implementing Bisection Method
def bisection(x0, x1, e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > e
    print('\nRequired Root is : %0.8f' % x2)

# Input Section
x0 = float(input('First Guess: '))
x1 = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))

# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0, x1, e)
"""
#Implement bisection method using python programming language.


def bisection_method(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        return None  # Bisection method fails if f(a) * f(b) > 0
    c = (a + b) / 2.0
    iteration = 1

    print("iteration ","c      ", "f(c)" )
    while True:
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        print( " ", iteration,"    ",c,"    ",f(c))
        
        if abs(f(c))<=tol:
            break
        c = (a + b) / 2.0
        iteration += 1
        


    return c, iteration  # Failed to find a root within max_iterations

def f(x):
    return x**3 - 2*x - 5
    
C, iterations = bisection_method(f, 2, 3)
#print("root :",f(C))
