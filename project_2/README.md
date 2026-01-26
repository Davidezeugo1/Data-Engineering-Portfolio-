# Simple_streaming_pipeline
An in-progress pipeline, but a functional real-time streaming pipeline.
The pipeline captures MongoDB Change Streams, publishes them to Kafka, processes them with Spark Structured Streaming, and persists the results into MySQL.
This project represents the transition from batch processing to event-driven architecture.

# Pipeline Flow
* MongoDB Source Connector
  * Uses MongoDB Kafka Connector
  * Streams insert/update/replace events
  * Publishes JSON change events to Kafka

* Kafka
  * Acts as a durable event buffer
  * Topics validated via AKHQ
  * Ensures replayability and fault tolerance

* Spark Structured Streaming
 * Reads Kafka topic
 * Parses MongoDB change events
 * Filters relevant operation types
 * Extracts fullDocument
 * Converts timestamps

* MySQL Sink
  * Written using foreachBatch
  * Ensures idempotent batch writes
  * Supports schema evolution
