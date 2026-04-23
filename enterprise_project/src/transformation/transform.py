from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

def transform():
    spark = SparkSession.builder.appName("Transform").getOrCreate()
    df = spark.read.parquet("data/bronze/orders")
    df_clean = df.dropDuplicates().dropna()
    df_agg = df_clean.groupBy("customer_id").agg(sum("amount").alias("total_spent"))
    df_agg.write.mode("overwrite").parquet("data/silver/customer_sales")
    print("Transformation done")