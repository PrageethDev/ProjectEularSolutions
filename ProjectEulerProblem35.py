__author__ = 'prageeth'

def primes(limit):
    numbers = range(3, limit+1, 2)
    half = (limit)//2
    initial = 4
    for step in xrange(3, limit+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)


def rotate(primeNumList):
    shuffle=[]
    for i in range(len(primeNumList)):
        shuffle.append(int(primeNumList[i:]+primeNumList[:i]))
    return set(shuffle)


def circularPrime(limit):
    primesWithinLimit = primes(limit)
    circularPrimes=[]
    numsToReject=['0','2','4','5','6','8']
    primesWithinLimit=[i for i in primesWithinLimit if not any(j in numsToReject for j in set(str(i)))]

    while primesWithinLimit:
        ShufleSet=rotate(str(primesWithinLimit[-1]))
        PrimesSet=set(primesWithinLimit)
        if not ShufleSet -  PrimesSet:
            circularPrimes+=list(ShufleSet)
        primesWithinLimit=list(PrimesSet - ShufleSet)
    circularPrimes.sort()
    return circularPrimes


def listingAndCounting(limit):
    outPut = circularPrime(limit)
    for element in outPut:
        print element
    noOfPrimes = len(outPut)
    return noOfPrimes


if __name__ == '__main__':
    limit = 1000000
    sumOfPrimes = listingAndCounting(limit)
    print '   OK, Next circular prime is greater than ' + str(limit)
    print 'Number of circular primes below ' + str(limit) + ' = ' + str(sumOfPrimes)