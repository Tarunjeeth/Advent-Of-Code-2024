file=open("input.txt","r")
data=file.readlines()
count=0
for i in data:
    str_l=i.split()
    a=[]
    for k in str_l:
        a.append(int(k))
    l_sort=sorted(a)
    l_sort_r=sorted(a)
    l_sort_r.sort(reverse=True)
    flag=1
    for j in range(len(a)-1):
        if (abs(a[j]-a[j+1])!=2 and abs(a[j]-a[j+1])!=1 and abs(a[j]-a[j+1])!=3):
            flag=0
    if flag==1:
        if (l_sort_r==a or l_sort==a):
            count+=1
    
print(count)