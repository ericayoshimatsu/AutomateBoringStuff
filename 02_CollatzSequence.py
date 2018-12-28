# Calculates de collatz sequence

def collatz(number):


    # even number
    if number%2 == 0:
        result = number//2
    # odd number
    else:
        result = 3*number +1

    print(result)
    return result


number = input()

try:
    number = int(number)

    while number > 1:
        number = collatz(number)
except ValueError:
    print('You did not entered a number >:(')