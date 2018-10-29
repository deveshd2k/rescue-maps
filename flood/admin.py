from django.contrib import admin
from .models import Coordinates,Profile,userData,userInfo
# Register your models here.
admin.site.register(Coordinates)
admin.site.register(Profile)
admin.site.register(userData)
admin.site.register(userInfo)