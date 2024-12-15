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

A deploy workflow deploys the helm chart on a target eks cluster ( see helm deployment notes ).    

The two workflows coudl be chained so for every commit a build is made and the deploymnet is triggered ( workflow callign workflow ) .   

## Notes
Running on debug mode for verbose logging while testing ; ideally we woudl want some args passed tot he python app to define the run mode ( argparse ).    

## Helm deployment
The current deploymnet is expecting an Ingress Load Balancer controller.  

For TLS deploymnet, get a certificate and create the secret   
`kubectl create secret tls poc-nivetek-com --namespace flask-api --key privkey.pem --cert fullchain.pem`    

Edit the value file and add the cert path to the ingress TLS block    

Edit the values file on the alb annotation subnets; add two public subnet ids from your target cluster vpc as below     
`alb.ingress.kubernetes.io/subnets: subnet-058238a2692dd7eff, subnet-00531735de31acf5f`     

Create a namespace    
`kubectl create ns flask-api`   

Install the chart   
`helm install flask-api flask-api -n flask-api`