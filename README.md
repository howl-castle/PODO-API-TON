# API for PODO iOS

### 0. Why API and iOS for a dApp?
- Flawless user experience has been considered to be the main key to achieve MASS ADOPTION in blockchain
- Powered by Dall-E engine, we deliver customers with brief+eye-catching pictures.
- Providing web2 way sign-up/sign-in experience to our customers (WalletSig is not necessary when logging-in)
- Thus, we provide AccountAbstraction-Like experience to our users
- Backed by DjangoRestFrameWork-Swagger API, iOS client

![IA](https://github.com/howl-castle/PODO-API-TON/blob/main/IA.png?raw=true)


### 1. Deployed on https://gleaming-cove-378613.ue.r.appspot.com/ (WIP)


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

