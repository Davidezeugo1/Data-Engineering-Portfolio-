# Data Engineering Portfolio

👋 Hi, I'm **David Ezeugo** — a data engineer focused on designing, building, and operating **production-grade datapipeline platforms** that support reliable batch and streaming.

This repository documents both **individual data pipelines** and the **underlying cluster infrastructure** that powers them. The goal is to demonstrate not just how data moves, but **how real-world data systems are designed, operated, and scaled**.

---

## 🧱 Platform Overview: On-Prem Data Engineering Cluster

This portfolio is backed by a **3-node Ubuntu cluster** built without Docker or Kubernetes to prioritize:

* Predictable networking
* Easier debugging
* Production realism
* Native Spark and Kafka performance

The cluster serves as a **shared execution environment** for all current and future pipelines.

### Cluster Architecture

* **Node 1 (Control Plane)**

  * Spark Master
  * Kafka Broker
  * ZooKeeper
  * Airflow Webserver & Scheduler
  * MongoDB
  * MySQL
  * MinIO (S3-compatible object storage)
* **Node 2 & Node 3 (Workers)**

  * Spark Workers
  * Shared storage mounts
  * Streaming and batch execution

### Shared Infrastructure

* **NFS-based shared storage**

  * Spark checkpoints
  * Kafka backups
  * Airflow DAG distribution
  * Data lake storage
* **Static hostname networking**

  * Deterministic service discovery
  * Stable Spark, Kafka, and database connectivity

This platform is designed to **host many pipelines simultaneously**, mirroring real enterprise data environments.

---

## ⚙️ Core Technologies

### Data & Compute

* **Apache Spark (Standalone Cluster)**

  * Batch processing
  * Structured Streaming
  * Spark UI for job inspection
* **Apache Kafka + ZooKeeper**

  * Real-time event streaming
  * Decoupled producers and consumers
* **Apache Airflow**

  * Workflow orchestration
  * Scheduling, retries, dependency management

### Storage

* **MongoDB** – Streaming and operational data source
* **MySQL** – Transactional and analytics sink
* **MinIO (S3-compatible)** – Checkpoints, backups, and data lake storage
* **Parquet** – Columnar analytics format

### Visualization & Observability

* **Airflow UI** – Pipeline orchestration visibility
* **Spark Web UI & History Server** – Job diagnostics and performance analysis
* **Kafka UI** – Topic and consumer monitoring
* **Grafana** – Metrics dashboards (cluster, pipelines, lag)

---

## 📂 Planed Pipelines & Projects 

Each project will run on the shared cluster and follow production-oriented patterns such as idempotency, checkpointing, and orchestration.

| Project              | Description                                     | Stack                                    |
| -------------------- | ----------------------------------------------- | ---------------------------------------- |
| Weather ETL          | Scheduled API ingestion into relational storage | Airflow, Python, MySQL                   |
| NYC Taxi Data Lake   | Batch analytics using Spark and Parquet         | Spark, Parquet, MySQL                    |
| Crypto Streaming     | Real-time ingestion and processing pipeline     | Kafka, Spark Structured Streaming, MySQL |
| Retail Data Platform | Multi-source analytics platform                 | Airflow, Spark, Kafka, MinIO             |

> All pipelines are designed to coexist on the same cluster, demonstrating shared infrastructure usage and operational maturity.

---

## 🔐 Production-Grade Design Principles

My goal for this platform is to emphasize:

* **Reliability**

  * Spark checkpointing
  * Airflow retries and backfills
* **Observability**

  * Persistent Spark UIs
  * Kafka consumer lag monitoring
  * Centralized dashboards
* **Scalability**

  * Horizontal Spark workers
  * Externalized storage
* **Change Management**

  * Version-controlled DAGs and jobs
  * Repeatable deployment patterns

Planned enhancements include TLS security, schema enforcement, and CI/CD automation.

---

## 📊 Dashboards & Monitoring

Live dashboards and service UIs are available here:

* **Airflow UI:** http://192.168.0.100:8085/ 
* **Spark UI / History Server:** http://192.168.0.100:8082/ 
* **Grafana Dashboards:** *(coming soon)*

> Access details and screenshots are documented in each project directory.

---

## 📚 Future Work

* Kafka Schema Registry and data contracts
* Spark History Server hardening
* Prometheus-based alerting
* CI/CD for DAGs and Spark jobs
* Infrastructure automation 

This repository will continue evolving as new pipelines and platform features are added.

---

📫 **Connect**
* Resume: *coming soon*
* Email: Davidezeugo1@gmail.com

Thanks for checking out my work!



