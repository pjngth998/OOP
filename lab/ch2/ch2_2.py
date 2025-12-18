user = input("Input : ").split()
if len(user) > 10:
    print("Invalid Input")
    exit()
for i in user:
    if i.isdigit() == False :
        print("Invalid Input")
        exit()     
ls = [int(x) for x in user]

z = 0
for i in ls:
    if i == 0:
        z+=1

if z==len(ls):
    print("Invalid Input")
    exit()

for i in ls:
    if i > 9 or i < 0:
        print("Invalid Input")
        exit() 

ls.sort()
c = 0
for i in ls :
    if i == 0:
        c+=1
        continue
    else:
        print(i,end="")
        break
print("0"*c,end="")
for i in range(c+1,len(ls)):
    print(ls[i],end="")
