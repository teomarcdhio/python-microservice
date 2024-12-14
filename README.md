# python-microservice
Basic Python microservice API built wiht Flask.   
The rest endpoint reutrns a json object with key "message" and value "Hello, world!"    

## Dev workspace
Setup the venv enviornmnet   
`python3 -m venv .venv`   
Activate the env   
`source .venv/bin/activate`   
Install dependecies   
`python3 -m pip install -r requirements.txt`  
Run the app   
`python3 main.py` 

## Build container
Build the container using the local Dockerfile    
`docker build -t flask-api:0.0.1 .`   

## Run the container locally
Run the container on your local machine exposing port 5000 to your host port 5000    
`docker run -p 5000:5000 flask-api:0.0.1`    

## Github actions
Every commit to the repo will trigger a build, test, containerisation and push to dockerhub.   

## Notes
Running on debug mode for verbose logging while testing ; ideally we woudl want some args passed tot he python app to define the run mode ( argparse ).    
