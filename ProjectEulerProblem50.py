__author__ = 'prageeth'

def creatingThePrimeList(n):

    toCheckList = list(range(n+1))
    fin = int(n**0.5)

    for i in range(2, fin+1):
        if not toCheckList[i]:
            continue
        toCheckList[2*i::i] = [None] * (n//i - 1)
    return [i for i in toCheckList[2:] if i]


def testingForSumOfConsecutivePrimes(limit):
    checkingSumOfPrimes = creatingThePrimeList(limit)
    largest = 0
    chain = []
    for start in range(10):
        seq = checkingSumOfPrimes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > limit:
                break
            i += 1
            if total in checkingSumOfPrimes:
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
                    print c
    print(sum(chain))


if __name__ == "__main__":
    limit=1000000
    testingForSumOfConsecutivePrimes(limit)