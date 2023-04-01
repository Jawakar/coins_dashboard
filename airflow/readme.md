Airflow DAG for ingesting data into GCP buckets
This directory contains an Airflow DAG (Directed Acyclic Graph) job that runs the ingest_data.py script every 5 minutes. The ingest_data.py script is designed to properly structure and store the data in GCP buckets in raw JSON format, making it easier to process and analyze the data later on.

Requirements
Before running the DAG, you'll need to make sure you have the following dependencies installed:

Docker
Docker Compose
Google Cloud SDK
You'll also need to have the necessary permissions to access the GCP buckets where the data will be stored.

Installation
To install and run the DAG with Docker Compose, follow these steps:

Clone the repository to your local machine:
bash
Copy code
git clone <repository_url>
Build the Docker images by running the following command in the root directory of the project:
Copy code
docker-compose build
Initialize the Airflow database by running the following command:
arduino
Copy code
docker-compose run --rm webserver airflow initdb
Modify the ingest_data.py script to work with your specific data source. You may also need to modify the bucket_name variable in the script to match the name of the GCP bucket where you want to store the data.

Start the Airflow services with Docker Compose:

Copy code
docker-compose up
This will start the Airflow services and begin running the ingest_data.py script every 5 minutes.

Usage
To view the Airflow web UI, open a browser and go to localhost:8080. From there, you can see the status of the DAG and its tasks.

You can also start the DAG manually by clicking the "Trigger DAG" button on the DAG's page in the Airflow web UI.

Conclusion
By using Airflow and the ingest_data.py script with Docker Compose, you can easily automate the process of ingesting data into GCP buckets, making it easier to process and analyze your data.






