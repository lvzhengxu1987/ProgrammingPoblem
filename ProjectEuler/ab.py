def FFibonacci(n):
    if n == 1 or n == 0:
        return 1
    return FFibonacci(n-1) + n

print FFibonacci(999)
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





