primeNum = []

number=int(input("enter a value: "))
def isPrime(d):
    i = 2
    while (i < d):
        if d % i == 0:
            return False
        i = i + 1
    return True


def printNum(l):
    m = 2
    while m <= l:
        if isPrime(m):
            primeNum.append(m)
        m= m + 1


printNum(number)

numOfPrime = len(primeNum)
sum = 0

b = 0
while b< numOfPrime:
    sum += primeNum[b]
    b = b + 1

ans = sum / numOfPrime

print(ans)
