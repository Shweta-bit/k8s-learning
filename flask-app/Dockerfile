# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container (if you have one)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set environment variables
# ENV xyz=123

# Expose the port on which the Flask app runs
EXPOSE 5000

# Command to run the application
CMD ["python", "main.py"]

