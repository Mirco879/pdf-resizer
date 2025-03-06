# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies required for PyMuPDF
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    libpng-dev \
    libjpeg-dev \
    zlib1g-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Define the environment variable for Flask app to listen on all interfaces
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask when the container launches
CMD ["flask", "run"]