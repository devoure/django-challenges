# link new image from another image of python
FROM python:3.8-alpine

# Allow container to log python print statements
ENV PYTHONUNBUFFERED 1

COPY ./async_tasks/requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

# Install requirements
RUN pip install -r /requirements.txt

RUN mkdir /app

# COPY files in the host machine to the container
COPY ./async_tasks /app

# Copy the entrypoint file from machine to container
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

# Change into the backend directory
WORKDIR /app

# Define entrypoint for container
ENTRYPOINT ["entrypoint.sh"]
