import pyspark
import pandas as pd
from google.cloud import storage
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

#get list of files
directory = "gs://coins_data_raw"
files = spark.sparkContext.wholeTextFiles(directory).keys().collect()

#take recent one
recent_path = files[-1]
test_json_df = spark.read.json(recent_path)

#explode JSON to columns
exploded_df = test_json_df.withColumn("timestamp", F.from_unixtime(test_json_df["timestamp"]/1000)).select(F.explode("data").alias("data"), "timestamp")

modified_df = exploded_df.selectExpr("data.id", "data.name", "timestamp", "data.changePercent24Hr", "data.explorer", "data.symbol", "data.priceUsd", "data.maxSupply", "data.rank", "data.volumeUsd24Hr", "data.vwap24Hr")

#casting to double
final_df = modified_df\
    .withColumn("priceUsd", modified_df["priceUsd"].cast("double"))\
        .withColumn("volumeUsd24Hr", modified_df["volumeUsd24Hr"].cast("double"))\
            .withColumn("changePercent24Hr", modified_df["changePercent24Hr"].cast("double"))\
                .withColumn("maxSupply", modified_df["maxSupply"].cast("double"))\
                    .withColumn("vwap24Hr", modified_df["vwap24Hr"].cast("double"))

#convert pyspark df to pandas df
pandas_final_df = final_df.toPandas()

# Convert the DataFrame to a CSV string
csv_string = pandas_final_df.to_csv(index=False)

#upload to google cloud storage
client = storage.Client("jawa-378700")
bucket_name = "coins_data_gold"
bucket = client.get_bucket(bucket_name)
blob = bucket.blob("coins.csv")
blob.upload_from_string(csv_string, content_type='text/csv')


