# Batch Data Pipeline: Airflow → Spark → MongoDB
Overview

This repository documents a successful end-to-end batch data engineering pipeline built on a 3-node Ubuntu cluster without Docker or Kubernetes.

The pipeline demonstrates how data is:

Orchestrated with Apache Airflow

Processed using Apache Spark (batch mode)

Persisted into MongoDB as the final sink

This project serves as the foundation for later streaming pipelines and proves the cluster is production-capable

✅ Key Leason:
** Learned to use the correct connector
** Learned to version control
** Learned to create the coonection for airflow to spark
** Learned to debug spark error


✅ Key Achievements:
** Fully working multi-node Spark cluster

** Airflow successfully triggering Spark jobs

** Reliable data ingestion into MongoDB

* DAG: spark_to_mongo can be found active on the airflow UI ** http://192.168.0.100:8085/home/  

