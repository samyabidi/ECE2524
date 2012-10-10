# ECE 2524 Homework 4 Problem 1.1 <Samy Abidi> change
import argparse, fileinput, string
from optparse import OptionParser
import sys
import operator
#the list of dictionary structures
ldlist = [];
ldlistsort = [];
ldlist2 = [];
#the list of lines inside the action file
filelist = [];
#print "beginning inventory actions";
#when you are loading action, and also loading the results into an output file filelist is zero otherwise it is one

#loads the data file into an array
def create_dic(arg1):
    count = 0;
    count2 = 0;
    f = open(arg1, 'r');
    for line in f:
        line = line.replace('\n','');
        if(count == 0): 
           line1 = line; 
        if(count == 1):
           line2 = line;
        if(count == 2):
           line3 = line;
        if(count == 3):
           line4 = line;
        if(count == 4):
           count = 0;
           count2 = count2 + 1;
           Parts = {'ItemID':line1,'Desc':line2,'Foot':line3,'Quant':line4};#filling the dictionary with choosen keys
           ldlist.append(Parts);
        else:
            count = count + 1;
    #print (ldlist); #this is all the items in inventory placed into a list of dicitonaries

def command_call():#for reading the input command file
    #temp variables
    tempid = 0;
    tempd = 0;
    tempf = 0;
    tempq = 0;
    temp1 = 0;
    arraypos = 3;
    val1 = '';
    val2 = '';
    valdescriptor1 = 0;
    valdescriptor2 = 0;
    #end temp variables
# for reading action files
    filelist = [];
    for line_input in sys.stdin:
        filelist.append(line_input.replace('\n',''));
    #checks which array position holds first value, depends on whether you are pushing values to output file
    try:
        if(filelist[0] == 'add' or filelist[0] == 'remove' or filelist[0] == 'set/update' or filelist[0] == 'list' or filelist[0] == 'sort'):
            arraypos = 0;
    except ValueError:
        arraypos = 1;
    count2 = 0;
    while(len(filelist)>count2):
        rep_done = 0;
        if(rep_done == 0):
            if(filelist[count2 + 0] == 'add'):
                #segment the rest of filelist here, then call add, then increment count2 to point to first 
                #line of new command
                tempid = filelist[count2 +1].split(':');
                tempd = filelist[count2 +2].split(':');
                tempf = filelist[count2 +3].split(':');
                tempq = filelist[count2 +4].split(':');
                add(tempid[1],tempd[1],tempf[1],tempq[1]);
                count2 = count2 + 5;
                rep_done = 1;
        if(rep_done == 0):    
        #segment values for remove and then increment count2 to move to next command if available
            if(filelist[count2 +0] == 'remove'):
                tempid = filelist[count2 +1].split(':');
                remove(tempid[0],tempid[1]);
                count2 = count2 + 2;
                rep_done = 1;
        if(rep_done == 0):
            if(filelist[count2 +0] == 'set/update'):
                val1 = filelist[count2 +1].split(':');
                val2 = filelist[count2 +2].split(':');
                valdescriptor1 = filelist[count2 +1].split(':');
                valdescriptor2 = filelist[count2 +2].split(':');
                val1 = val1[1]
                val2 = val2[1]
                valdescriptor1 = valdescriptor1[0];
                valdescriptor2 = valdescriptor2[0];
                setupdate(val1,val2,valdescriptor1,valdescriptor2)
                count2 = count2 + 3
                rep_done = 1;
        if(rep_done == 0 ):        
            if(filelist[count2 +0] == 'list'):
            #if no second line to describe what item and val to list then list all
                try:
                    val1 = filelist[count2 +1].split(':');
                    valdescriptor1 = filelist[count2 +1].split(':');
                    val1 = val1[1]
                    valdescriptor1 = valdescriptor1[0];
                except:
                    val1 = 'all';
                    valdescriptor1 = 'all'
                list_item(val1,valdescriptor1)
                count2 = count2 +2 ;
                rep_done = 1;
        if(rep_done == 0):
            if(filelist[count2 +0] == 'sort'):
                valdescriptor1 = filelist[count2 +1].split(':');
                valdescriptor1 = valdescriptor1[0];
                sort(valdescriptor1)
                count2 = count2 +2 ;
                rep_done = 1;
                
def add(ID,desc,foot,quant):
    Parts = {'ItemID':ID,'Desc':desc,'Foot':foot,'Quant':quant};
    ldlist.append(Parts);
    write_back("files/parts");
    print 'add OK'

def remove(field_d,val):
    count = 0;
    ldlist2 = list(ldlist);
    for item in ldlist2:
        if(item[field_d] == val):# means we have a match for the part to have a field updated
            ldlist.pop(count);
        else:
            count = count + 1;
    write_back("files/parts");
    print 'remove OK'    
            
def setupdate(val1,val2,valdescriptor,valdescriptor2):
    for item in ldlist:
        if(item[valdescriptor2] == val2):# means we have a match for the part to have a field updated
            item[valdescriptor] = val1;
    write_back("files/records");
    print 'set OK';      
            
            
def list_item(val1,valdescriptor):
    while len(ldlistsort) > 0 : ldlistsort.pop() #empty the list sent to sort even if it is not being sent for safety
    if(val1 == 'all'):
        for item in ldlist:
            print item;
            ldlistsort.append(item);
    else:
        for item in ldlist:
            if(item[valdescriptor] == val1):# means we have a match for the part to have a field updated
                print item;
                ldlistsort.append(item);
    print'list OK'
                      

def sort(valdescriptor):
    for item in ldlistsort:
        newlist = sorted(ldlistsort, key = lambda k: k[valdescriptor])#sorts in the same form that is saved here
    for item in newlist:
        print item;
    
    print'sort OK'

def write_back(arg1):
    f = open(arg1, 'w');
    for item in ldlist:
        f.write(item["ItemID"]);
        f.write('\n')
        f.write(item["Desc"]);
        f.write('\n')
        f.write(item["Foot"]);
        f.write('\n')
        f.write(item["Quant"]);
        f.write('\n');
        f.write('\n')
    

            
#running of the code-equivalent to main

#accepts proper command line arguments
if(sys.argv[1] == '-f' or sys.argv[1] == '--data-file'):
    create_dic("files/records");
    command_call();        
elif(sys.argv[1] == '-h' or sys.argv[1] == '--help'):
     sys.stdout.write("this program deals with inventory\n");  
else:
    sys.stdout.write("not the correct CLA from standard\n");        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

