# Use Alpine Linux as base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache bash gcc libc-dev linux-headers musl-dev libffi-dev openssl-dev

# Install Flask
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flask pandas

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container's filesystem
COPY . /app

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
