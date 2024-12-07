file=open("input.txt","r")
data=file.readlines()
count=0
iter=0
all=[]
for i in data:
    str_l=i.split()
    a=[]
    for k in str_l:
        a.append(int(k))
    l_sort=sorted(a)
    l_sort_r=sorted(a)
    l_sort_r.sort(reverse=True)
    flag=1
    problem=0
    for j in range(len(a)-1):
        if (abs(a[j]-a[j+1])!=2 and abs(a[j]-a[j+1])!=1 and abs(a[j]-a[j+1])!=3):
            flag=0
    if flag==1:
        if (l_sort_r==a or l_sort==a):
            count+=1
        else:
            flag=0
    if flag==0:
        b=[]
        for e in range(len(a)):
            c=[]
            c.extend(a)
            c.pop(e)
            b.append(c)
        all.append(b)
        b=[]
for n in range(len(all)):
    count_r=0
    for g in range(len(all[n])):
        flag_c=1
        lh_sort=sorted(all[n][g])
        lh_sort_r=sorted(all[n][g])
        lh_sort_r.sort(reverse=True)
        for f in range(len(all[n][g])-1):
            if (abs(all[n][g][f]-all[n][g][f+1])!=2 and abs(all[n][g][f]-all[n][g][f+1])!=1 and abs(all[n][g][f]-all[n][g][f+1])!=3):
                flag_c=0
        if flag_c==1:
            if (lh_sort_r==all[n][g] or lh_sort==all[n][g]):
                count_r+=1
    if count_r>0:
        count+=1  
print(count)
