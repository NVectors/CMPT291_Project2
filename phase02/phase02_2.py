# Phase 02
# Create four indexes

import re
#import idx2numpy # A Python package which provides tools to convert files to and from IDX format
#from bplustree import BPlusTree # An on-disk B+tree for Python 3

#from bsddb3 import db

# 01: A hash index on recs.txt with row ids as keys and the full email record as data

# Email record consist of everything after the colon to the right of the row id
# This file includes one line for each email in the form of I:rec where I is 
# the row id and rec is the full email record

# input file: "recs.txt"
# index name: "re.idx"
def part_01():
    recs = open('recs.txt', 'r')    
    hi = {} # create hash index dictionary

    
    while True:
        try:
            line = recs.readline() # line is type str
            x = re.split(":<mail>", line, 1)
            key = x[0]
            x = re.split(key+':', line, 1)
            value = x[1] # values == data
            value = value.replace('\n', '')
            #print(key, value) # test
            hi[key] = value
        except:
            break
    
    recs.close()
    
    test = open("1recs.txt", 'w')
    
    for x in hi.keys():
        test.write(x)
        test.write("\n")
        test.write(hi[x])
        test.write("\n")
        
    
    test.close()

    
    
    #print(hi) # test
    
    

    

# 02: A B+-tree index on terms.txt with terms as keys and row ids as data
# input file: "terms.txt"
# index name: " te.idx"
def part_02():
    terms = open('terms.txt', 'r')  
    btd = {} # create b tree dictionary

    
    while True:
        try:
            line = terms.readline() # line is type str
            x = re.split(":", line, 1)
            key = x[0]
            x = re.split(key+':', line, 1)
            value = x[1] # values == data
            value = value.replace('\n', '')
            #print(key, value) # test
            btd[key] = value
        except:
            break    
    
    
    #print(btd) # test
    
    terms.close()
    
    test = open("1terms.txt", 'w')
    
    for x in btd.keys():
        test.write(x)
        test.write("\n")
        test.write(btd[x])
        test.write("\n")
        
    
    test.close()    
    

# 03: A B+-tree index on emails.txt with emails as keys and row ids as data
# input file: "emails.txt"
# index name: "em.idx"
def part_03():
    emails = open('emails.txt', 'r')
    btd = {} # create b tree dictionary

    
    while True:
        try:
            line = emails.readline() # line is type str
            x = re.split(":", line, 1)
            key = x[0]
            x = re.split(key+':', line, 1)
            value = x[1] # values == data
            value = value.replace('\n', '')
            #print(key, value) # test
            btd[key] = value
        except:
            break    
    
    
    #print(btd) # test 
    #print(len(btd))

    emails.close()
    
    test = open("1emails.txt", 'w')
    
    for x in btd.keys():
        test.write(x)
        test.write("\n")
        test.write(btd[x])
        test.write("\n")
        
    
    test.close()       
    

# 04: A  B+-tree index on dates.txt with dates as keys and row ids as data
# input file: "dates.txt"
# index name: "da.idx"
def part_04():
    dates = open('dates.txt', 'r')
    btd = {} # create b tree dictionary

    
    while True:
        try:
            line = dates.readline() # line is type str
            x = re.split(":", line, 1)
            key = x[0]
            x = re.split(key+':', line, 1)
            value = x[1] # values == data
            value = value.replace('\n', '')
            #print(key, value) # test
            btd[key] = value
        except:
            break    
    
    
    #print(btd) # test 
    #print(len(btd))
    
    dates.close() 
    
    
    
    test = open("1dates.txt", 'w')
    
    for x in btd.keys():
        test.write(x)
        test.write("\n")
        test.write(btd[x])
        test.write("\n")
        
    
    test.close()       
    

def main():
    part_01()
    part_02()
    part_03()
    part_04()
    
    
if __name__ == "__main__":
    main()