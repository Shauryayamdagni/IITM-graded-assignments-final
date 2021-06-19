def tempdic(l,subject):
    dict={}
    for x in range(1,len(l)):
        dict[subject[x]]=l[x]
    return dict


TEST_CASE=str(input())
n=int(input())
line=str(input())
id_subj=line.split(",")
students={}
for x in range(1,n+1,1):
    line=str(input())
    temp=line.split(",")
    for y in range(0,len(temp)):
        temp[y]=int(temp[y])
    #print(temp)
    students[x]=dict(tempdic(temp.copy(),id_subj))