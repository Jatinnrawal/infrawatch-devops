#!/bin/bash

mkdir -p backups

timestamp=$(date +%Y%m%d_%H%M%S)

tar -czvf backups/infrawatch_$timestamp.tar.gz .

echo "Backup completed!"