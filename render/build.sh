#!/usr/bin/env bash
# Exit on error
set -o errexit


# Definir las variables de entorno necesarias
export DJANGO_SETTINGS_MODULE="core.settings"
export EMAIL="admin@vudera.com"
export PASSWORD="admin_password"



# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
