
def Fibonacci(n):
    if n == 1 or n == 0:
        return 1
    return Fibonacci(n-1) + n

#print Fibonacci(10)
i = 0
while True:
    value = Fibonacci(i)
    i += 1
    
    if value % 2 == 0 and value <= 4000000 :
        sum += value
    if value > 4000000 :
        break
print sum






