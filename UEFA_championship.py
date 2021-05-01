# cook your dish here
for i in range(int(input())):
    coll=[]
    tname=[]
    main=[]
    d={}
    for j in range(12):
        x=input().split()
        x.remove("vs.")
        x[1],x[2]=int(x[1]),int(x[2])
        coll.append(x)
        tname+=[x[0]]+[x[3]]
    tname=list(set(tname))
    for k in tname:
        d[k]=[0,0]
    for l in coll:
        s1,s2,t1,t2=l[1],l[2],d[l[0]],d[l[3]]
        t1[1]+=s1-s2
        t2[1]+=s2-s1
        if s1>s2:
            t1[0]+=3
        elif s2>s1:
            t2[0]+=3
        else:
            t1[0]+=1
            t2[0]+=1
    for key in d:
        main.append([key,d[key][0],d[key][1]])
    t=sorted(main,key=lambda x: (x[1], x[2]))
    print (t[-1][0], t[-2][0])











