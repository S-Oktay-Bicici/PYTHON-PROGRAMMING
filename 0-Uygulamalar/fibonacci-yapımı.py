# ### Fibonacci dizisini yazdıran kodu yazınız
def fib(n):
    prev = 1
    current = 1
    print(prev)
    print(current)
    for i in range(n):
        next = current + prev
        print(next)
        prev = current
        current = next

fib(10)

