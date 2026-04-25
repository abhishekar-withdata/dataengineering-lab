from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("AttritionModel").getOrCreate()

# Load data
_df = spark.read.format("delta").load("/lakehouse/gold/employee_features")

# Feature columns
features = ["salary", "overtime_hours", "years_at_company"]
assembler = VectorAssembler(inputCols=features, outputCol="features")

_df = assembler.transform(_df)

# Train model
lr = LogisticRegression(featuresCol="features", labelCol="attrition")
model = lr.fit(_df)

print("Model trained successfully")
