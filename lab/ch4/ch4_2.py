print(" *** Arithmetic Sequence ***")
try:
    ip = input("Enter 2 numbers : ").strip().split(" ")
    n1,n2 = [int(x) for x in ip]
    sum = n1
    for i in range(10):
        if i == 0:
            print(n1,end=" ")
        else:
            sum += n2
            print(sum,end=" ")
    print("")
    print("===== End of program =====")
except:
    print("")