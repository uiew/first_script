#"爬取所有的 github 没有注册的4个字母以内的 id" 
# (0-9a-z) 36个字符的组合。]
import requests    

def get_all_string(all_string, string):
    url = "https://github.com/" + string
    if requests.get(url).status_code != 404:
        return 
    all_string.append(string)
    print(url+" 没有被注册")
    return  

az = [chr(x+97) for x in range(26)]
n09 =  [chr(x+48) for x in range(10)]
az.extend(n09)
chars = az

one_list = [str(x) for x in chars]
# list1 == one_list; list2 
def run_set_lists(list1, list2):
    return ["".join([x1, x2]) for x2 in list1 for x1 in list2] 

two_list = run_set_lists(one_list, one_list)
three_list = run_set_lists(one_list, two_list)
# four_list = run_set_lists(one_list, three_list)
# five_list = run_set_lists(one_list, four_list)

one_list.extend(two_list)
one_list.extend(three_list)
# one_list.extend(four_list)
# one_list.extend(five_list)

all_string = []
for x in one_list:
    get_all_string(all_string, x)

print(all_string)
