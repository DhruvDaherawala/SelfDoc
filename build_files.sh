#!/bin/bash

# Activate virtual environment
source /vercel/path0/venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Django migrations or other setup commands
python manage.py migrate

# Continue with the build process
# ...
