#!/usr/bin/env python
# author: luo1fly

import time, random
# import custom modules above


def insert_sort(lst1):
    lst = lst1[:]
    # lst = lst1
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while j > 0 and current < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = current
    return lst

if __name__ == '__main__':
    opt_lst = []
    for t in range(10):
        opt_lst.append(random.randrange(0, 100))
    start = time.time()
    ret_lst = insert_sort(opt_lst)
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