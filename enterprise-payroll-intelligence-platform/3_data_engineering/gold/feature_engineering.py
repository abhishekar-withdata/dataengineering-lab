from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()

# Load silver data
df = spark.read.format("delta").load("/lakehouse/silver/payroll")

# Create ML features
features_df = df.withColumn("overtime_ratio", col("overtime_hours")/col("salary")) \
                .withColumn("high_earner", (col("salary") > 100000).cast("int"))

features_df.write.format("delta").mode("overwrite").save("/lakehouse/gold/employee_features")

print("Feature engineering complete")