#!/bin/bash

# Check in to the project working directory
cd /ridemyway-api-django

# Wait for database connection before running the application and migrations
while ! netcat -z database 5432; do
    sleep 0.1
done

# Run migrations
python3 manage.py migrate

# Run the application
python3 manage.py runserver 0.0.0.0:8000 # listens on every interface on port 8000.
