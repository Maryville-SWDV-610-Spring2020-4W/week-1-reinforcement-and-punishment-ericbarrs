def newInput(question):
    x = input(question + '\033[1m')
    print('\033[0m', end="")
    return x

def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False


print('Check to see if a number is a multiple.')
n = int(newInput('Enter a number '))
m = int(newInput('Enter the multiple '))
print(is_multiple(n,m))
print()