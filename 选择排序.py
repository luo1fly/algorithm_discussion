#!/usr/bin/env python
# author: luo1fly

import time
import random
# import custom modules above


def select_sort(lst1):
    lst = lst1[:]
    # lst = lst1
    for i in range(len(lst)):
        minimum = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst

if __name__ == '__main__':
    opt_lst = []
    for t in range(10):
        opt_lst.append(random.randrange(0, 100))
    start = time.time()
    ret_lst = select_sort(opt_lst)
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