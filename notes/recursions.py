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