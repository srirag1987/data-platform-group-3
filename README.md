
# Data Platform Setup and Usage

This repository contains the setup for a data platform that includes Apache Spark, Apache Kafka, and Iceberg, among other components. Follow the instructions below to get the platform up and running.

## Prerequisites

- **Docker:** Install Docker by following the instructions [here](https://docs.docker.com/engine/install/).
- **Visual Studio Code:** Download and install Visual Studio Code from [here](https://code.visualstudio.com/).

## Setup

1. **Download the `data_platform-group-3` folder.**
2. **Open a terminal inside the folder:**
   - Right-click inside the folder in your file explorer.
   - Select "Open in Terminal" (or the equivalent option for your operating system).

3. **Start the data platform services:**
   - In the terminal, run the following command:

     ```bash
     docker-compose up -d
     ```

   This command starts all the necessary containers in the background (detached mode).

## Explanation of Services

The `docker-compose.yml` file defines several services that work together:

- **pyspark-jupyter:** Jupyter Notebook environment with Apache Spark for data processing.
- **ed-zookeeper:** Zookeeper service for coordination.
- **ed-kafka:** Kafka message broker for streaming data.
- **spark-iceberg:** Apache Spark with Iceberg integration for data storage and querying.
- **rest:** Iceberg REST API for accessing data.
- **minio:** MinIO object storage for storing Iceberg tables.
- **mc:** MinIO client for managing data in MinIO.

## Creating a Kafka Topic

1. **Open Docker Desktop.**
2. **Go to the "Containers" tab.**
3. **Find the "ed-kafka" container.**
4. **Click "Open shell".**
5. **Run the following command to create a Kafka topic named "device-data":**

    ```bash
    kafka-topics --create --topic device-data --bootstrap-server localhost:29092
    ```

## Accessing Jupyter Notebook

1. **Open your web browser and navigate to [http://localhost:8888](http://localhost:8888).**
2. **Create a password to access Jupyter Notebook if prompted.**

## Running the Data Producer

1. **Open a terminal inside Visual Studio Code.**
2. **Navigate to the project directory.**
3. **Run the following command to start the data producer:**

    ```bash
    python producer.py
    ```

   This will send data to the "device-data" Kafka topic.

## Data Processing and Storage

The Apache Spark application will consume the streaming data from Kafka, process it, and save it into Iceberg tables stored in MinIO.

## Additional Notes

- The `docker-compose.yml` file contains environment variables for configuration. Modify them as needed to suit your requirements.
- Refer to the documentation of each service for more details.

This README provides a basic overview of the project. Feel free to explore the code and experiment further.