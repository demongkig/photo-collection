#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing project dependencies..."
pip install -r requirements.txt

echo "Collecting template styles and assets..."
python manage.py collectstatic --no-input

echo "Synchronizing database structure layouts..."
python manage.py migrate