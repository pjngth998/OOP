def main():
    time = input("Enter your input : ").split()
    if len(time) != 4:
        print("Invalid Input")
        return
    for i in time:
        if i.isalpha():
            print("Invalid Input")
            return
    hr_in = int(time[0])
    min_in = int(time[1])
    hr_out = int(time[2])
    min_out = int(time[3])
    if hr_in < 7 or hr_out > 23 or min_in > 59 or min_in < 0 or min_out > 59 or min_out < 0 :
        print("Invalid Input")
        return
        

    sum_in = hr_in*60 + min_in
    if sum_in > 23*60 or sum_in < 7*60 :
        print("Invalid Input")
        return
    sum_out = hr_out*60 + min_out
    if sum_out > 23*60 or sum_out < 7*60 :
        print("Invalid Input")
        return
    del_time = sum_out - sum_in
    if del_time < 0:
        print("Invalid Input")
        return
    if del_time % 60 != 0:
        remain = 1
    else :
        remain = 0
    sum_time = int((del_time/60) + remain)
    
    if del_time <= 15:
        print(0)
    elif del_time > 15 and sum_time <= 3:
        print(sum_time*10)
    elif sum_time > 3 and sum_time <=6:
        print(30 + (sum_time-3)*20)
    elif sum_time > 6 :
        print(200)

main()