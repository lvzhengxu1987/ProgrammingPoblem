'''
def FFibonacci(n):
    if n <= 0 :
        return 0
    if n == 1 or n == 2:
        return 1
    return FFibonacci(n-1) + FFibonacci(n-2)

'''
def FFibonacci(n):
    suma = 0
    sumb = 0
    sum = 0
    for i in range(n):
        if  i < 0:
            break
        if i == 0 or i == 1:
            suma = suma + 1
            sumb = 1
            sum = suma
        else:
            sumb = suma
            sum = suma + sumb
            suma = sum

    return sum
#'''
print FFibonacci(11)

'''
i = 0
sum = 0
while True:
    value = FFibonacci(i)
    print value
    i += 1
    if value % 2 == 0 and value <= 4000000 :
        sum += value
    if value > 4000000 :
        break
print sum
'''