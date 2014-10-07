##Matt Zimmerman
##MIT OCW 6.00SC, Lecture 4 Problem Set 1 Assignment problem b
##ps1b.py
##Paying off in a year

intBal = float(raw_input('Enter the outstanding balance on your credit card: '))
annInt = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

minMop = 0
monInt = annInt/12
bal = intBal
numMon = 0

while bal > 0:

    minMop += 10
    bal = intBal
    numMon = 0

    while numMon < 12 and bal > 0:

        numMon += 1
        thisInt = monInt * bal
        bal -= minMop
        bal += thisInt

bal = round(bal, 2)
print "Result:"
print "Monthly payment to pay off in 1 year: $", minMop
print "Number of months needed: ", numMon
print "Balance: $", bal