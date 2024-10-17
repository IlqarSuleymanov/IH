#!/bin/bash

# Update package list and install necessary dependencies
echo "Updating package list..."
sudo apt update

echo "Installing dependencies..."
sudo apt install -y python3 python3-pip

# Clone the project from GitHub
echo "Cloning the project..."
git clone https://github.com/IlqarSuleymanov/IH.git

echo "Installation complete! You can now navigate to the IH directory and run the scripts."
