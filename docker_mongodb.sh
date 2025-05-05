#!/bin/bash

# Exit on any error
set -e

# Function to print status
print_status() {
  echo -e "\n\033[1;34m$1\033[0m\n"
}

print_status "Updating packages..."
sudo apt-get update

print_status "Installing prerequisites..."
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

print_status "Pulling MongoDB image..."
docker pull mongodb/mongodb-community-server:latest

print_status "Running MongoDB container..."
docker-compose up --build -d mongodb
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:5.0-ubuntu2004

print_status "MongoDB is running on port 27017"
