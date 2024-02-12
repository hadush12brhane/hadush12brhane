"""def jacobi(A, b, N=25, x=None):
    #Solves the equation Ax=b via the Jacobi iterative method.
    # Create an initial guess if needed
    if x is None:
        x = [0] * len(A[0])

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = [A[i][i] for i in range(len(A))]
    R = [[A[i][j] for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        R[i][i] = 0
        for j in range(len(A)):
            if i != j:
                R[i][j] = -A[i][j]

    # Iterate for N times
    for k in range(N):
        x_new = [0] * len(x)
        for i in range(len(A)):
            s = sum([R[i][j] * x[j] for j in range(len(A))])
            x_new[i] = (b[i] - s) / D[i]
        x = x_new
    return x

A = [[2.0,1.0],[5.0,7.0]]
b = [11.0,13.0]
guess = [1.0,1.0]
sol = jacobi(A,b,N=25,x=guess)

print("A:")
print(A)
print("b:")
print(b)
print("x:")
print(sol)
"""



def jacobi_method(A, b, x0, tol=0.05, max_iterations=100):
    # Checks if matrix satisfies Diagonal Dominance.
    diagonals = [abs(A[i][i]) for i in range(len(A))]
    row_sums = [sum([abs(j) for j in A[i]]) - diagonals[i] for i in range(len(A))]

    for i in range(len(diagonals)):
        if abs(diagonals[i]) < row_sums[i]:
            print("The matrix doesn't satisfy diagonal dominane.")
            return

    n = len(A)
    x = x0[:]
    x_new = x0[:]
    iteration = 1
    print("iteration  ", "x", "y", "z")
    while True:
        for i in range(n):
            coeff_sum=0
            for j in range(n):
                if j != i:
                    coeff_sum=coeff_sum + A[i][j] * x[j]
                    
            x_new[i] = (b[i] - coeff_sum) / A[i][i]

        print(iteration,end=" =>")
        for m in range(n):
            print( x_new[m], end = "  ")
            
            if abs(x_new[m] - x[m]) < tol :
                return x_new, iteration + 1
        print()    
        x = x_new[:]
        iteration += 1


A = [[4,1,1],
     [1,5,2],
     [1,2,3]]
b = [2,-6,-4]
initial_guess = [0.5, -0.5, -0.5]
jacobi_method(A, b, initial_guess)

