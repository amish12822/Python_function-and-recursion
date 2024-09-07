"Print number 5 to 1 using Recursion"

def pri(n):
    
    if (n==0):
        return
    print(n)
    pri(n-1)

pri(int(input("enter no.: ")))