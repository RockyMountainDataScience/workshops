import numpy as np

def fib(n):
    """
    This function returns the n'th Fibonacci number.
    """
    N = n+2
    f = np.nan*np.zeros(N) # Initialize an empty array
    f[0] = f[1] = 1 # Starting Fibonacci numbers

    # Estimate the rest
    for i in range(2, N):
        f[i] = f[i-1] + f[i-2]
    return f[-1]

print(fib(10)) # 10th Fibonacci number should be 55