# Realtime Data Streaming | End-to-End Data Engineering Project

## Table of Contents
- [Realtime Data Streaming | End-to-End Data Engineering Project](#realtime-data-streaming--end-to-end-data-engineering-project)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [System Architecture](#system-architecture)
  - [Technologies](#technologies)

## Introduction

This project demonstrates a complete data engineering solution, encompassing data ingestion, processing, and storage. It leverages a robust tech stack including Apache Airflow, Python, Kafka, Zookeeper, Spark, and Cassandra, all containerized for efficient deployment. The whole project is initially introduced by [Yusuf Ganiyu](https://github.com/airscholar) in his [Youtube Video](https://www.youtube.com/watch?v=GqAcTrqKcrY&ab_channel=CodeWithYu).

## System Architecture

![System Architecture](https://github.com/yangforbig/DE-DataStreaming/blob/main/Data%20engineering%20architecture.png)

The project is designed with the following components:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.

## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker
