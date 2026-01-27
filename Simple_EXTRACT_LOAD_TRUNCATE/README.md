# Simple ETL & Database Synchronization Pipeline
This project serves as an end-to-end data pipeline involving extraction, transformation, and automated cleanup. It was developed to apply core data engineering principles—specifically handling multi-database environments and containerized workflows.

# Pipeline Architecture & Workflow
* The pipeline is divided into three distinct functional modules, orchestrated within a Docker environment:
  
[Data Ingestion (CSV to MySQL)](https://github.com/Davidezeugo1/Data-Engineering-Portfolio-/blob/50957f870f58393bda0b4ca0a9167ed796aa42bc/Simple_EXTRACT_LOAD_TRUNCATE/loadsqldb.py): Leverages Pandas and SQLAlchemy to parse raw CSV data and perform the initial load into a MySQL staging environment. This stage focuses on schema mapping and establishing the primary data source.

[Cross-Database Transformation & Load](https://github.com/Davidezeugo1/Data-Engineering-Portfolio-/blob/50957f870f58393bda0b4ca0a9167ed796aa42bc/Simple_EXTRACT_LOAD_TRUNCATE/loadtopost.py): Acts as the transformation layer. The script extracts data from MySQL, performs a SQL JOIN operation to enrich the dataset with a new calculated column, and loads the refined data into a PostgreSQL production-ready instance.

[Verification & Automated Cleanup (Truncation)](https://github.com/Davidezeugo1/Data-Engineering-Portfolio-/blob/50957f870f58393bda0b4ca0a9167ed796aa42bc/Simple_EXTRACT_LOAD_TRUNCATE/truncate.py): Ensures data integrity by running validation queries post-load. Once the transfer is verified, the script automatically truncates the tables in both MySQL and PostgreSQL to reset the environment, simulating a temporary staging workflow.

* Deployment & Containerization:
  
[Dockerfile Configuration](https://github.com/Davidezeugo1/Data-Engineering-Portfolio-/blob/50957f870f58393bda0b4ca0a9167ed796aa42bc/Simple_EXTRACT_LOAD_TRUNCATE/dockerfile): The entire application is containerized using Docker. This ensures environment consistency, simplifies dependency management, and allows the pipeline to be executed seamlessly across any infrastructure.
