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

In pyspark-shell environment,

show_views_file = sc.textFile('input_join2/join2_gennum?.txt')
def split_show_views(line):
    line  = line.strip().split(',')
    show = line[0]
    views = int(line[1])
    return (show,views)
show_views = show_views_file.map(split_show_views)
show_views.take(2)
show_channel_file  = sc.textFile('input_join2/join2_genchan?.txt')
show_channel_file.take(2)
def split_show_channel(line):
    line = line.strip().split(',')
    show = line[0]
    channel = line[1]
    return (show,channel)
show_channel = show_channel_file.map(split_show_channel)
show_channel.take(2)
joined_dataset = show_views.join(show_channel)
joined_dataset.take(2)
def extract_channel_views(show_views_channel):
    show,view_channel = show_views_channel
    views,channel = view_channel
    return (channel,views)
channel_views = joined_dataset.map(extract_channel_views)
channel_views.take(2)
def some_function(a,b):
    return a+b
channel_views.reduceByKey(some_function).collect()

