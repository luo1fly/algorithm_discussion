#!/usr/bin/env python
# author: luo1fly

import random
import time
from copy import copy
# import custom modules above


def bubble_sort(lst1):
    """
    :param lst1: 待排序列表
    :return: 排序后的列表
    """
    # lst = deepcopy(lst1)
    lst = copy(lst1)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

if __name__ == '__main__':
    opt_lst = []
    for t in range(10):
        opt_lst.append(random.randrange(0, 100))
    start = time.time()
    ret_lst = bubble_sort(opt_lst)
    end = time.time()
    print(
        'opt_lst:',
        opt_lst,
        'ret_lst:',
        ret_lst,
        'time_used:',
        end - start,
        sep='\n',
    )
