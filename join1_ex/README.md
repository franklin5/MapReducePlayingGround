In this example, we would like to create a pivot-table using join1_FileA.txt and join1_FileB.txt by keyword of nouns and relate date info. 

1. Check if Unix piping works using the two python modules, 
> cat join1_File*.txt | ./join1_mapper.py | sort | ./join1_reducer.py

2. Running Hadoop streaming command:
 > hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   -input /user/cloudera/input \
   -output /user/cloudera/output_join \   
   -mapper /home/cloudera/join1_mapper.py \   
   -reducer /home/cloudera/join1_reducer.py