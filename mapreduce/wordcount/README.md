In this wordcount example, we can write our own mapper and reducer python code and supply them to hadoop streaming pipline. Here is how:

1. Create some data:
> echo "A long time ago in a galaxy far far away" > testfile1

> echo "Another episode of Star Wars" > testfile2

2. Create input dir and copy local files to the HDFS filesystem:
> hadoop fs -mkdir wordcount_input

> hadoop fs -copyFromLocal testfile* wordcount_input

3. Run unix pipline to check if mapper and reducer are working properly in serial computation:
> cat testfile* | ./wordcount_mapper.py | sort | ./wordcount_reducer.py  

4. Run hadoop wordcount example with the input, output, mapper, and reducer specified:
> hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input wordcount_input -output wordcount_output -mapper /home/cloudera/Downloads/wordcount/wordcount_mapper.py -reducer /home/cloudera/Downloads/wordcount/wordcount_reducer.py
-- Notes: 1) wordcount_output has to be a new dir within hdfs: if existing dir is found, the program aborts, because hadoop does not indend to overwrite data; 2) mapper and reducer python scripts have to be specified with absolute path; 3) ./wordcount_mapper.py and ./wordcount_reducer.py has to be given all rights to all users, namely 'chmod a+x' to these two files, and I have found 'chmod u+x' does not work properly; 4) --help tells us more options to run hadoop streaming: for instance, -NumReduceTasks can be specified. 0 is equivalent to no reducer and only mapper is performed, we can use 'hdfs dfs -getmerge' to gather the part files into one single local file; 1 reduce tak gives globally sorted ordering, while 2 or higher does not have this global order. 