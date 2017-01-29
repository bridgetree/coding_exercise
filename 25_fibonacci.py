def fib(x):
    if x==0:
        return 0
    if x==1:
        return 1

    return fib(x-1) + fib(x-2)

# Dynamic Programming

# finding fibonacci numbers using dynamic programming

mem = {0: 0, 1: 1}
def fib(x):
    if x in mem:
        return mem[x]
    r = fib(x-1) + fib(x-2)
    mem[x] = r
    return r
