
def Permutation(res, string, i):  
    if string == None:  
        return  
    if string[i] == '':  
        # print("%s\n"%string)
        res.append("".join(string[:(len(string)-1)]))  
    else:  
        for j in range(i,len(string)-1):              
            string[j],string[i] = string[i],string[j]  
            Permutation(res, string, i+1)  
            string[j],string[i] = string[i],string[j]  
    return res
# res = []
# res = Permutation(res, ['a','b','c','d', ""], 0)     
