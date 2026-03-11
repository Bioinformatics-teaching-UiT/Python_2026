"""
FizzBuzz exercise

Write a script that goes through the numbers 1 to 100.

If the number is divisible by 3 and 5, output 'FizzBuzz'.

If the number is divisible by 3 (but not 5), output 'Fizz'.

If the number is divisible by 5 (but not 3), output 'Buzz'.

Otherwise, just print out the number.
"""

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)