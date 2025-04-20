'''Write a Python program that prints the sum of two floating point numbers, 
the difference between two integers, and the product of a 
floating point number and an integer. In each case, have the program 
print out the data type of the resulting answer.
'''

floating_number = 5.6
floating_number2 = 7.8
integer_number = 8
integer_number2 = 13

sums = floating_number + floating_number2
difference = integer_number - integer_number2
product = floating_number * integer_number

print(f'Sum of two floating point numbers: {sums}')
print(f'Data type: {type(sums)}')
print(f'Differnece of two integer numbers: {difference}')
print(f'Data type: {type(difference)}')
print(f'Product of integer & float: {product}')
print(f'Data type: {type(product)}')