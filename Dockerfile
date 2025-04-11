# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system packages (ALSA for audio, others for PDF rendering)
RUN apt-get update && apt-get install -y \
    alsa-utils \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variable for Google credentials (You will mount this later)
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

# Optional: expose a port if you want to run a future Flask or Streamlit app
# EXPOSE 8501

# Run your script
CMD ["python", "main.py"]
