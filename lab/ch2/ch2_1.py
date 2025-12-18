def main():
    n = input("Input : ")
    if n.isdigit() == False :
        print("Invalid Input")
        return  
    n = int(n)
    if n < 0:
        print("Invalid Input")
        return  
    for i in range(1,n+1):
        print(" "*(n-i),"#"*i)
main()