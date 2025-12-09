def main():
    user = input("Enter your input : ")
    if user[0] != '[' or user[-1] != ']':
        print("Invalid Input")
        return
    
    for i in range(1,len(user)-1):
        if user[i] == '[' or user[i] == ']':
            print("Invalid Input")
            return 

    if "[" not in user:
        print("Invalid Input")
        return

    if "]" not in user:
        print("Invalid Input")
        return
    
    if "," not in user:
        print("Invalid Input")
        return
    
    for i in user:
        if i.isalpha():
            print("Invalid Input")
            return
            
    user = user[1:-1].split(',')
    if len(user) < 2:
        print("Invalid Input")
        return 
    
    
            
    ls = [int(i) for i in user]
    max = -999
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i == j:
                continue
            else:
                if ls[i]*ls[j] > max:
                    max = ls[i]*ls[j]
    print(max)
main()