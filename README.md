# Reddit to Redshift ETL Pipeline

This project retrieves posts from Reddit, processes the data, stores it in Amazon S3, and loads the final output into Amazon Redshift. The workflow is managed using Apache Airflow, containerized with Docker for easy local development.

---

## 🛠️ Features

- 🔄 **Automated data pipeline** with Apache Airflow
- 🗃️ **Raw and processed data** stored in S3
- 🎯 **Target: Redshift** for analytics-ready data
- 🐍 Modular Python code for flexibility and clarity
- 🐳 Dockerized environment for quick setup

---

## 📁 Project Structure

```
project-root/
├── config/
│ └── config.conf # Configuration for API keys, S3 paths, etc.
├── dags/
│ └── reddit_dag.py # Airflow DAG for the pipeline
├── data/
│ ├── input/ # Raw Reddit data
│ └── output/ # Transformed data
├── etls/
│ ├── aws_etl.py # Load data from S3 to Redshift
│ └── reddit_etl.py # Transform Reddit data
├── pipelines/
│ ├── aws_s3_pipeline.py # Upload transformed data to S3
│ └── reddit_pipeline.py # Retrieve and prepare Reddit data
├── utils/
│ ├── constants.py # Global constants
│ └── utils.py # Utility functions
├── venv/ # Python virtual environment
├── airflow.env # Airflow environment variables
├── docker-compose.yml # Docker services configuration
├── Dockerfile # Docker image definition
└── requirements.txt # Python dependencies
```
---

## 🚀 How It Works

1. **Extract**: Fetch posts from Reddit using the Reddit API.
2. **Transform**: Clean and structure the data using `reddit_etl.py`.
3. **Load to S3**: Save raw and transformed data to Amazon S3.
4. **Load to Redshift**: Use `aws_etl.py` to move data from S3 into Redshift tables.
5. **Orchestrate**: `reddit_dag.py` schedules and runs the full workflow with Airflow.

---

## 🐳 Quick Start (Docker)

```bash
# Clone the repository
git clone https://github.com/your-username/reddit-to-redshift.git
cd reddit-to-redshift

# Start Airflow and services
docker-compose up --build

```

---
## 📦 Requirements

- Reddit API credentials: https://www.reddit.com/prefs/apps
- AWS account with:
S3 bucket <br>
S3 Glue: ETL and Crawler <br>
Redshift (serverless recommended) <br>
IAM role with necessary permissions <br>
Note: For testing, be sure that everything will be clean and data size is small

