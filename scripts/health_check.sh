#!/bin/bash

URL="http://localhost:5000/health"

response=$(curl -s $URL)

echo "Application Health Check:"
echo $response