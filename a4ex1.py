def fib(n:int) -> int:
    
    i, n1, n2= 0, 0, 1
    
    if n < 0:
        return print("fib("+str(n)+") =", -1)
    elif n == 1:
        return 1
    else:
        for i in range(n):
           # print("fib ("+str(i)+")=",n1)
            F = n1 + n2
            n1 = n2
            n2 = F
        print("fib ("+str(i+1)+")=",n1)

        return


#fib(int(input()))
fib(0)
fib(1)
fib(2)
fib(3)
fib(7)
fib(-2)

