# ECE 2524 Homework 4 Problem 1.1 <Samy Abidi> change
import argparse, fileinput, string
from optparse import OptionParser
import sys
import operator
#the list of dictionary structures
ldlist = [];
ldlist2 = [];
#the list of lines inside the action file
filelist = [];
print "beginning inventory actions";
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
    if(filelist[0] == 'add'):
        #segment the rest of filelist here and call the add function
        tempid = filelist[1].split(':');
        tempd = filelist[2].split(':');
        tempf = filelist[3].split(':');
        tempq = filelist[4].split(':');
        add(tempid[1],tempd[1],tempf[1],tempq[1]);
    if(filelist[0] == 'remove'):
        tempid = filelist[1].split(':');
        remove(tempid[0],tempid[1]);
    if(filelist[0] == 'set/update'):
        val1 = filelist[1].split(':');
        val2 = filelist[2].split(':');
        valdescriptor1 = filelist[1].split(':');
        valdescriptor2 = filelist[2].split(':');
        val1 = val1[1]
        val2 = val2[1]
        valdescriptor1 = valdescriptor1[0];
        valdescriptor2 = valdescriptor2[0];
        setupdate(val1,val2,valdescriptor1,valdescriptor2)
        print 'set';
    if(filelist[0] == 'list'):
        try:
            val1 = filelist[1].split(':');
            valdescriptor1 = filelist[1].split(':');
            val1 = val1[1]
            valdescriptor1 = valdescriptor1[0];
        except:
            val1 = 'all';
            valdescriptor1 = 'all'
        list_item(val1,valdescriptor1)
        print 'list';
    if(filelist[0] == 'sort'):
        valdescriptor1 = filelist[1].split(':');
        valdescriptor1 = valdescriptor1[0];
        sort(valdescriptor1)
        
        print 'sort';
def add(ID,desc,foot,quant):
    Parts = {'ItemID':ID,'Desc':desc,'Foot':foot,'Quant':quant};
    ldlist.append(Parts);

def remove(field_d,val):
    count = 0;
    ldlist2 = list(ldlist);
    for item in ldlist2:
        if(item[field_d] == val):# means we have a match for the part to have a field updated
            ldlist.pop(count);
        else:
            count = count + 1;
        
            
def setupdate(val1,val2,valdescriptor,valdescriptor2):
    for item in ldlist:
        if(item[valdescriptor2] == val2):# means we have a match for the part to have a field updated
            item[valdescriptor] = val1;      
            
            
def list_item(val1,valdescriptor):
    if(val1 == 'all'):
        print ldlist;
    else:
        for item in ldlist:
            if(item[valdescriptor] == val1):# means we have a match for the part to have a field updated
                print item;      

def sort(valdescriptor):
    for item in ldlist:
        newlist = sorted(ldlist, key = lambda k: k[valdescriptor])
    print newlist;



            
#running of the code-equivalent to main

create_dic("files/parts");
command_call();
print (ldlist);        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

