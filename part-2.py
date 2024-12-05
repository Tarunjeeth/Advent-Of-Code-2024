file=open("input.txt","r")
data=file.readlines()
left=[]
right=[]
score=0
for i in data:
    left.append(int(i.split()[0]))
    right.append(int(i.split()[1]))
for j in left:
    count=0
    for k in right:
        if(j==k):
            count+=1
    score=score+count*j
print(score)