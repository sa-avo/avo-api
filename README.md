# avo-api
Deploy ML model on flask and interact with json api

#Pre-conditions for execution

To execute this you will require Docker to be installed on Windows 10/MacOS/Ubuntu

https://docs.docker.com/desktop/windows/install/

The Docker installation sometimes requires an additional update to be installed

https://docs.microsoft.com/en-us/windows/wsl/install-manual

#NB Commands - only if pre-conditions are met

This builds this image that will host the server, Copy as is into terminal

docker build -t avo-api -f Dockerfile .

This runs the image deploying the Pipple model and exposing ports

docker run -p 5000:5000 avo-api

This builds the requests interface - very light python version

docker build -t requests -f DockerFileReq .

This will run the image allowing interaction with ML model

docker run -ti requests


