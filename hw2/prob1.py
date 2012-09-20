# ECE 2524 Homework 2 Problem 1 <Samy Abidi>
print "prob1 testing"
f = open('/etc/passwd', 'r')
for line in f:
        test = line.split(':')
        print test[0] + "   " + test[6],
print "prob1 done"
