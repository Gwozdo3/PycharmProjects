def fib(n):
    print "n =", n
    if n > 1:
        return n*fib(n - 1)
    else:
        print "koniec"
        return 1
print fib(4)