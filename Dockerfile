# Use Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Default command: run the Python script that processes all collections
CMD ["python", "run_all_collections.py"]
