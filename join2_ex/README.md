In this example, we first generate  <TV show, count> (A TV show title and the number of viewers) txt files, and <TV show title, channel> (A TV show title and the channel it was on) txt files, and answer the question of "What is the total number of viewers for shows on ABC?". Note that, The show-to-channel relationship is Many-to-Many. In other words, each show might appear on many channels, and each channel might broadcast many shows.

In pseudo-SQL it might be something like:

select sum( viewer count) from File A, File B where FileA.TV show = FileB.TV show and FileB.Channel='ABC' grouped by TV show

1. First generate some datasets using the scripts (see the Code and Text Files section at the bottom) as follows:
> sh make_data_join2.txt
(this is a script that produces 6 files:

python make_join2data.py y 1000 13 > join2_gennumA.txt

python make_join2data.py y 2000 17 > join2_gennumB.txt

…)

2. Use HDFS commands to copy the 6 files created in step 1 into one HDFS directory, just like step 2 in Part 1 and in the wordcount assignment.

Note: These datasets are pseudo-randomly generated so the output is the same for any environment. The files are not large, however they are big enough that it would be time consuming to solving the assignment by hand. One could put the data in a database but that would defeat the purpose of the assignment!

3. The datasets generated in step 1 contain the following information:

join2_gennum*.txt consist of <TV show, count> (A TV show title and the number of viewers)

Example join2_gennum*.txt:

Almost_News, 25
Hourly_Show,30
Hot_Cooking,7
Almost_News, 35
Postmodern_Family,8
Baked_News,15
Dumb_Games,60
…
join2_genchan*.txt consists of <TV show title, channel> (A TV show title and the channel it was on)

Example join2_genchan*.txt:

Almost_News, ABC
Hourly_Show, COM
Hot_Cooking, FNT
Postmodern_Family, NBC
Baked_News, FNT
Dumb_Games, ABC
…

Data Notes:

TV show titles do not have spaces
Channels have 3 letters
TV show titles can appear multiple times, with different counts
A TV show and channel combination might appear multiple times
TV shows could appear on multiple channels
The output should have no commas or punctuation, only 1 space between the TV show title and number

Hint 1: The new join mapper is like the join1 mapper but instead of stripping dates from the key field it should be selecting rows related to 'ABC'.

In Python strings are character arrays. Strings can be declared and accessed as follows:

my_string = 'LMNOP'
my_string[0:3]='LMN'
In Python the string function to check if a string is just digits is as follows:

my_string.isdigit() # will return True or False.
Hint 2: The new join reducer is like the join1_reducer but instead of building up a list of dates & counts, it should be summing viewer counts to keep a running total. Make sure you understand what will be in the intermediate output files that become reducer input (after the mapper and after Hadoop shuffle & group). Look carefully at the groups that are present in the reducer input to see what conditions your reducer will have to check for. You can test the mapper output using the Unix piping mentioned in Part 1.

Hint 3: This new join task has some overlap with wordcounting task. Use the wordcount code to review the counting and updating logic, as well as functions that handle strings and integers.

Hint 4: Here is a possible pseudo code example of how to implement this join using tv-show as the key:

join2_mapper:

read lines, and split lines into key & value

if value is ABC or if value is a digit print it out

Note: you can test just the mapper by running something like:

> cat join2_gen*.txt | ./join2_mapper.py | sort
Also, if we did have huge files partitioned across a cluster you might have information about viewer counts in one partition and information about which show is on ABC in another partition. The mapper and the Hadoop shuffle will bring those bits of information together to the same reducer if a key is a show.

join2_reducer:

read lines and split lines into key & value

if a key has changed (and it's not the first input)

then check if ABC had been found and print out key and running total,

if value is ABC then set some variable to mark that ABC was found (like abc_found = True)

otherwise keep a running total of viewer counts

Hint 5:

The first two lines of your output should be:

Almost_Games 49237
Almost_News 46592
