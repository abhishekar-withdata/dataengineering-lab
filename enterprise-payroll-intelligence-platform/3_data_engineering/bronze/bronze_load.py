from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BronzeLoad").getOrCreate()

# Load raw payroll data
payroll_df = spark.read.option("header", True).csv("/data/raw/payroll.csv")

# Write to bronze layer
payroll_df.write.format("delta").mode("overwrite").save("/lakehouse/bronze/payroll")

print("Bronze layer loaded successfully")
