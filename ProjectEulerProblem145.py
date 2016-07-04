__author__ = 'prageeth'

def sumrevers(chekingNum):
    summation = chekingNum + int(str(chekingNum)[::-1])
    if summation % 2 != 0:
        return summation

def checknum(num):
    if not (str(num)[-1] == "0") or (str(num)[0] == "0"):
        if type(sumrevers(num)) == int:
            num = str(sumrevers(num))
            checklis = [checkedNum for checkedNum in str(num)]
            if all(int(checkOdd) % 2 != 0 for checkOdd in checklis):
                return True

def outAnswers(limit):
    cnt = 0
    for num in xrange(1, limit):
        if checknum(num):
            cnt += 1
            print num
    return cnt

if __name__ == '__main__':
    limit = 1000
    answer = outAnswers(limit)
    print 'There are ', answer, ' reversible numbers below ', limit