#!/bin/bash

echo "Rolling back..."

docker stop infrawatch-container
docker start infrawatch-container

echo "Rollback complete!"