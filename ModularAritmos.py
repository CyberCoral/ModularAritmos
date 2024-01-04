# ver. Tue/02/Jan/2024
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#

class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b
    def real(self):
        return self.real
    
    def imaginary(self):
        return self.imaginary

def real_mod(a, b):
    '''
    Does
    "a mod b"
    for all real a and b.
    '''
    if isinstance(a, float) != True and isinstance(a, int) != True:
        raise TypeError("'a' must be a float or int")
    if isinstance(b, float) != True and isinstance(b, int) != True:
        raise TypeError("'b' must be a float or int")
    if b == 0:
        raise ZeroDivisionError("Division by zero in function.")
    
    mod = (a / b - int(a / b)) * b
    return mod

def one_mod(a):
    '''
    Does
    "a mod 1"
    for all real a.
    '''
    mod = a - int(a)
    return mod

def floor0(a):
    '''
    Does floor(a),
    method 1 with
    a mod 1.
    '''
    return a - one_mod(a)

def floor1(a):
    '''
    Does floor(a)
    method 2 with
    int(a)
    '''
    return int(a)

def complex_mod(a: list, b: list, complex_: bool = True):
    '''
    Does
    "a mod b"
    for complex numbers
    a and b.
    List form (2 elements each).
    '''
    if isinstance(a, list) != True:
        raise TypeError("'a' must be a list.")
    elif len(a) != 2:
        raise ValueError("'a' must have 2 elements.")
    elif [isinstance(i, int) != True and isinstance(i, float) != True for i in a].count(True) != 0:
        raise TypeError("'a's elements must be int or float.")

    if isinstance(b, list) != True:
        raise TypeError("'b' must be a list.")
    elif len(b) != 2:
        raise ValueError("'b' must have 2 elements.")
    elif [isinstance(i, int) != True and isinstance(i, float) != True for i in b].count(True) != 0:
        raise TypeError("'b's elements must be int or float.")

    if isinstance(complex_, bool) != True:
        raise TypeError("complex_ must be a bool.")

    a1, a2, b1, b2 = a[0], a[1], b[0], b[1]
    dem, c_dem = b1 ** 2 + b2 ** 2, b1 ** 2 - b2 ** 2
    result = []

    if dem == 0:
        raise ZeroDivisionError("The denominator must not be zero.")

    f1 = floor1(((a1 * b1) + (a2 * b2)) / dem)
    f2 = floor1(((a1 * b2) - (b1 * a2)) / dem)

    g1 = (a1 * c_dem - (2 * a2 * b1 * b2)) / dem
    g2 = (a2 * c_dem - (2 * a1 * b1 * b2)) / dem

    result = [ g1 - (f1 * b1) + (f2 * b2), g2 + (f1 * b2) + (f2 * b1) ]

    if complex_ != True:
        return result
    return complex(result[0], result[1])

def MOD(num: list, real_nums: list, imag_nums: list, complex_: bool = True):
    '''
    Does
    'num mod a+bi'
    for as many items in
    real_nums and imag_nums are
    (they must have the same number
    of elements), includes complex
    mod
    '''
    if isinstance(num, list) != True:
        raise TypeError("'num' must be a list.")
    elif len(num) != 2:
        raise ValueError("'num' must have 2 elements.")
    elif [isinstance(i, int) != True and isinstance(i, float) != True for i in num].count(True) != 0:
        raise TypeError("'num's elements must be int or float.")

    if isinstance(real_nums, list) != True:
        raise TypeError("'real_nums' must be a list.")
    elif len(real_nums) < 0:
        raise IndexError("The list must not be empty.")
    elif [isinstance(i, int) != True and isinstance(i, float) != True for i in real_nums].count(True) != 0:
        raise TypeError("'real_nums's elements must be int or float.")

    if isinstance(imag_nums, list) != True:
        raise TypeError("'imag_nums' must be a list.")
    elif len(real_nums) < 0:
        raise IndexError("The list must not be empty.")
    elif [isinstance(i, int) != True and isinstance(i, float) != True for i in imag_nums].count(True) != 0:
        raise TypeError("'imag's elements must be int or float.")

    if len(real_nums) != len(imag_nums):
        raise IndexError("The num parts must have the same number of elements.")

    if isinstance(complex_, bool) != True:
        raise TypeError("complex_ must be a bool.")

    for i in range(len(real_nums)):
        num = complex_mod(num, [real_nums[i], imag_nums[i]], False)
    
    if complex_ != True:
        return num
    return complex(num[0], num[1])


    
    

    


    
