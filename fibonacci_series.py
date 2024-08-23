def fibonacci_series(n):
    a, b = 0, 1 
    while a <= n:
        print(a)
        a, b = b, a + b  
    print()  

n = int(input("Enter a number: "))
fibonacci_series(n)
