x = float(input('Give me a number:'))


def FizzBuzz (x):
  if ((x % 3.0== 0) and (x % 5.0== 0)) :
    return (print('FizzBuzz'))
  elif (x % 3.0== 0):
    return (print('Fizz'))
  elif (x % 5.0== 0):
    return (print('Buzz'))
  else:
    return (print('Nothing'))

FizzBuzz (x)