t=("zero","one","two","three","four","five","six","seven","eight","nine")
l=[]
n=int(input())
while(n>0):
    a=n%10
    l.append(t[a])
    n=n//10
for x in range(len(l)-1,-1,-1):
    print(l[x],end="\n")
print(l[len(l)-1],end="")
for x in range(len(l)-2,-1,-1):
    print(l[x].capitalize(),end="")