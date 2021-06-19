def merge(D1 ,D2, priority):
    dic1={}
    dic2={}
    vip=[]
    merged={}
    if(len(D1) > len(D2)):
        dic1=D1
        dic2=D2
        if priority == "first":
            vip = D1
        else:
            vip = D2
    else:
        dic1=D2
        dic2=D1
        if priority == "first":
            vip = D1
        else:
            vip = D2
        print(dic1,dic2,vip)
    for x in dic1.keys():
        if not(x in dic2.keys()):
            merged[x]=dic1[x]
        else:
            merged[x]=vip[x]
    for x in dic2.keys():
        if not (x in dic1.keys()):
            merged[x] = dic2[x]
        else:
            merged[x] = vip[x]
    return merged


print(merge({1:10,2:20,3:30},{3:60,4:40,2:2020,40:4040},"second"))