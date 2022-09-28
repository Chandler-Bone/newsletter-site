# Newsletter Site

### How to configure:

Edit the following enviroment variables in the `docker-compose.yml`

- TWILIO_ACCOUNT_SID=<TWILIO_ACCOUNT_SID>
- TWILIO_AUTH_TOKEN=<TWILIO_AUTHENTICATION_TOKEN>
- TWILIO_NUMBER=<TWILIO_PHONE_NUMBER>
- DEBUG=<0/1>

### How to run:

```bash 
cd project_2
docker-compose up
```

### How to configure (while running):
```bash
# setup database
cd app
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py makemigrations newsletter
docker-compose run web python manage.py migrate

# setup admin login
docker-compose run web python manage.py createsuperuser
```

### How to access:
http://localhost/
