# avo-api
Deploy ML model on flask and interact with json api

NB Commands

docker build -t requests -f DockerFileReq .
docker run -p 5001:5001 requests

docker build -t avo-api -f Dockerfile .
docker run -p 5000:5000 avo-api
