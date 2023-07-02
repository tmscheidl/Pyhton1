def fib(n:int) -> int:
  #  i,j = n-1, n-2
    
    if n == 0:
        return 0
    elif n <= 0:
        return -1
    elif n ==1:
        return 1
    else:
    #return (fib(i + j))         
        return (fib(n-1) + fib(n-2))


#fib(int(input()))

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(-2))
