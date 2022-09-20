from django.contrib import admin

from FLServerSQLITEDjango.models import Table1

# Здесь указывается, что приложение использует описанную модель данных
admin.site.register(Table1)