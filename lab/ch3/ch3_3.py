emp = ["\"\"","\'\'"]


def add_score(duck, subject, score):
    duck[subject] = score
    return duck
    
def calc_average_score(duck):
    total = list(duck.values())
    avg = sum(total)/len(total)
    return avg


try:
    ip = input("Input : ")
    ip = ip.split(" | ")
    if len(ip) != 3:
        raise Exception
    
    if ip[0]=="{}":
        cur_dict = {}
    else:
        cur_dict = eval(ip[0])
    if ip[1] in emp:
        raise Exception
    cur_subject = ip[1].replace("'",'')
    if "." in ip[2]:
        cur_score = float(ip[2])
    else:
        cur_score = int(ip[2])
    if cur_score < 0:
        raise Exception
    ans = add_score(cur_dict,cur_subject,cur_score)
    print(ans,end=", ")
    print("Average score: {:.2f}".format(calc_average_score(ans)))
    

except Exception as e:
    if type(cur_dict) == dict:
        if ip[0]=="{}":
            print(cur_dict,end=", ")
            print("Average score: 0.00")
        else:
            print(cur_dict,end=", ")
            temp = list(cur_dict.values())
            print("Average score: {:.2f}".format(temp[0]))
    else:
        print("Invalid")