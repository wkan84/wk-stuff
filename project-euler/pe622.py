#https://projecteuler.net/problem=622
#The problem is equivalent to find all n such that 60 is the multiplicative order of 2 mod n.

#Iterate through to calculate the multiplicative order. Since it only goes up to 60, a simple loop suffice.
def multiplicative_order(b, n):
    i = b
    count = 1
    while (i != 1):
        i = (i * b) % n
        count += 1
    return count

#Given a list of prime factors and multiplicities, return all divisors.
#Only the divisors of 2^60 - 1 could have multiplicative order 60.
def findFactors(primeDivisors, multiplicity, currentDivisor, currentResult):
    if (currentDivisor == len(primeDivisors)):
        res.append(currentResult);
        return;
    for i in range(multiplicity[currentDivisor]+1):
        findFactors(primeDivisors, multiplicity, currentDivisor + 1, currentResult);
        currentResult *= primeDivisors[currentDivisor];
    
res = []
findFactors([3, 5, 7, 11, 13, 31, 41, 61, 151, 331, 1321], [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, 1)
div = res[1:]
s = 0
for d in div:
    if multiplicative_order(2, d) == 60:
        s += d + 1
print(s)
