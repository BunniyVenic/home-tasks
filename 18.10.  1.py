n=int(input())
def rec(x):
    if x<n+1:
        print (x)
        rec (x+1)
        print (x)
rec(1)