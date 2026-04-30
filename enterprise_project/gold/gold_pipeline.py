from gold.fact.fact_transactions import build_fact_transactions
from gold.dimension.dim_customer_scd2 import apply_scd2
from gold.aggregates.agg_daily_transactions import build_daily_agg


def run_gold_pipeline(spark, silver_df, base_path):

    # Build fact
    fact_df = build_fact_transactions(silver_df)

    # Write fact
    fact_df.write.format("delta").mode("append").save(f"{base_path}/fact_transactions")

    # Apply SCD2 for customer
    apply_scd2(spark, silver_df, f"{base_path}/dim_customer")

    # Aggregations
    agg_df = build_daily_agg(fact_df)
    agg_df.write.format("delta").mode("append").save(f"{base_path}/agg_daily_transactions")
