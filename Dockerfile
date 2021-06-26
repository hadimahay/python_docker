# Alpine base image that contains python 3.10
FROM python:3.8.0b4-alpine3.10
# define the directory to work in
WORKDIR /code
# copy the requirements.txt file to the work directory
COPY requirements.txt .
COPY blog.py .
# Install some system deps in a virtual environment named .build-deps, you can name it what ever you want
# install pip dependencies in the same layer
RUN apt add --no-cache --virtual .build-deps \
    build-base openssl-dev pkgconfig libffi-dev \
    cups-dev jpeg-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt del .build-deps # delete the .build-deps in the same layer
# Copy rest of the source code
COPY src/ src/
# EXPOSE the needed ports, for example 8080
EXPOSE 8080
# Running Command or Entry Point
CMD python src/blog.py
