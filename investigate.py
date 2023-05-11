import pyspark
import os
import sys
from pyspark.sql import SparkSession
import pyspark.sql.functions as func
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS
from pyspark.mllib.evaluation import RankingMetrics
from pyspark.sql.functions import col, expr

def main(spark, userID, file_size):
    
    #------------------------Load the track, train, val from Parquet files------------------------
    
    print('\nLoading data...\n')
    
    if file_size == 'small':

        train = spark.read.parquet(f'hdfs:/user/{userID}/recommender_train_small')
        val = spark.read.parquet(f'hdfs:/user/{userID}/recommender_val_small')
    
    elif file_size == 'full':

        train = spark.read.parquet(f'hdfs:/user/{userID}/recommender_train')
        val = spark.read.parquet(f'hdfs:/user/{userID}/recommender_val')
    
    # Print the number of rows in each dataframe
    print('\nfor train: \n')
    print(train.groupby('recording_msid').count().count())
    print('\nfor val: \n')
    print(val.groupby('user_id').count().count())

    # Join train and val using user_id and recording_msid
    train_val = train.join(val, on=['user_id','recording_msid'], how='inner')
    print(train_val.count())

    # Evaluate on user_id = 27
    train.filter(train.user_id == 27).sort('count', ascending=False).show()
    val.filter(val.user_id == 27).sort('count', ascending=False).show()

    # Print train and validation sizes for user_id = 27
    print(train.filter(train.user_id == 27).count())
    print(val.filter(val.user_id == 27).count())

if __name__ == "__main__":
    
    # Create the spark session object
    spark = SparkSession.builder.appName('ALS').config("spark.sql.broadcastTimeout", "36000").getOrCreate()

    # Get user netID from the command line
    userID = os.environ['USER'] 

    file_size = sys.argv[1]

    # Call our main routine
    main(spark,userID,file_size)
