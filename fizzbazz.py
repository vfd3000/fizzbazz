def fizzbuzz(x):
    result = str(x)
    if x % 3 == 0 and x % 5 == 0:
        result = 'FizzBuzz'
    elif x % 3 == 0:
        result = 'Fizz'
    elif x % 5 == 0:
        result = 'Buzz'
    return result