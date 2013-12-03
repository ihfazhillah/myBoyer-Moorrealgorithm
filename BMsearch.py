#!coding:UTF-8

bad_table={}
def check_other_word():
    pass

def check_word(src,dst,total_position):
    dic=dict.fromkeys(src,1)
    if src[-1] != dst[total_position-1]:
        pass
    # dst[total_position-1] in src
    pass

    
def cal_move_distance():
    pass
    
def badchar(src):
    global bad_table
    for index,value in enumerate(src):
        if bad_table.has_key(value):
            bad_table[value].append(index)
        else:
            bad_table.setdefault(value,[index])
        
        
def KMsearch(src,dst):
    '''KMsearch(src,dst) -> return the first beginning src in dst
    same as string.find()
    src is the string to search
    dst is the string to be searched in'''
    global bad_table
    s_len=len(src)
    d_len=len(dst)
    total_position=s_len
    s_now=s_len-1
    d_now=0
    dic=dict.fromkeys(src,1)
    badchar(src)
    print bad_table.items()
    # while total_position<d_len:
        # result=check_word(src,dst,total_position)
        #check result
        
        #move
        # total_position+=x
        
        # pass
        





if __name__ == "__main__":
    source="EXAMPLE"
    dest="HERE IS A SIMPLE EXAMPLE"
    KMsearch(source,dest)
