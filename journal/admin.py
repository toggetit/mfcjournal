from django.contrib import admin
from .models import Org, Actor, InRecord, OutRecord

# Register your models here.
admin.site.register(Org)
admin.site.register(Actor)
admin.site.register(InRecord)
admin.site.register(OutRecord)
