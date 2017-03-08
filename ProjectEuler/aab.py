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
    ssum = 0
    for i in range(n):
        if  i < 0:
            break
        if   i == 0 or i == 1:
            suma=1
            sumb=1
            ssum = 1
        else:
            ssum = suma + sumb
            sumb = suma
            suma = ssum
    return ssum
#'''

#for i in range(1,100):
#    print i , FFibonacci(i)

i = 1
ssum = 0
suma = 0
while True:
    value = FFibonacci(i)
    if value % 2 == 0 and value <= 4000000 :
        ssum += value
    elif value > 4000000 :
        break
    i += 1
print ssum
