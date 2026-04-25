from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Streaming").getOrCreate()

# Simulated stream input
stream_df = spark.readStream.schema("employee_id INT, event_time STRING, status STRING") \
    .json("/data/stream/attendance")

# Simple anomaly detection (late flag)
anomaly_df = stream_df.filter(col("status") == "late")

query = anomaly_df.writeStream.format("console").start()
query.awaitTermination()
