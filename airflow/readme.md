# Airflow DAG for ingesting data into GCP buckets

This directory contains an Airflow DAG (Directed Acyclic Graph) job that runs the `ingest_data.py` script every 5 minutes. The `ingest_data.py` script is designed to properly structure and store the data in GCP buckets in raw JSON format, making it easier to process and analyze the data later on.

## Requirements

Before running the DAG, you'll need to make sure you have the following dependencies installed:

* Docker
* Docker Compose
* Google Cloud SDK

You'll also need to have the necessary permissions to access the GCP buckets where the data will be stored.

## Installation

To install and run the DAG with Docker Compose, follow these steps:

1. Clone the repository to your local machine:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git clone <repository_url>
</code></div></div></pre>

2. Build the Docker images by running the following command in the root directory of the project:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">docker-compose build
</code></div></div></pre>

3. Initialize the Airflow database by running the following command:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>arduino</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">docker-compose run --rm webserver airflow initdb
</code></div></div></pre>

4. Modify the `ingest_data.py` script to work with your specific data source. You may also need to modify the `bucket_name` variable in the script to match the name of the GCP bucket where you want to store the data.
5. Start the Airflow services with Docker Compose:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">docker-compose up
</code></div></div></pre>

This will start the Airflow services and begin running the `ingest_data.py` script every 5 minutes and partition the data based on timestamp.

## Usage

To view the Airflow web UI, open a browser and go to `localhost:8080`. From there, you can see the status of the DAG and its tasks.

You can also start the DAG manually by clicking the "Trigger DAG" button on the DAG's page in the Airflow web UI.

## Conclusion

By using Airflow and the `ingest_data.py` script with Docker Compose, you can easily automate the process of ingesting data into GCP buckets, making it easier to process and analyze your data.
