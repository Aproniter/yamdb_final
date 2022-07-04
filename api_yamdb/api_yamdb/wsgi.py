import os

from users.models import User
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_yamdb.settings')

application = get_wsgi_application()


# try:
#     users = User.objects.get(username=os.getenv('DJANGO_SUPERUSER_USERNAME'))
# except User.DoesNotExist:
#     User.objects.create_superuser(
#         username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
#         email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
#         password=os.getenv('DJANGO_SUPERUSER_PASSWORD'),
#         is_active=True,
#         is_staff=True
#     )
