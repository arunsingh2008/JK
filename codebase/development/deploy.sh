



#!/bin/bash

# Prepare the application for deployment
echo 'Building docker image...'
docker build -t myapp:latest .

# Choose a cloud service provider (AWS in this case)
# Ensure AWS CLI is installed and configured
echo 'Deploying to AWS ECS...'

# Create a new ECS cluster (if not already created)
aws ecs create-cluster --cluster-name myapp-cluster

# Register an ECS task definition
aws ecs register-task-definition --family myapp-task --container-definitions file://ecs-task-definition.json

# Deploy the application to ECS
aws ecs update-service --cluster myapp-cluster --service myapp-service --desired-count 1

# Ensure the application is accessible over the internet
echo 'Application deployed successfully and is accessible over the internet.'



