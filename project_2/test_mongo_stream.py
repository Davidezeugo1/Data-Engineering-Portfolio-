## First test to make sure the Kafka topic would be reached and verify that the transformation was correct on handling the JSON object and strings.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("MongoKafkaDebug") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# =========================
# Schemas
# =========================

mongo_envelope_schema = StructType([
    StructField("operationType", StringType()),
    StructField("fullDocument", StringType()),  # IMPORTANT: string
])

full_document_schema = StructType([
    StructField("_id", IntegerType()),
    StructField("fname", StringType()),
    StructField("lname", StringType()),
    StructField("brithday", StringType()),
    StructField("created_at", StructType([
        StructField("$date", LongType())
    ]))
])

# =========================
# Kafka Source
# =========================

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "192.168.0.100:9092") \
    .option("subscribe", "mongo.stream.profile") \
    .option("startingOffsets", "earliest") \
    .load()

json_df = kafka_df.selectExpr("CAST(value AS STRING) as raw_json")

# =========================
# Debug foreachBatch
# =========================

def debug_batch(df, batch_id):
    print(f"\n\n================ BATCH {batch_id} =================")

    print("\n--- RAW KAFKA VALUE ---")
    df.select("raw_json").show(truncate=False)

    envelope_df = df.select(
        from_json(col("raw_json"), mongo_envelope_schema).alias("env")
    )

    print("\n--- PARSED ENVELOPE ---")
    envelope_df.select("env").show(truncate=False)

    filtered_df = envelope_df.filter(
        col("env.operationType") == "insert"
    )

    print("\n--- AFTER FILTER (insert) ---")
    filtered_df.select("env").show(truncate=False)

    full_doc_df = filtered_df.select(
        from_json(col("env.fullDocument"), full_document_schema).alias("doc")
    )

    print("\n--- PARSED fullDocument ---")
    full_doc_df.select("doc").show(truncate=False)

    final_df = full_doc_df.select(
        col("doc._id"),
        col("doc.fname"),
        col("doc.lname"),
        col("doc.brithday"),
        (col("doc.created_at.$date") / 1000)
            .cast("timestamp")
            .alias("created_at")
    )

    print("\n--- FINAL FLATTENED OUTPUT ---")
    final_df.show(truncate=False)

# =========================
# Start Stream
# =========================

query = json_df.writeStream \
    .foreachBatch(debug_batch) \
    .start()

query.awaitTermination()
