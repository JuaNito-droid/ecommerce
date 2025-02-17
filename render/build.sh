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

# Crear un superusuario si no existe (esto es para evitar errores si el superusuario ya está creado)
python manage.py shell <<EOF
from apps.user.models import UserAccount
from django.db.utils import IntegrityError

try:
    # Verificar si el superusuario ya existe
    if not UserAccount.objects.filter(email="$EMAIL").exists():
        # Crear superusuario
        UserAccount.objects.create_superuser(email="$EMAIL", password="$PASSWORD", first_name="Admin", last_name="User")
        print("Superuser created successfully.")
    else:
        print("Superuser already exists.")
except IntegrityError as e:
    print(f"Error creating superuser: {e}")
EOF