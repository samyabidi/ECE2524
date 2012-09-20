ECE2524
=======

all class assignments

# ECE 2524 Homework 2 Problem 1 <Samy Abidi>
print "prob1 testing"
f = open('/etc/passwd', 'r')
for line in f:
        test = line.split(':')
        print test[0] + "   " + test[6],
print "prob1 done"

# ECE 2524 Homework 2 Problem 2 <Samy Abidi>
Blacksburg = "Blacksburg"
f = open('account.txt', 'r')
print 'ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS'
for line in f:
        test = line.split()
        if test[3] == Blacksburg:
            print test[4] +', '+test[1]+', '+test[0]+', '+test[2]


# ECE 2524 Homework 2 Problem 3 <Samy Abidi>
f = open('account.txt', 'r')
print 'ACCOUNT SUMMARY'
total =  0
count = 0
maximum = 0
minimum = 1000000.00
max_name = "NULL"
min_name = "NULL"
for line in f:
        test = line.split()
        temp = test[2]
        total = total + float(test[2])
        temp = float(test[2])
        if temp > maximum:
            maximum = temp
            max_name = test[1]
        if temp<minimum:
            
            minimum = temp
            min_name = test[1] 
            
            
        count = count + 1
            
print "Total amount owed = ", total
print "Average amount owed = ", total / count
print "Maximum amount owed = "+ str(maximum) + " by " + max_name
print "Minimum amount owed = "+ str(minimum) + " by " + min_name

