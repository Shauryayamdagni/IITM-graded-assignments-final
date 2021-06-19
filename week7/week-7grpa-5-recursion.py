def collatz_repeat(n,c=0):
    if (n==1):
        return c    #because at last when n will be one then also there will be increment
    else:
        if ((n%2)!=0):
            return(collatz_repeat((3*n)+1,c+1))
        else:
            return(collatz_repeat(n//2,c+1))


print(collatz_repeat(10))