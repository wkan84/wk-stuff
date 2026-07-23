import math

digits = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]


def allsubsets(lst, sublist, init_len, res):
    if len(lst) + len(sublist) < init_len // 2:
        return res
    if len(sublist) == init_len // 2:
        res.add(tuple(sublist))
        return res
    allsubsets(lst[1:], sublist, init_len, res)
    temp = sublist[:]
    temp.append(lst[0])
    allsubsets(lst[1:], temp, init_len, res)
    return res

allsplits = allsubsets(digits, [], len(digits), set())
validsplits = []
for tup in allsplits:
    if (sum(digits) - 2 * sum(tup)) % 11 == 0:
        validsplits.append(tup)

test_tup = validsplits[1]

def tup_count(tup):
    tup_cnt = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    comp_cnt = {0:2, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2}
    
    for i in tup:
        tup_cnt[i] += 1
        comp_cnt[i] -= 1
        
    tup_val = math.factorial(9)
    if tup_cnt[0] == 0:
        tup_val *= 10
    elif tup_cnt[0] == 1:
        tup_val *= 9
    else:
        tup_val *= 8
    for c in tup_cnt.values():
        if c == 2:
            tup_val = tup_val // 2
    
    comp_val = math.factorial(10)
    for c in comp_cnt.values():
        if c == 2:
            comp_val = comp_val // 2
    return tup_val * comp_val

tot = 0
for tups in validsplits:
    tot += tup_count(tups)
    
print(tot)
