from django.contrib import admin
from .models import Connection, Document, Matrix

admin.site.register(Matrix)
admin.site.register(Document)
admin.site.register(Connection)
