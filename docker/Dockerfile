# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3

# Set a working directory where all the setup would take place in the image
WORKDIR /ridemyway-api-django

# The default user that should be used
USER root

# copy the requirements which contains dependencies to be installed
COPY ./requirements.txt /ridemyway-api-django

# Install netcat and requirements
RUN apt-get update && apt-get install -y netcat
RUN pip install -r requirements.txt

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# All files in the root directory are copied here
COPY . .
