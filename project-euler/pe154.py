# https://projecteuler.net/problem=154
# How many coefficients in the expansion of (x + y + z)^200000 are multiples of 10^12?

import math

def div_count(n, p):
    cnt = 0
    bas = p
    while (math.floor(n / bas) > 0):
        cnt += math.floor(n / bas)
        bas *= p
    return cnt

precomp_div_count = {}
for n in range(0, 200001):
    precomp_div_count[n] = (div_count(n,2), div_count(n, 5))

CONS_DIV_2 = precomp_div_count[200000][0]
CONS_DIV_5 = precomp_div_count[200000][1]
tot = 0

for i in range(0,200001):
    if i % 1000 == 0:
        print(i)
    for j in range(0,200001-i):
        k = 200000 - i - j
        pow_5 = CONS_DIV_5 - precomp_div_count[i][1] - precomp_div_count[j][1] - precomp_div_count[k][1]
        if pow_5 >= 12:
            pow_2 = CONS_DIV_2 - precomp_div_count[i][0] - precomp_div_count[j][0] - precomp_div_count[k][0]
            if pow_2 >= 12:
                tot += 1

print(tot)
