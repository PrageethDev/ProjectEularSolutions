__author__ = 'prageeth'

# This finds the number of days the month has
def findingDays(month, yr):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) \
       or (month == 8) or (month == 10) or (month == 12):
        d = 31
        return d
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        d = 30
        return d
    elif (month == 2):
        if yr % 4 == 0:
            if yr % 100 == 0:
                if yr % 400 == 0:
                    d = 29
                    return d
                else:
                    d = 28
                    return d
            d = 29
            return d
        else:
            d = 28
            return d

    else:
        print "There are no ", month, "months for a year"


# This finds sundays on the first of the month from 1st Jan 1900
def findingSunDays():

    counter = 0 # Start on Monday the 1st, 1900
    noOfSundays = 0

    # Year
    for year in range(1900, 2001):
        print "\nYear = ", year

        # Month
        for month in range(1, 13):
            noOfDaysForTheMonth = findingDays(month, year)

            for daysInTheMonth in range(1, (noOfDaysForTheMonth + 1)):
                counter += 1

                if (daysInTheMonth == 1) and (counter%7 == 0):
                    print "month =", month, "date from the starting count =", counter
                    noOfSundays += 1
    return noOfSundays



    # have to subtract 2 for the year 1900, to get from 1901 #so the count will be 171

if __name__ == '__main__':
    totNumOfSunsays = findingSunDays()
    print "\nNo of Sundays from 01/01/1900 - 31/12/2000 = ", (totNumOfSunsays)
    print "No of Sundays from 01/01/1901 - 31/12/2000 =", totNumOfSunsays-2