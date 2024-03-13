#!/bin/bash

# Update package lists
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install Flask and Flask-Restful
pip3 install flask flask-restful

# Clone your Flask app repository (replace <repository_url> with your actual repository URL)
git clone <repository_url>

# Change directory to your Flask app directory
cd your_flask_app_directory

# Optionally, if you're using a virtual environment, create and activate it
# python3 -m venv venv
# source venv/bin/activate

# Set environment variables
export VM_ID=VM_0001
# export SECRET_KEY=your_secret_key
# export DATABASE_URL=your_database_url

# Run the Flask app
python3 app.py
