# ECE 2524 Homework 3 Problem 2 <Samy Abidi> change
import argparse, fileinput, string
from optparse import OptionParser
import sys
i = 0;
temp = range(0);
#state variables for different CLA
ignoreblank = 3;
ignoreint = 3;
ignoreh = 3;
ignorehelp = 3;
wasfile = 0;

parser = OptionParser();
parser.add_option("--ignore-blank", nargs=2);
parser.add_option("--ignore-non-numeric", nargs=3);

print(sys.argv[1:]);

#testing for CLA
try:
    sys.argv.remove('--ignore-blank');
    ignorebblank = 1;
except ValueError:
    print("ignore blank");
    ignorebblank = 0;
try:
    sys.argv.remove('--ignore-non-numeric');
    ignoreint = 1;
except ValueError:
    print("ignore int");
    ignoreint = 0;
try:
    sys.argv.remove('-h');
    ignoreh = 1;
    sys.stdout.write("process some values \n");
    sys.exit(0); 
    sys.ex
except ValueError:
    print("ignore -h");
    ignoreh = 0;
try:
    sys.argv.remove('-help');
    ignorehelp = 1;
    sys.stdout.write("show the help message and exit \n");
    sys.exit(0);
except ValueError:
    print("ignore -help");
    ignorehelp = 0;
    
#loading files into array
for line in fileinput.input():
    temp.append(line);
    temp[i] = temp[i].replace('\n','');
    if(ignorebblank ==1):#delete blanks
        if(temp[i] == ''):
            print("inside ignorebblank");
            temp.pop(i);
            i = i-1;
    if(ignoreint ==1):
        try:#to determine if the array value is an integer or not and delete it if not
            temp[i] = int(temp[i]);   
        except ValueError:
            temp.pop(i);
            i = i-1;
            print("non int found and deleted");
    i = i +1;
    wasfile = 1;
#print(temp); #the final array of all values inside the array

#checking if there are items in the array
if (len(sys.argv)>1):#if their is 1 or more argv
    argval = sys.argv[1];
else:
    argval = '';
#checking for the blank like commmand which is bad not really sure if this is doing it
if((((argval != '-h') and (argval != '-help')) and (argval != '')) and (wasfile != 1)):
    sys.stdout.write("not the correct CLA from standard \n");
    sys.stderr.write("not the correct CLA from error\n");
    sys.exit(12); 
    

#this is logic for if you are inputting values by hand or file
#####################################################
######################################################

mul1 = 1; 
var = 0;
#file or hand

try:
    if(wasfile == 1):
        mul1 = int(temp[0]);   
    else:
        mul1 = int(mul1);
except ValueError:
        sys.stderr.write("none integer\n");
        sys.exit(1);
#break from integer input use and code for file input use
j = 1;
while (var == 0):
    print("in while loop");
    try:
        if(wasfile == 1):
            mul2 = temp[j];
        else:
            mul2 = raw_input();
        if (mul2 == ''):
            print(mul1);
            mul1 = 1;
            mul2 = 1;
    except EOFError:
        sys.stderr.write("end of file\n");
        sys.exit(1);
    try:
        mul2 = int(mul2);   
    except ValueError:
        sys.stderr.write("none integer\n");
        sys.exit(1);
    mul1 = mul1 * mul2; #mult the two values
    if(j == (len(temp)-1)):
        var =1;
    else:
        j = j+1;
print("final total");
print(mul1);















