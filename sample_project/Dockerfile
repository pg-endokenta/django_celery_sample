# Use the official Python image from the Docker Hub
FROM python:3.13.0-slim-bullseye

# Set the working directory in the container
WORKDIR /sample_project

# Copy the requirements file into the container
COPY requirements.txt /sample_project/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /sample_project/

