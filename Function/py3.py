"WAF to find the factorial of n. (n is the parameter)"

def fac(n):
    fact = 1
    for num in range(1, n+1):
        fact = fact * num
    
    print(fact)


fac(5)
