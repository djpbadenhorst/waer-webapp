# README

## RUN LOCALLY
To run locally:
```
virtualenv venv --python=python3
. venv/bin/activate
pip install -r requirements.txt
flask --app=src/app run
```

## AUTHENTICATE DOCKER:
To authenticate docker:
```
gcloud auth login
```

## BUILD & PUSH CONTAINER
To build and push container:
```
docker build -t waer .
docker tag waer gcr.io/waer-370612/test:latest
docker push gcr.io/waer-370612/test:latest
```

## DEPLOY CONTAINER
To deploy new container image:
```
gcloud --project=waer-370612 run services update test --region=us-central1 --image=gcr.io/waer-370612/test:latest
```
