#!/bin/bash

echo "Starting deployment..."

docker stop infrawatch-container || true
docker rm infrawatch-container || true

docker build -t infrawatch .

docker run -d \
-p 5000:5000 \
--name infrawatch-container \
infrawatch

echo "Deployment completed!"