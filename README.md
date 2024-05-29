# Data Platform Setup and Demonstration

This project demonstrates a data platform setup using Docker, featuring Apache Spark, Apache Kafka, and Iceberg, along with a demonstration of streaming data processing with Apache Spark.

## Prerequisites

- **Docker:** Install Docker from [here](https://docs.docker.com/engine/install/).
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

## Services Overview

The `docker-compose.yml` file defines several services that work together:

- **spark-iceberg:** Jupyter Notebook environment with Apache Spark and Iceberg integration.
- **iceberg-rest:** REST API for accessing Iceberg data.
- **minio:** MinIO object storage for storing Iceberg tables.
- **mc:** MinIO client for managing data in MinIO.

## Additional Setup for Streaming Data Demonstration

1. **Open the `spark-iceberg` container:**
   - Use Docker Desktop or run the following command in your terminal:

     ```bash
     docker exec -it spark-iceberg /bin/bash
     ```

2. **Install `ncat` and start a socket listener:**

    ```bash
    sudo sh -c 'apt-get update; sudo apt-get install -y ncat; sudo ncat -l 9999'
    ```

3. **Access Jupyter Notebook:**
   - Open your web browser and navigate to [http://localhost:8888](http://localhost:8888).
   - Open the `notebooks` folder to find the example notebooks `01_data_frame_example.ipynb` and `02_reading_from_sockets.ipynb`.

## Demonstration of Socket Streaming and Processing

1. **Open the notebook `02_reading_from_sockets.ipynb` in Jupyter Notebook.**
2. **Run all cells in the notebook:**
   - This notebook demonstrates streaming data processing where Apache Spark consumes data from the socket, processes it to count words, and displays the results in the console.

## Additional Notes

- The `docker-compose.yml` file contains environment variables for configuration. Modify them as needed to suit your requirements.
- Refer to the documentation of each service for more details.
- For Kafka topic creation and data production, please refer to the detailed README section in the project directory.

Feel free to explore the code and experiment further with the notebooks and services provided.