#https://projecteuler.net/problem=504

import math

#Pick's theorem gives a relation to area, interior points and boundary point
def pick_thm(a,b,c,d):
    area = (a+c)*(b+d)
    boundary_pt = math.gcd(a, b) + math.gcd(b, c) + math.gcd(c, d) + math.gcd(a, d)
    return (area - boundary_pt)//2 + 1

#Recursively go through the 100**4 possibilities.
#This can be further optimize for symmetry to reduce the search space.
def combination(cur_list, n, l):
    if len(cur_list) == l:
        if math.sqrt(pick_thm(*cur_list)).is_integer():
            res.append(cur_list)
        return
    for i in range(1, n+1):
        new_list = cur_list[:]
        new_list.append(i)
        combination(new_list, n, l)

res = []
combination([], 100, 4)
print(len(res))
