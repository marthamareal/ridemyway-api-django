# Ride My Way

[![CircleCI](https://circleci.com/gh/marthamareal/ridemyway-api-django/tree/develop.svg?style=svg)](https://circleci.com/gh/marthamareal/ridemyway-api-django/tree/develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/b25caa8a91890a31cd55/maintainability)](https://codeclimate.com/github/marthamareal/ridemyway-api-django/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b25caa8a91890a31cd55/test_coverage)](https://codeclimate.com/github/marthamareal/ridemyway-api-django/test_coverage)

## Description
Ride-My-Way is an application built to solve several problems within the transportation sector in the economy. It provides drivers with the ability to create ride offers and riders to join available ride offers.

This **API** is built using [Django Rest framework](https://www.django-rest-framework.org/), [Python](https://www.python.org/) as a language and [PostgreSQl](https://www.postgresql.org/) as a database engine and [Docker](https://www.docker.com/) as a development environment.
You can find its related architectural diagrams [here](https://docs.google.com/document/d/1levHW6qx5BvadlorrS6anW8C32KL9fmV5gDvCPlAKjE/edit?usp=sharing) and a tool for project management [here](https://www.pivotaltracker.com/n/projects/2272213).

## Project set up

clone the repository
```
     $ git clone https://github.com/marthamareal/ridemyway-api-django
```
- check if you have python installed
```
    $ python --version
```
- check if you have docker and docker-compose installed
```
    $ docker --version
    $ docker-compose --version
```
- check if you have postgres installed
```
    $ postgres --version
```
- Build and run application with docker
```
    $ docker-compose build
    $ docker-compose up
```

After the build, you can access and interact with the API using base url ` http://0.0.0.0:8000/
`
## Testing
```.run tests inside a contaioner
   $ docker-compose ps  # Check running containers
   $ docker exec -it ridemyway-api-django_app_1  # Open the container using bash
   $ pytest  # Run tests using Pytest tool
```
