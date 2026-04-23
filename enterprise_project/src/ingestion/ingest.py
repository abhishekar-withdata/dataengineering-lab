from pyspark.sql import SparkSession

def ingest():
    spark = SparkSession.builder.appName("Ingestion").getOrCreate()
    df = spark.read.option("header", True).csv("data/raw/orders.csv")
    df.write.mode("overwrite").parquet("data/bronze/orders")
    print("Ingestion done")