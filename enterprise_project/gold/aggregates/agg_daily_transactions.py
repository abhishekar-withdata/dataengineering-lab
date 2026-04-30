from pyspark.sql.functions import sum, count, to_date

def build_daily_agg(df):
    return df.withColumn("txn_date", to_date("transaction_timestamp")) \
        .groupBy("txn_date") \
        .agg(
            count("*").alias("total_transactions"),
            sum("amount").alias("total_amount")
        )
