#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Crear el superusuario (ajustado a tu modelo personalizado)
python manage.py shell <<EOF
from ecommerce.models import UserUseraccount  # Asegúrate de que el modelo esté correctamente importado
if not UserUseraccount.objects.filter(email='admin@example.com').exists():
    user = UserUseraccount.objects.create(
        email='admin@example.com',
        first_name='Admin',
        last_name='User',
        password='password123',  # Usa una contraseña más segura
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    user.set_password('password123')  # Establece la contraseña de manera segura
    user.save()
    print("Superusuario creado con éxito.")
else:
    print("El superusuario ya existe.")
EOF

# Puedes agregar más comandos si es necesario, como iniciar el servidor, etc.