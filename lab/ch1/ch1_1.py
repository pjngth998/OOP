def main():
    n = (input("Input : "))
    if n.isdigit() == False :
        print("Output : Invalid Input")
        exit()
    n = int(n)
    if n > 9:
        print("Output : Invalid Input")
        return
    print("Output :", n + n*11 + n*111 + n*1111)

main()