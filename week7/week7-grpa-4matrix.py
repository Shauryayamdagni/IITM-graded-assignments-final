m=int(input())
n=int(input())
mat=[]
for x in range(0,m):
    l = input()
    row=l.split(" ")
    for x in range(0,len(row)):
        row[x]=int(row[x])
    mat.append(list(row))
for x in range(0,m):
    for y in range(0,n):
        if((x==0) or (y==0) or (y==n-1) or (x==m-1)):
            f=0
        else:
            mat[x][y]=0
for x in range(0,m):
    for y in range(0,n):
        if( y!=n-1):
            print(mat[x][y],end=" ")
        else:
            print(mat[x][y],end="")
    print(end="\n")
