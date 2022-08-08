primeNum = []

number=int(input("Enter Number: "))
def isPrime(w):
    i = 2
    while (i < w):
        if w % i == 0:
            return False
        i = i + 1
    return True


def printNum(l):
    a= 2
    while a <= l:
        if isPrime(a):
            primeNum.append(a)
        a= a + 1


printNum(number)

numOfPrime = len(primeNum)
sum = 0

g = 0
while g< numOfPrime:
    sum += primeNum[g]
    g = g + 1

ans = sum / numOfPrime

print(ans)
