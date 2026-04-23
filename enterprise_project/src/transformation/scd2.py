from pyspark.sql.functions import lit, current_timestamp

def apply_scd2(df):
    return df.withColumn("is_current", lit(True)) \
             .withColumn("start_date", current_timestamp()) \
             .withColumn("end_date", lit(None))