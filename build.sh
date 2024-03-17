#!/bin/bash
pip install -r requirements.txt
# Run Django collectstatic command to collect static files
python manage.py collectstatic --no-input

# Run any other necessary build steps here
# For example:
# python manage.py migrate
# python manage.py compress
# npm install
# npm run build
