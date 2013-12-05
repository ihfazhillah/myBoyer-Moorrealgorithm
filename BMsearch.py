#!coding:UTF-8

bad_table={}
good_table={}
s_len=0
d_len=0

def use_bad_table((wrong_word,s_now)):
    return 7
    
def use_good_table((wrong_word,s_now)):
    return 1
    
def check_word(src,dst,total_position):
    global bad_table
    global good_table
    global s_len
    global d_len
    
    s_now = s_len-1
    dic=dict.fromkeys(src,1)
    if src[-1] != dst[total_position]:
        if src[-1] not in dic:
            return 1,s_len
        else :
            return 2,(src[-1],s_now)
    else:
        d_now = total_position
        while s_now>=0:
            s_now -= 1
            d_now -= 1
            if src[s_now] != dst[d_now]:
                wrong_word = dst[d_now]
                return 2,(wrong_word,s_now)
                
    return 0,0
    
    
def create_bad_table(src):
    global bad_table
    
    for index,value in enumerate(src):
        if bad_table.has_key(value):
            bad_table[value].append(index)
        else:
            bad_table.setdefault(value,[index])
        
def create_good_table(src):
    global good_table
    lst=[]
    for temp in range(s_len/2,s_len):
        lst.append(src[temp:])
    good_table=dict.fromkeys(lst) 
    for key in good_table.keys():
        lenth=len(key)
        good_table[key]=[]
        for n in range(s_len-lenth):
            if key == src[n:n+lenth]:   
                good_table[key].append(n+lenth-1)
                
            
def BMsearch(src,dst):
    '''BMsearch(src,dst) -> return the first beginning src in dst
    same as string.find()
    src is the string to search
    dst is the string to be searched in'''
    
    global bad_table
    global good_table
    global s_len
    global d_len
    
    s_len=len(src)
    d_len=len(dst)
    total_position=s_len-1

    create_bad_table(src)
    create_good_table(src)
    while total_position<=d_len:
        flag,result=check_word(src,dst,total_position)
        if flag == 0:#find
            return total_position-s_len+1  
        elif flag == 1:#all move
            total_position+=result
        elif flag == 2:
            bad_dis = use_bad_table(result)
            good_dis = use_good_table(result)
            if bad_dis > good_dis:
                total_position += bad_dis
            else:
                total_position += good_dis
        
    return -1 #fail


if __name__ == "__main__":
    source="EXAMPLE"
    dest="HERE IS A SIMPLE EXAMPLE"
    result=BMsearch(source,dest)
#    print result