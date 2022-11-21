FROM public.ecr.aws/docker/library/python:3.7.12-slim-buster
RUN apt update
RUN apt install curl unzip gcc="4:8.3.0-1" python3-dev="3.7.3-1" -y\
    && rm -rf /var/lib/apt/lists/*

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
WORKDIR /
