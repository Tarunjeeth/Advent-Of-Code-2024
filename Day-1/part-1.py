file=open("input.txt","r")
data=file.readlines()
left=[]
right=[]
count=0
for i in data:
    left.append(int(i.split()[0]))
    right.append(int(i.split()[1]))
left.sort()
right.sort()
for i in range(len(left)):
    count+=abs(left[i]-right[i])
print(count)
