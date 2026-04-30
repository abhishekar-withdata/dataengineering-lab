from pyspark.sql.functions import col

def build_fact_transactions(df):
    return df.select(
        col("transaction_id"),
        col("customer_id"),
        col("account_id"),
        col("amount"),
        col("transaction_type"),
        col("transaction_timestamp")
    )
