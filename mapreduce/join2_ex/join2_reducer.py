#!/usr/bin/env python
import sys
line_cnt = 0
abc_found = False
total_viewers = 0
prev_word          = "  "                #initialize previous word  to blank string
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt += 1
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
    if curr_word != prev_word:
        if line_cnt > 1:
            if abc_found:
                print('{0}\t{1}'.format(prev_word,total_viewers))
                abc_found = False
        # this part is not yet clean code, but it works for the test purpose.
        if value_in == 'ABC':
            prev_word = curr_word
            abc_found = True
        else:
            prev_word = curr_word  
            total_viewers = int(value_in)
    else:
        if value_in.isdigit():
            prev_word = curr_word
            total_viewers += int(value_in)
        elif value_in == 'ABC':
            prev_word = curr_word
            abc_found = True
        else:
            print "neither viewer number is found nor ABC channel is found! Perhaps data needs cleaning before Map/Reduce."
            exit(1)
if value_in == 'ABC':
    print('{0}\t{1}'.format(curr_word,total_viewers))
