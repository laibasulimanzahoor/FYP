# Use official Python image
FROM python:3.12.7-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    libtk8.6 \
    && rm -rf /var/lib/apt/lists/*
# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Command to run the app
CMD ["python", "main.py"]
