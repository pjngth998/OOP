
def palimdrome(check:str) -> bool:
    for k in range(0,int(len(check)/2)):
        if check[k]!=check[len(check)-k-1]:
            return False
    return True

n = input("Enter digits : ")
if n.isdigit() == False:
    print("Invalid Input")
    exit()

n = int(n)
if n <= 1 :
    print("Invalid Input")
    exit()

max = 0

for i in range((10**n),int((10**(n-1)-1)/2),-1):
    for j in range((10**n),int((10**(n-1)-1)/2),-1):
        
        temp = i*j
        if max > temp:
            break
        temp = str(temp)
        if palimdrome(temp):
            temp = int(temp)
            if max<temp:
                max = temp
        
print(max)
