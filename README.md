docker build -t waer .
docker run -it --rm --name waer -p 5000:5000 waer

gcloud auth login
sudo docker login -u _token -p "$(gcloud auth print-access-token)" https://gcr.io

docker tag waer gcr.io/waer-370612/test:latest
docker push gcr.io/waer-370612/test:latest

