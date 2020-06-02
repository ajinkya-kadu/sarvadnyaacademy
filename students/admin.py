from django.contrib import admin

# Register your models here.

from .models import Pdfupload
from .models import Admissions


admin.site.register(Pdfupload)
admin.site.register(Admissions)

