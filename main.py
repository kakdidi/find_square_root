# Find Square Root
'''
in this example, we will learn to find the square root of a number. 
We will create two source codes.
1. To find the square root of a real number.
2. To find the square root of a complex number.
'''
# Change this value and test yourself
num = 6.25

# ** is used for exponentiation
num_sqrt = num ** 0.5
print('The square root of', num, 'is:', num_sqrt)

print(''' 
===Explanation===
in the program, we used ** to find the power of a number. 
The square root of num variable is computed using,

num_sqrt = num ** 0.5
''')

# The resul is stored in the num_sqrt variable
# here, we have reised num to the power of 0.5 which gives us the square root.

#find the square root of real or complex numbers
# import the complex math module

import cmath

num = 64-64j

num_sqrt = cmath.sqrt(num)
print('The square root of', num, 'is', num_sqrt)

angka = float(input('Masukkan angkanya : '))
konv = cmath.sqrt(angka)
print('Hasil akar kuadratnya adalah :', konv) 