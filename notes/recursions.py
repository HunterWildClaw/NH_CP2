# Recursion notes

number = 5
factorial =1

while number >0:
    factorial *= number
    number -= 1

print(factorial)

def factor(num):
    if num == 1: return 1
    return num * factor(num-1)
    
print(factor(5))
number = 10
sequence=[1,1]

for i in range(1, number):
    sequence.append(sequence[i]+sequence[i-1])

print(sequence)

recursive_sequence=[1,1]
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        recursive_sequence.append(recursive_sequence[fibonacci(n)] + recursive_sequence[n-1])

def fibonacci(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    else: return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))