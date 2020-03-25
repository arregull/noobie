#Slow. 
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
		
		
		
		
#Fast		
fib_cache = {}
def fibonacci_2(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n > 2:
        value = fibonacci_2(n-1) + fibonacci_2(n-2)
        
    fib_cache[n] = value
    return value
