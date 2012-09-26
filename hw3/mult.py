# ECE 2524 Homework 3 Problem 1 <Samy Abidi>
import sys
if (len(sys.argv)>1):
    argval = sys.argv[1];
else:
    argval = '';
if(((argval != '-h') and (argval != '-help')) and (argval != '')):
    sys.stdout.write("not the correct CLA from standard \n");
    sys.stderr.write("not the correct CLA from error\n");
    sys.exit(12); 
if (argval == '-h'):
    sys.stdout.write("process some values \n");
    sys.exit(0); 
    sys.ex
if (argval == '-help'):
    sys.stdout.write("show the help message and exit \n");
    sys.exit(0);
mul1 = 1; 
var = 0;
mul1 = raw_input();
try:
        mul1 = int(mul1);   
except ValueError:
        sys.stderr.write("none integer\n");
        sys.exit(1);
while (var == 0):
    print("in while loop");
    try:
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
    mul1 = mul1 * mul2;
print("done");
