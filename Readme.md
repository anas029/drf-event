```bash
pip install djangorestframework dj-rest-auth django-allauth
```

settings.py

```python
# INSTALLED_APPS
# ...
'rest_framework.authtoken',
'allauth',
'allauth.account',
'dj_rest_auth',
'dj_rest_auth.registration',
# ...
```

```python
ACCOUNT_EMAIL_VERIFICATION = "none"
```

```python
# MIDDLEWARE
# ...
'allauth.account.middleware.AccountMiddleware',
# ...
```

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ]
}
```
