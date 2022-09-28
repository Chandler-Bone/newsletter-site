from django.contrib import admin

# Register your models here.
from .models import RegisteredUser

#adds registereduser model to admin site for debugging
admin.site.register(RegisteredUser)