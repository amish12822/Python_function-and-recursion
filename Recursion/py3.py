"Write a recursive function to calculate the sum of first n natural numbers."

def sum1(n):
    if (n==0):
        return 0
    return sum1(n-1) + n

print(sum1(int(input("enter value: "))))