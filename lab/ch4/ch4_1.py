try:
    n = input("Sum from 1 to : ")
    n = int(n)
    x = n
    if n <= 0:
        raise Exception
    sum = 0
    while(x > 0):
        sum += x
        x -= 1
    print("Sum from 1 to {} is {}".format(n,sum))
except :
    print("Input Error")