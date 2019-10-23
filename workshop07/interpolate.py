import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

print(f'Scipy version {scipy.__version__}')


# This program will interpolate a general polynomial over 
# x. There is a suddle bug in the interpolate_polynomial
# function. Can you find it without print statements?

def interpolate_polynomial(x, p, kind='linear'):
    """
    This function interpolates a polynomial of ordern len(p). 
    The output is an interpolated polynomial function of order

    y = p[0] + p[1]*x^1 + p[2]*x^2...
    """

    y = np.zeros_like(x)

    # Find y(x) given all polynomial parameters p
    for power, p_i in enumerate(p):
        y =+ p_i * x**power
    
    # Interpolate
    y_interp = scipy.interpolate.interp1d(x, y, 
                kind=kind)
    return y_interp

if __name__ == '__main__':
    x = np.linspace(0, 10, num=3) # num=50 is the default value
    p = [20, 0, 2]

    x_interp = np.linspace(0, 10, num=100)
    y_interp = interpolate_polynomial(x_interp, p)
    plt.scatter(x, y_interp(x), label='raw', c='k')
    plt.plot(x_interp, y_interp(x_interp), label='interpolated')
    plt.title(r'Interpolating $y = 20 + 2x^2$')
    plt.xlabel('x'); plt.ylabel('y')
    plt.legend()
    plt.show()
