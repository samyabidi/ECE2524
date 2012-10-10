# ECE 2524 Homework 4 Problem 1 <Samy Abidi> change
import argparse, fileinput, string
from optparse import OptionParser
import sys
import operator
#the list of dictionary structures and the list that holds the action files
ldlist = [];
filelist = [];
print "beginning inventory actions";
#when you are loading into file filelist is zero otherwise it is one
#for reading command line
#print(sys.argv[2]);


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
           Parts = {'ID':line1,'Desc':line2,'Foot':line3,'quant':line4};
           ldlist.append(Parts);
        else:
            count = count + 1;
        
        
    print(ldlist);
    newlist = sorted(ldlist, key=lambda k: k['Foot']);#to access single dic do newlist
#newlist[0]['ID'];
#create_dic("files/parts");
def command_call():#for reading the input command file
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
# for reading action files
    filelist = [];
    for line_input in sys.stdin:
        filelist.append(line_input.replace('\n',''));
#if you are pushing all the information into another file then filelist[0] exists
#but if you are not pushing it into another file then filelist[1] is the first element with data so I creaetd a try statement here to solve the problem.
    try:
        if(filelist[0] == 'add' or filelist[0] == 'remove' or filelist[0] == 'set/update' or filelist[0] == 'list' or filelist[0] == 'sort'):
            arraypos = 0;
    except ValueError:
        arraypos = 1;
    print "this is what array pos equals";
    print arraypos
    if(filelist[0] == 'add'):
        #print 'add';
        #segment the rest of filelist here and call the add function
        tempf = filelist[1].split(':');
        tempd = filelist[2].split(':');
        tempid = filelist[3].split(':');
        tempq = filelist[4].split(':');
        add(tempf[1],tempd[1],tempid[1],tempq[1]);
    if(filelist[0] == 'remove'):
        tempid = filelist[1].split(':');
        remove(tempid[1]);
    if(filelist[0] == 'set/update'):
        val1 = filelist[1].split(':');
        val2 = filelist[2].split(':');
        valdescriptor1 = filelist[1].split(':');
        valdescriptor2 = filelist[2].split(':');
        val1 = val1[1]
        val2 = val2[1]
        valdescriptor1 = valdescriptor1[0];
        valdescriptor2 = valdescriptor2[0];
        print "printing all important vals";
        print val1;
        print val2;
        print valdescriptor1;
        print valdescriptor2;
        setupdate(val1,val2,valdescriptor1,valdescriptor2)
        print 'set';
    if(filelist[0] == 'list'):
        print 'list';
    if(filelist[0] == 'sort'):
        print 'sort';

def add(foot,desc,ID,quant):
    Parts = {'ID':ID,'Desc':desc,'Foot':foot,'quant':quant};
    ldlist.append(Parts);

def remove(ID):
    count = 0;
    for item in ldlist:
        if(item['ID'] == ID):
            ldlist.pop(count);
            count = count -1;
        count = count + 1;
#this needs to be able to search any kind of characteristic of the electronic part     
def setupdate(val1,val2,valdescriptor,valdescriptor2): #ID,Foot, Desc, quant,valdescriptor,valdescriptor2):          
    count = 0;
    Quant = '';
    Foot = '';
    Desc = '';
    ID = '';
    print valdescriptor;
    print valdescriptor2;
    if(valdescriptor == "itemID"):
        valdescriptor = 4 
        ID = val1;
    if(valdescriptor == "Descriptor"):
        valdescriptor = 1
        Desc = val1
    if(valdescriptor == "Footprint"):
        valdescriptor = 2
        Foot = val1
    if(valdescriptor == "Quantity"):
        valdescriptor = 3
        Quant = val1;
    if(valdescriptor2 == "itemID"):
        valdescriptor2 = 4
        ID = val2 
    if(valdescriptor2 == "Descriptor"):
        valdescriptor2 = 1
        Desc = val2
    if(valdescriptor2 == "Footprint"):
        valdescriptor2 = 2
        Foot = val2
    if(valdescriptor2 == "Quantity"):
        valdescriptor2 = 3
        Quant = val2
    print "before entering loop";
    print val1;
    print val2;
    print valdescriptor;
    print valdescriptor2;
    print Quant;
    print Foot;
    print Desc;
    print ID;
    for item in ldlist:
        print item['ID'];
        if(item['ID'] == ID):#item[valdescriptor2] == val2 ?
            print "IN HERE DDDDDDDDD";
            if(valdescriptor == 1):
                ldlist[count]['Desc'] = Desc;
            if(valdescriptor == 2):
                ldlist[count]['Foot'] = Foot;
            if(valdescriptor == 3):
                print "in HEREREEE";
                ldlist[count]['quant'] = Quant;
            if(valdescriptor == 4):
                ldlist[count]['ID'] = ID;
        if(item['Desc'] == Desc and valdescriptor2 != 1 ):
            if(valdescriptor == 1):
                ldlist[count]['Desc'] = Desc;
            if(valdescriptor == 2):
                ldlist[count]['Foot'] = Foot;
            if(valdescriptor == 3):
                ldlist[count]['quant'] = Quant;
            if(valdescriptor == 4):
                ldlist[count]['ID'] = ID;
        if(item['Foot'] == Foot and valdescriptor2 != 2 ):
            if(valdescriptor == 1):
                ldlist[count]['Desc'] = Desc;
            if(valdescriptor == 2):
                ldlist[count]['Foot'] = Foot;
            if(valdescriptor == 3):
                ldlist[count]['quant'] = Quant;
            if(valdescriptor == 4):
                ldlist[count]['ID'] = ID;
        if(item['quant'] == Quant and valdescriptor2 != 3 ):
            if(valdescriptor == 1):
                ldlist[count]['Desc'] = Desc;
            if(valdescriptor == 2):
                ldlist[count]['Foot'] = Foot;
            if(valdescriptor == 3):
                ldlist[count]['quant'] = Quant;
            if(valdescriptor == 4):
                ldlist[count]['ID'] = ID;
        count = count + 1;   

    
def list(ID,Foot, Desc, quant,valdescriptor):          
    count = 0;
    for item in ldlist:
        if(item['ID'] == ID and valdescriptor2 != 4 ):
            print item;
        if(item['Desc'] == Desc and valdescriptor2 != 1 ):
            print item;
        if(item['Foot'] == Foot and valdescriptor2 != 2 ):
            print item;
        if(item['quant'] == quant and valdescriptor2 != 3 ):
            print item;
        count = count + 1;   
        
def sort(ID,Foot, Desc, quant,valdescriptor):          
    count = 0;
    for item in ldlist:
        if(valdescriptor2 != 4 ):
            newlist = sorted(ldlist, key=lambda k: k['ID']);
        if(valdescriptor2 != 1 ):
            newlist = sorted(ldlist, key=lambda k: k['Desc']);
        if(valdescriptor2 != 2 ):
            newlist = sorted(ldlist, key=lambda k: k['Foot']);
        if(valdescriptor2 != 3 ):
            newlist = sorted(ldlist, key=lambda k: k['quant']);
        count = count + 1;  



#################beginning actual calls

create_dic("files/parts");
command_call();
print(ldlist);









   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

