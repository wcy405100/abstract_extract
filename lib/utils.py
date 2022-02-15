# -*- coding: utf-8 -*-

import numpy as np


'''
# 注意输入格式：[(文本1，序号1),(文本2，序号2)]，序号在文本后
# 返回格式：[文本1，文本2],[序号1，序号2]
'''
def sort_tuple_list(tplist):
    ordered=sorted(tplist,key=lambda x:x[-1])
    return [i[0] for i in ordered],[i[1] for i in ordered]

def return_index(score_list,sum_size):
    ind = np.argpartition(score_list,-(sum_size))[-(sum_size):]
    return ind

def vote_all(all_list,all_indx,susize):
    unique_hash =[]
    unique_sum =[]
    unique_count =[]
    for ind,ele in enumerate(all_list):
        hele = hash(ele)
        if hele not in unique_hash:
            unique_hash.append(hele)
            unique_sum.append((ele,int(all_indx[ind])))
            unique_count.append(1)
        else:
            id = unique_hash.index(hele)
            unique_count[id] += 1
    if int(susize)<len(unique_sum):
        index_list = return_index(np.array(unique_count),int(susize))
        tpl = []
        for i in index_list:
            tpl.append(unique_sum[i])
        res,index_list = sort_tuple_list(tpl)
        return res,index_list
    else:
        res,index_list = sort_tuple_list(unique_sum)
        return res,index_list