from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SilverCleaning").getOrCreate()

# Read from bronze
bronze_df = spark.read.format("delta").load("/lakehouse/bronze/payroll")

# Clean data
clean_df = bronze_df.dropDuplicates(["employee_id"]) \
    .filter(col("salary").isNotNull())

# Write to silver
clean_df.write.format("delta").mode("overwrite").save("/lakehouse/silver/payroll")

print("Silver layer created")
