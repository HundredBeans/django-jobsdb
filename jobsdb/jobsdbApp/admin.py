from .models import Artikel, Lowongan
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

# Register your models here.


admin.site.register(Artikel)
admin.site.register(Lowongan)