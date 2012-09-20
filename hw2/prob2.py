# ECE 2524 Homework 2 Problem 2 <Samy Abidi>
Blacksburg = "Blacksburg"
f = open('account.txt', 'r')
print 'ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS'
for line in f:
        test = line.split()
        if test[3] == Blacksburg:
            print test[4] +', '+test[1]+', '+test[0]+', '+test[2]

