from django.contrib import admin

from .models import DataFileUpload
from .models import WebsiteAuth
# Register your models here.
admin.site.register(DataFileUpload)
admin.site.register(WebsiteAuth)