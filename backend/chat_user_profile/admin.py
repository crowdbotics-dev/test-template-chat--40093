from django.contrib import admin
from .models import Contact,Profile,VerificationCode
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(VerificationCode)

# Register your models here.
