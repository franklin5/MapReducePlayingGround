In this example, I am going to use spark to reproduce results achieved by using MapReduce join1 example.

To enter pyspark shell ipython environment, 
> PYSPARK_DRIVER_PYTHON=ipython pyspark

fileA = sc.textFile("input/join1_FileA.txt") # where input dir is within hadoop filesystem
fileB = sc.textFile("input/join1_FileB.txt")

def split_fileA(line):
    line = line.strip().split(',')
    word = line[0]
    count = int(line[1])
    return (word,count)

def split_fileB(line):
    line = line.strip().split(',')
    date_word = line[0]
    count_string = line[1]
    date_word  = date_word.split()
    date = date_word[0]
    word = date_word[1]
    return (word, date+" "+count_string)

fileA_data = fileA.map(split_fileA)
fileB_data = fileB.map(split_fileB)

Run join

The goal is to join the two datasets using the words as keys and print for each word the wordcount for a specific date and then the total output from A.

Basically for each word in fileB, we would like to print the date and count from fileB but also the total count from fileA.

Spark implements the join transformation that given a RDD of (K, V) pairs to be joined with another RDD of (K, W) pairs, returns a dataset that contains (K, (V, W)) pairs.

> fileB_joined_fileA = fileB_data.join(fileA_data)
> fileB_joined_fileA.collect()
