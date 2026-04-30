from pyspark.sql.functions import col, current_date, lit
from delta.tables import DeltaTable

def apply_scd2(spark, source_df, target_path):
    source_df = source_df.withColumn("effective_date", current_date()) \
        .withColumn("end_date", lit(None).cast("date")) \
        .withColumn("is_current", lit(True))

    if DeltaTable.isDeltaTable(spark, target_path):
        target = DeltaTable.forPath(spark, target_path)

        target.alias("t").merge(
            source_df.alias("s"),
            "t.customer_id = s.customer_id AND t.is_current = true"
        ).whenMatchedUpdate(
            condition="t.name <> s.name OR t.city <> s.city",
            set={"end_date": "current_date()", "is_current": "false"}
        ).whenNotMatchedInsertAll().execute()
    else:
        source_df.write.format("delta").save(target_path)
