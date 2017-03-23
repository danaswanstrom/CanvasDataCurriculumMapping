### Code for PySpark on DataProc
from pyspark.sql import SparkSession
# Might not need this
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType, TimestampType, LongType
from pyspark.sql.functions import *
import os
import csv
import itertools
file_source = "gs://canvas-data-txt-ecasd/canvasdata/"


canvas_data_txts = ['wiki_page_fact.txt', 'wiki_page_dim.txt']

canvas_spark_df_dictionary = {file_name.replace(".txt","_df"):
                             spark.read.csv(file_source + file_name, 
                                            inferSchema=True, 
                                            sep = "\t", 
                                            nullValue='\\N', 
                                            header=True) 
                              for file_name in canvas_data_txts}

wiki_pg_fact = canvas_spark_df_dictionary['wiki_page_fact_df']
wiki_pg_dim = canvas_spark_df_dictionary['wiki_page_dim_df']

standards = ['5.NBT.1', '5.NBT.3', '5.NBT.3', '5.NBT.3a', '5.NBT.3b', '5.NBT.4', '5.NBT.7']
standards_dic_with_url = {standard:
                         [row.url for row in 
                          wiki_pg_dim[wiki_pg_dim['body']
                                      .like('%' + standard + '%')].select('url').collect()]
                         for standard in standards}

keys = sorted(standards_dic_with_url.keys())
with open("stand_url.csv", "w") as outfile:
   writer = csv.writer(outfile, delimiter = ",")
   writer.writerow(keys)
   # Note the izip_longest because pyspark is 2.7
   writer.writerows(itertools.izip_longest(*[standards_dic_with_url[key] for key in keys]))

#Exit pyspark and run gsutil cp stand_url.csv gs://canvas-data-txt-ecasd/canvasdata/
