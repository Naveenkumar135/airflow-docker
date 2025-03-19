FROM apache/airflow:2.7.3

# # Set environment variable to include the Airflow path
# ENV PYTHONPATH=/opt/airflow:$PYTHONPATH

# Copy your requirements.txt to the container
COPY requirements.txt /requirements.txt

# Upgrade pip to ensure we're using the latest version
RUN pip install --upgrade pip

# # Install the Postgres provider (and other necessary dependencies)
# RUN pip install apache-airflow-providers-postgres

# # Install Airflow if it's not part of the base image or update to a specific version
# RUN pip install apache-airflow==2.0.1

# Install the dependencies listed in the requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt


