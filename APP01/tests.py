import os


if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydjango.settings')
    import django
    django.setup()
    from APP01 import models
    res = models.Books.objects.filter()
    print(res)




