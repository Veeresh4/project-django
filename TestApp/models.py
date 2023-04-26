from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""Declaring fields which are going to store data in db"""
class register_db(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fullname}"


"""model for compnay data"""
class company_db(models.Model):
    # emp_fullname = models.ForeignKey(emp_db, on_delete=models.CASCADE, related_name="company")     # foreign key for accessing employee data
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=10)
    company_email = models.EmailField()
    company_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name}"


"""model for employee data"""
class emp_db(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)           # creating another user in db
    company_name = models.ForeignKey(company_db, on_delete=models.CASCADE, related_name="employee")     # foreign key for accessing company data
    emp_id = models.IntegerField()
    emp_fullname = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_phone = models.CharField(max_length=10)
    emp_companyname = models.CharField(max_length=100)
    emp_role = models.CharField(max_length=100)
    emp_domain = models.CharField(max_length=100)
    emp_location = models.CharField(max_length=100)
    emp_status = models.BooleanField()
    # created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.emp_fullname}"
