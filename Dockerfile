FROM apache/airflow:2.9.1-python3.10

COPY requirements.txt /requirements.txt

USER root
RUN apt-get update && apt-get install -y gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /requirements.txt
