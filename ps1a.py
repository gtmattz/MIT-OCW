##Matt Zimmerman
##MIT OCW 6.00SC, Lecture 4 Problem Set 1 Assignment problem 1
##ps1a.py
##Solving for Minimum Payment

outBal = float(raw_input('Enter Outstanding Balance: '))
annInt = float(raw_input('Enter Annual Interest Rate: '))
minMop = float(raw_input('Enter Minimum monthly payment rate: '))

totPaid = 0.0

for i in range(12):

    minDue = minMop*outBal
    intPaid = (annInt/12)*outBal
    priPaid = minDue - intPaid
    outBal -= priPaid
    totPaid += minDue
    print "Month: ", i+1
    print "Minimum Due: $", round(minDue, 2)
    print "Principal paid: $", round(priPaid, 2)
    print "Remaining Balance: $", round(outBal, 2)

print ".........."
print "Result:"
print "Total Paid: $", round(totPaid, 2)
print "Remaining Balance: $", round(outBal, 2)