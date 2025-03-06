# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install required system packages for PyMuPDF
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libmupdf-dev \
    libfreetype6-dev \
    && apt-get clean

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port (Render uses port 10000 by default for Flask)
EXPOSE 10000

# Define the command to run the app
CMD ["python", "app.py"]