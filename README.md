# PODO-API-TON


### 1. Deployed on https://gleaming-cove-378613.ue.r.appspot.com/


### 2. Main stacks
- DjangoRestFramework: https://www.django-rest-framework.org/
- OpenAPI and Swagger: https://drf-yasg.readthedocs.io/en/stable/
- GCP Appengine: https://cloud.google.com/appengine?hl=ko


### 3. Runserver

1. install packages and dependencies

```
  pip install -r requirements.txt
```

2. runserver

```
  python manage.py runserver
```

3. sign-in (admin)

```
  # createsuperuser, on BASE_DIR
    python manage.py createsuperuser

  # Head to 127.0.0.1:8000/admin
```

