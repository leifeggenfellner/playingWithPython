def collatz(number):
    global inputNumber
    if number % 2 == 0:
        inputNumber = number // 2
        print(number // 2)
        return number // 2
    else:
        inputNumber = 3 * number + 1
        print(3 * number + 1)
        return 3 * number + 1


try:
    inputNumber = int(input('Enter a number:\n'))
    while inputNumber != 1:
        collatz(inputNumber)
except ValueError:
    print('Error: Input was not an integer.\nPlease enter an integer.')
