# Kube-python

### Set up python environment:
1- create virtual environment- 

    python3 -m venv env

2- Activate virtual environment -

    source ./env/bin/activate

3- Test Python Setup (Should see '/usr/bin/pip3
') -

    which pip3

4- Upgrade pip within the virtual environment -

    python3 -m pip install --upgrade pip

5 - Add 3 folders for app, docker, and kubernetes -

    mkdir app
    mkdir docker
    mkdir kubernetes

### To Build Docker Image
1- To capture current state(dependencies) of pip -

    pip freeze > requirements.txt 

    Note: Move resulted to ./app

2- To build the docker image -

    docker build -f docker/Dockerfile -t fast-api-python:latest . --progress=plain --no-cache

### To Run Docker Image

    docker run -p 8000:8000 fast-api-python:latest