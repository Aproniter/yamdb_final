import os

from users.models import User
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')

application = get_wsgi_application()

users = get_object_or_404(User, username=os.getenv('DJANGO_SUPERUSER_USERNAME'))

if not users:
    User.objects.create_superuser(
        username=os.getenv('DJANGO_SUPERUSER_USERNAME'), 
        email=os.getenv('DJANGO_SUPERUSER_EMAIL'), 
        password=os.getenv('DJANGO_SUPERUSER_PASSWORD'), 
        is_active=True, 
        is_staff=True
    )