#!/usr/bin/env python
import sys
for line in sys.stdin:
    line       = line.strip()   # strip out carriage return
    key_value  = line.split(",")   # split line, into key and value, returns a list
    key_in     = key_value[0]# key is first item in list
    value_in   = key_value[1].strip()   # value is 2nd item and 
                                        # it's important to strip away empty space, 
                                        # otherwise it might have problem recognizing digit in string object.
    if value_in == 'ABC' or value_in.isdigit(): # only select ABC channel and viewer counts that include both ABC channel and not. 
        print( '{0}\t{1}'.format(key_in, value_in) )  #print a string tab and string
    
#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
