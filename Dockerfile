# Pull official base Python Docker image
FROM python:3.10.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install poetry 
RUN poetry install
# Copy the Fastapi project
COPY . /code/
