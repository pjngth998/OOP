emp = ["\"\"","\'\'"]
proper = ["albumTitle","artist","tracks"]

def update_records(duck,id,prop,value):
    if value == "\"\"" or value == "\'\'":
        del duck[id][prop]
    elif prop != "tracks" and value not in emp:
        if ip[0]=="{}":
            susu = {prop:value}
            duck[id] = susu
        else:
            duck[id][prop] = value
    elif prop == "tracks":
        if "tracks" not in ip[0]:
            if ip[0]=="{}":
                susu = {"tracks":[value]}
                duck[id] = susu
            else:
                duck[id]["tracks"] = [value]
        else:
            duck[id]["tracks"].extend([value])
    return duck

    
try:
    ip = input("Input : ").split(" | ")
    if len(ip) != 4:
        raise Exception
    if ip[2] not in proper:
        raise Exception
        
    if ip[0]=="{}":
        cur_dict = {}
    else:
        cur_dict = eval(ip[0])
    cur_id = ip[1]
    cur_prop = ip[2]
    cur_value = ip[3]
    if cur_id == "" or cur_prop=="" or cur_value=="":
        print("Invalid")
        exit()
    print(update_records(cur_dict,cur_id,cur_prop,cur_value))

except Exception as e:
    print("Invalid")


