from django.contrib import admin
from TestApp.models import register_db, company_db, emp_db

# Register your models here.
admin.site.register(register_db)
admin.site.register(company_db)
admin.site.register(emp_db)
